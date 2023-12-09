<script setup>
const isOpen = ref(false)
const qrcode = ref(false)
const selected = ref(0)
const date = ref(new Date())

const label = computed(() => date.value.toLocaleDateString('cs-CZ', { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' })
)
onMounted(()=> {
  qrcode.value = true;
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
        <UButton block>Registrovat</UButton>
        <UButton to="/login" block variant="link" color="primary">Přihlásit</UButton>
      </UForm>
    </UCard>
  </UModal>

  <UModal v-model="qrcode" prevent-close>
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <div class="w-full aspect-square overflow-hidden rounded-lg bg-gray-50 block h-auto relative" style="aspect-ratio: 1/1;">
        <Icon name="i-heroicons-arrow-path" class="qrloading text-primary-500" size="4rem" ></Icon>
        <img class="w-full aspect-square bg-gray-50 block" style="aspect-ratio: 1/1;" src="">
      </div>
      <template #header>
        <div class="flex items-center justify-between">
            <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-white">
              Registrační Kód
            </h3>
            <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" @click="qrcode = false" />
        </div>
      </template>
      <template #footer>
        <p>Načtěte QR Kód pomocí mobolního telefonu.</p>
      </template>
    </UCard>
  </UModal>

</template>

<style scoped>
.qrloading {
  @apply absolute top-1/2 left-1/2;
  animation: qrload 1s linear infinite;
}

@keyframes qrload {
  0% {
    transform: translate(-50%,-50%) rotate(0turn);
  }
  100% {
    transform: translate(-50%,-50%) rotate(1turn);
  }
}
</style>