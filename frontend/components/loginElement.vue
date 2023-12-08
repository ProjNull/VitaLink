<script setup>
const isOpen = ref(false)


onMounted(()=> {
  isOpen.value = true;
})
</script>

<template>
  <UModal v-model="isOpen">
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <template #header>
        <h1>Přihlášení</h1>
      </template>
      <UForm :validate="validate" :state="state" class="space-y-4" @submit="onSubmit">
        <UInput variant="outline" placeholder="Heslo"/>

        <UButton block>Přihlásit</UButton>
        <ULink class="block text-center underline">Registrace</ULink>
      </UForm>

    </UCard>
  </UModal>
</template>