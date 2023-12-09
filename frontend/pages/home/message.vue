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
  description: 'Make changes to your account here. Click save when you\'re done.'
}, {
  key: 'recieved',
  label: 'Přijaté',
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
            <UButton icon="i-heroicons-arrow-path-solid" square="" @click="router.go()"></UButton>
            <UButton icon="i-heroicons-pencil-solid" @click="writeMSG = true">Poslat Zprávu</UButton>
            
          </div>
        </div>
        
        
      </template>
      
      <UTabs :items="items" class="w-full">
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
            <UInput v-model="state.subject" placeholder="Predmět"></UInput>
          </UFormGroup>

          <UFormGroup label="Zpráva" name="message">
            <UTextarea v-model="state.message" resize placeholder="Zpráva" />
          </UFormGroup>
        
        
        <UButton type="submit" block="">Poslat</UButton>
        </UForm>
      </UCard>
    </UModal>
  </div>
</template>


