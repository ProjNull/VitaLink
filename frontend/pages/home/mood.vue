<script setup>
const config = useAppConfig()
onMounted(() => {
    config.ui.primary = localStorage.getItem("color") ? localStorage.getItem("color") : "red"
})
const writeMSG = ref(false)

const toast = useToast()
const router = useRouter()
const items = [{
  key: 'sended',
  label: 'Poslané',
  icon:"i-heroicons-cloud-arrow-down-solid",
  description: 'Make changes to your account here. Click save when you\'re done.'
}, {
  key: 'recieved',
  label: 'Přijaté',
  icon:"i-heroicons-cloud-arrow-up-solid",
  description: 'Change your password here. After saving, you\'ll be logged out.'
}]

const state = reactive({
  subject: undefined,
  message: undefined
})

const validate = (state) => {
  const errors = []
  if (!state.subject) errors.push({ path: 'email', message: 'Required' })
  if (!state.message) errors.push({ path: 'password', message: 'Required' })
  return errors
}

const questions = [{
  id:-1,
  name: "Jiné"
},{
  id:1,
  name: "Co je pro mě důležité."
},{
  id:2,
  name: "Co pro mě není důležité."
},{
  id:3,
  name: "Přál/bych is, abi..."
},{
  id:4,
  name: "Pomohlo my..."
},{
  id:5,
  name: "Bojím se..."
},{
  id:6,
  name: "Mám otázku..."
},{
  id:7,
  name: "Chtěl bych si promluvit s..."
},{
  id:8,
  name: "Můžu něco sám udělat?"
},{
  id:9,
  name: "Potřebuji..."
},{
  id:10,
  name: "Nerozumím..."
}
]
const predefined = ref(0)

const current = computed(() => {
  if (predefined.value == 0) {
    return {
      id:10,
      name: "Vyber možnost"
    }
  } else {
    return questions.find(question => question.id === predefined.value)
  }
  
})

async function onSubmit (event) {
  // Do something with data
  console.log(event.data)
  writeMSG.value = false
  toast.add({
    title:"Zpráva poslána!"
  })
}

</script>

<template>
  
  <UContainer>
    <UCard class="mt-5">
      <template #header>
        <div class="flex">
          <div class="flex-1 flex gap-1">
            <UButton icon="i-heroicons-arrow-left-20-solid" variant="outline" @click="router.push('/home')">Zpět</UButton>
            
          </div>
          <div class="flex-1 flex gap-1 justify-end">
            <UButton icon="i-heroicons-arrow-path-solid" square="" @click="router.go()">Aktualizovat</UButton>
            <UButton icon="i-heroicons-pencil-solid" @click="writeMSG = true">Poslat Zprávu</UButton>
            
          </div>
        </div>
        
        
      </template>
      
      <UTabs :items="items" class="w-full">
        <template #default="{ item, selected }">
          <div class="flex items-center gap-2 relative truncate">
            <UIcon :name="item.icon" class="w-4 h-4 flex-shrink-0" />

            <span class="truncate">{{ item.label }}</span>

            <span v-if="selected" class="absolute -right-4 w-2 h-2 rounded-full bg-primary-500 dark:bg-primary-400" />
          </div>
        </template>
        <template #item="{ item }">

            <div v-if="item.key === 'sended'" class="space-y-3">
              <template v-for="i in 10">
                <UCard>
                  <h1>Zpráva {{ i }}</h1>
                  <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Vero laborum volupta</p>
                </UCard>
              </template>
            </div>
            <div v-else-if="item.key === 'recieved'" class="space-y-3">
              <template v-for="i in 10">
                <UCard>
                  <h1>Zpráva {{ i }}</h1>
                  <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Vero laborum volupta</p>
                </UCard>
              </template>
            </div>
    
        </template>
      </UTabs>
    </UCard>
  </UContainer>
  <div>
    

    <UModal v-model="writeMSG">
      <UCard
        :ui="{
          base: 'h-full flex flex-col',
          rounded: '',
          divide: 'divide-y divide-gray-100 dark:divide-gray-800',
          body: {
            base: 'grow'
          }
        }"
      >
        <template #header>
          <div class="flex items-center justify-between">
            <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-white">
              Poslat Zprávu
            </h3>
            <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" @click="writeMSG = false" />
          </div>
        </template>
        <UForm :validate="validate" :state="state" class="space-y-4" @submit="onSubmit">
          
            <UFormGroup label="Předmět" name="subject">
              <USelectMenu
              v-model="predefined"
              :options="questions"
              placeholder="Select people"
              value-attribute="id"
              option-attribute="name"
            >
              <template #label>
                {{ current.name }}
              </template>
            </USelectMenu>
            <br v-if="current.id == -1">
            <UInput v-if="current.id == -1" v-model="state.subject" placeholder="Predmět"></UInput>
          </UFormGroup>

          <UFormGroup label="Zpráva" name="message">
            <UTextarea v-model="state.message" resize :ui="{'base':'min-h-[20rem]'}" placeholder="Zpráva" />
          </UFormGroup>
        
        
        <UButton type="submit" block="">Poslat</UButton>
        </UForm>
      </UCard>
    </UModal>
  </div>
</template>


