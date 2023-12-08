<script setup>
const isOpen = ref(false)
const qustion = ref(0)

const toast = useToast()

const nickname = ref("")
const nalada = ref(0)

const advancedcolors = ref(false)

const zakladnibarvy = ["red","yellow","lime","blue","violet","pink"]
const barvy = ["red","orange","amber","yellow","lime","green","emerald","teal","cyan","sky","blue","indigo","violet","purple","fuchsia","pink","rose"]


const barvyPreklad = {
  "red": "Červená",
  "orange": "Oranžová",
  "amber": "Amber",
  "yellow": "Žlutá",
  "lime": "Limetka",
  "green": "Zelená",
  "emerald": "Emerald",
  "teal": "Modrozelená",
  "cyan": "Azurová",
  "sky": "Obloha",
  "blue": "Modrá",
  "indigo": "Indigová",
  "violet": "Fialová světle",
  "purple": "Fialová",
  "purple": "Růžová",
  "fuchsia":"Fuchsiová",
  "pink": "Růžová",
  "rose": "Ruže"
}

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

const emojis = [
  {
    icon: "i-fluent-emoji:smiling-face-with-heart-eyes",
    text:"Je mi dobře.",
    value: 5
  },{
    icon: "i-fluent-emoji:beaming-face-with-smiling-eyes",
    text:"Jsem spokojen.",
    value: 4
  },{
    icon: "i-fluent-emoji:face-with-diagonal-mouth",
    text:"Tak mezi.",
    value: 3
  },{
    icon: "i-fluent-emoji:disappointed-face",
    text:"Jsem smutný.",
    value: 2
  },{
    icon: "i-fluent-emoji:face-with-thermometer",
    text:"Je to prostě špatný.",
    value: 1
  },
]

const donequstions = ref([])

function nextQustion() {
  qustion.value++
}

function checkAll() {
  let isOK = true;
  if (nickname.value == "") {
    toast.add({
      title: 'Není zadaná přezdívka.',
      icon: 'i-heroicons:exclamation-triangle-solid',
    })
    isOK = false;
  }

  if (nalada.value == 0) {
    toast.add({
      title: 'Není zadaná nálada.',
      icon: 'i-heroicons:exclamation-triangle-solid',
    })
    isOK = false;
  }

  if (isOK) {
    toast.add({
      title: 'Posílám',
      icon: 'i-heroicons:check-badge-solid',
    })
  }
}

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
        <UInput v-model="nickname"></UInput>
      </div>
      <div v-if="qustion == 1">
        <h1>Jak se cítíš?</h1>
        <div class="flex justify-center py-2">
          <template v-for="emoji in emojis">
            <button @click="nalada = emoji.value" class="transition-all" style="transition-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);" :class="{'scale-125 drop-shadow-2xl z-20 mx-3': nalada == emoji.value, 'brightness-75': (nalada != 0 && nalada != emoji.value)}">
              <Icon size="3rem" :name="emoji.icon"></Icon>
            </button>
          </template>
        </div>
        <UDivider/>
        <div class="text-center">
          <span :class="{'hidden': (nalada != 0)}">
              Vyberte náladu
            </span>
          <template v-for="emoji in emojis">
            <span :class="{'hidden': (nalada != emoji.value)}">
              {{ emoji.text }}
            </span>
          </template>
        </div>
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
              <UIcon name="i-heroicons-paint-brush-solid" /> {{ barvyPreklad[barva] }}
            </UButton>
          </template>
          <template v-if="advancedcolors == true" v-for="barva in barvy">
            <UButton square="true" @click="changeColor(barva)" :color="barva" :variant="selected(barva)" size="xl" padded="true">
              <UIcon name="i-heroicons-paint-brush-solid" /> {{ barvyPreklad[barva] }}
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
            <UButton v-if="qustion <= 3" @click="nextQustion()">Pokračovat</UButton>
            <UButton v-else-if="qustion > 3" @click="checkAll()">Dokončit</UButton>
          </div>
        </div>
        <div class="flex justify-stretc gap-1 mx-auto mt-4">
          <template v-for="i in 5">
            <div class="h-2 flex-1 rounded-xl transition-color duration-500" :class="{'bg-primary-500': qustion + 1 > i,'bg-primary-300':qustion + 1 == i,'bg-gray-700': qustion + 1 < i}">
            </div>
          </template>
        </div>

        

        
      </template>
      
    </UCard>
    
    <!-- <UProgress :ui="{'progress':{'rounded':''}}" :value="qustion" :max="4"></UProgress> -->
  </UModal>
</template>

<style>
h1 {
  @apply text-lg font-bold;
}
</style>