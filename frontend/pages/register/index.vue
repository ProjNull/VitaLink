<script setup>
const isOpen = ref(false)
const selected = ref(0)
const date = ref(new Date())

const label = computed(() => date.value.toLocaleDateString('cs-CZ', { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' })
)
onMounted(()=> {
  isOpen.value = true;
})
</script>

<template>
  <SvgBG1></SvgBG1>
  <UModal v-model="isOpen" prevent-close :overlay="false">
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <template #header>
        
        <h1 class="text-center text-2xl">Registrace</h1>
        <img src="/logo.svg" class="w-20 mx-auto pt-2">
      </template>

      <UForm :validate="validate" :state="state" class="space-y-4" @submit="onSubmit">
        <UInput icon="i-heroicons-user-solid" variant="outline" color="gray" placeholder="Jméno"/>
        <UInput icon="i-heroicons-user-solid" variant="outline" color="gray" placeholder="Příjmení"/>
        <UPopover :popper="{ placement: 'bottom' }">
          <UButton icon="i-heroicons-calendar-days-20-solid" variant="outline" block :label="label" />

          <template #panel="{ close }">
            <LazyDatePicker v-model="date" @close="close" />
          </template>
        </UPopover>
        <UButton to="/register/qustions" block>Registrovat</UButton>
        <UButton to="/login" block variant="link" color="primary">Přihlásit</UButton>
      </UForm>

    </UCard>
  </UModal>

</template>