<script setup>
const isOpen = ref(false)
const selected = ref(0)
const date = ref(new Date())

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
</script>

<template>
    <SvgBG1></SvgBG1>
  <UModal v-model="isOpen" prevent-close :overlay="false">
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <template #header>
        <h1 class="text-center">Co je VitaLink</h1>
      </template>

      <h1>O</h1>

    </UCard>
  </UModal>

</template>