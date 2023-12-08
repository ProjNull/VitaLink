<script setup>
const isOpen = ref(false)
const qustion = ref(0)

const nalada = ref(0)

const advancedcolors = ref(false)

const zakladnibarvy = ["red","yellow","lime","blue","violet","pink"]
const barvy = ["red","orange","amber","yellow","lime","green","emerald","teal","cyan","sky","blue","indigo","violet","purple","fuchsia","pink","rose"]

function changeColor(barva) {
  config.ui.primary = barva
  localStorage.setItem("color", barva)
}

function selected(barva) {
  if (config.ui.primary == barva) {
    return "solid"
  }
  return "outline"
}

const config = useAppConfig()
function onSubmit (form) {
  console.log('Submitted form:', form)
}
onMounted(()=> {
  isOpen.value = true;
})
</script>

<template>
  <SvgBG1></SvgBG1>
  <UModal v-model="isOpen" prevent-close :overlay="false">
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <template #header>
        <h1 class="text-center text-2xl">Pár Otázek</h1>
        
      </template>
      
      <div v-if="qustion == 0">
        <h1>Jak ti máme říkat?</h1>
        <UInput></UInput>
      </div>
      <div v-if="qustion == 1">
        <h1>Jak se cítíš?</h1>
        <URange v-model="nalada"></URange>
      </div>
      <div v-if="qustion == 2">
        <h1>Vyber tvou oblíbenou barvu</h1>
        <div class="text-right">
          <ULink
            class="text-gray-400 hover:text-primary hover:underline m-2"
            @click="advancedcolors = !advancedcolors"
          >
            <span v-if="advancedcolors == false">Víc</span>
            <span v-if="advancedcolors == true">Méně</span>
          </ULink>
        </div>
        <div class="flex flex-wrap gap-2 justify-center">
          <template v-if="advancedcolors == false" v-for="barva in zakladnibarvy">
            <UButton square="true" @click="changeColor(barva)" :color="barva" :variant="selected(barva)" size="xl" padded="true">
              <UIcon name="i-heroicons-paint-brush-solid" />
            </UButton>
          </template>
          <template v-if="advancedcolors == true" v-for="barva in barvy">
            <UButton square="true" @click="changeColor(barva)" :color="barva" :variant="selected(barva)" size="xl" padded="true">
              <UIcon name="i-heroicons-paint-brush-solid" />
            </UButton>
          </template>
        </div>
        
      </div>
      <div v-if="qustion == 3">
        <h1>Qustion 4</h1>
      </div>
      <div v-if="qustion >= 4">
        <h1>Qustion 5</h1>
      </div>

      <template #footer>
        <div class="flex">
          <div class="flex flex-1 justify-start">
            <UButton v-if="qustion > 0" variant="outline" @click="qustion -= 1">Zpět</UButton>
          </div>
          <div class="flex flex-1 justify-end">
            <UButton v-if="qustion <= 3" @click="qustion++">Pokračovat</UButton>
            <UButton v-else-if="qustion > 3" @click="qustion++">Dokončit</UButton>
          </div>
        </div>
        

        

        
      </template>
      
    </UCard>
    <UProgress :ui="{'progress':{'rounded':''}}" :value="qustion" :max="4"></UProgress>
  </UModal>
</template>

<style>
h1 {
  @apply text-lg font-bold;
}
</style>