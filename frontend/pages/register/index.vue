<script setup>
const state = ref([])
let statenow = 0
const selected = ref(0)
const date = ref(new Date())

const toast = useToast()
const router = useRouter()
const route = useRoute()

const label = computed(() => date.value.toLocaleDateString('cs-CZ', { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' })
)
onMounted(()=> {
  state.value[statenow] = true
})

const items = [{
  key: "register",
  label: 'Registrace',
  disabled: true,
  content: 'And, this is the content for Tab2'
}, {
  key: "code",
  label: 'Kód',
  disabled: true,
  content: 'Finally, this is the content for Tab3'
}]


function register() {
  toast.add({title:"Registruji"})

  setTimeout(()=> {
    toast.add({title:"Registrace dokončena"})
    setTimeout(()=> {
      router.push("/register/questions")
    },1000)
  }, 500)
}

function stateUP() {
  statenow++

  state.value[statenow - 1] = false
  state.value[statenow] = true
}

</script>

<template>
    <SvgBG1></SvgBG1>
    <UModal v-model="state[0]" prevent-close :overlay="false">
      <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <h1 class="text-center text-2xl">Vítá vás VitaLink</h1>
        <img src="/logo.svg" class="w-20 mx-auto pt-2">
        </template>
        <UDivider></UDivider>

        <h1>Lorem</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium enim reprehenderit repellendus assumenda blanditiis quo odio dolores consequuntur iusto nam iste ab maiores maxime consequatur sed, temporibus est a tempora!</p>


        <h1>Lorem</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium enim reprehenderit repellendus assumenda blanditiis quo odio dolores consequuntur iusto nam iste ab maiores maxime consequatur sed, temporibus est a tempora!</p>

        <template #footer>
          <div class="flex">
            <div class="flex flex-1 justify-start">
              <UButton variant="outline" @click="qustion -= 1">Zrušit</UButton>
            </div>
            <div class="flex flex-1 justify-end">
              <UButton @click="stateUP">Pokračovat</UButton>
            </div>
          </div>
        </template>
      </UCard>
    </UModal>

    <UModal v-model="state[1]" prevent-close :overlay="false">
      <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <h1 class="text-center text-2xl">Ověřte si své informace</h1>
        <img src="/logo.svg" class="w-20 mx-auto pt-2">
        </template>
        <h1>{{ route.query["first"] }}</h1>
        
        <template #footer>
          <div class="flex">
            <div class="flex flex-1 justify-start">
              <UButton variant="outline" @click="qustion -= 1">Zrušit</UButton>
            </div>
            <div class="flex flex-1 justify-end">
              <UButton @click="stateUP">Pokračovat</UButton>
            </div>
          </div>
        </template>
      </UCard>
    </UModal>

    <UModal v-model="state[2]" prevent-close :overlay="false">
      <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <h1 class="text-center text-2xl">Vytvořte si heslo</h1>
        <img src="/logo.svg" class="w-20 mx-auto pt-2">
        </template>
        
        <UInput placeholder="Heslo"></UInput>

        <template #footer>
          <div class="flex">
            <div class="flex flex-1 justify-start">
              <UButton variant="outline" @click="qustion -= 1">Zrušit</UButton>
            </div>
            <div class="flex flex-1 justify-end">
              <UButton @click="register">Registrovat</UButton>
            </div>
          </div>
        </template>
      </UCard>
    </UModal>

</template>