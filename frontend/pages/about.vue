<script setup>
const isOpen = ref(false)
const selected = ref(0)
const date = ref(new Date())

const toast = useToast()
const router = useRouter()

const label = computed(() => date.value.toLocaleDateString('cs-CZ', { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' })
)
onMounted(()=> {
  isOpen.value = true;
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


</script>

<template>
    <SvgBG1></SvgBG1>
    <UModal v-model="isOpen" prevent-close :overlay="false">
      <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <h1 class="text-center text-2xl">Co je VitaLink</h1>
        <img src="/logo.svg" class="w-20 mx-auto pt-2">
        </template>

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
              <UButton @click="register">Registrovat</UButton>
            </div>
          </div>
        </template>
      </UCard>
    </UModal>

</template>