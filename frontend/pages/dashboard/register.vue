<script setup>
const isOpen = ref(true)
const qrcode = ref(false)
const selected = ref(0)
const date = ref(new Date())
const runtimeConfig = useRuntimeConfig()

const qrdata = ref("")
const label = computed(() => date.value.toLocaleDateString('cs-CZ', { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' })
)
onMounted(()=> {
  isOpen.value = true;
})

var state = ref({
  first: undefined,
  last: undefined
})


function onSubmit() {
  qrdata.value = encodeURI(`${location.host}/register?first=${state.value.first}&last=${state.value.last}&date=${date.value.toISOString()}`)
  console.log(qrdata.value)
  qrcode.value = true
}
</script>

<template>
  <UModal v-model="isOpen" prevent-close :overlay="false">
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <template #header>
        
        <h1 class="text-center text-2xl">Registrace</h1>
        <img src="/logo.svg" class="w-20 mx-auto pt-2">
      </template>

      <UForm :state="state" class="space-y-4" @submit="onSubmit">
        <UInput icon="i-heroicons-user-solid" v-model="state.first" variant="outline" color="gray" placeholder="Jméno"/>
        <UInput icon="i-heroicons-user-solid" v-model="state.last" variant="outline" color="gray" placeholder="Příjmení"/>
        <UPopover :popper="{ placement: 'bottom' }">
          <UButton icon="i-heroicons-calendar-days-20-solid" variant="outline" block :label="label" />

          <template #panel="{ close }">
            <LazyDatePicker v-model="date" @close="close" />
          </template>
        </UPopover>
        <UButton type="submit" block>Registrovat</UButton>
        <UButton to="/login" block variant="link" color="primary">Přihlásit</UButton>
      </UForm>
    </UCard>
  </UModal>

  <UModal v-model="qrcode" prevent-close>
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <div class="w-full aspect-square overflow-hidden rounded-lg bg-gray-50 block h-auto relative isolate" style="aspect-ratio: 1/1;">
        <Icon name="i-heroicons-arrow-path" class="qrloading text-primary-500 z-[-1]" size="4rem" ></Icon>
        <img class="w-full aspect-square bg-gray-50 block z-20" style="aspect-ratio: 1/1;" :src="`${runtimeConfig.public.apiURL}/genqr?data=${encodeURIComponent('http://'+qrdata)}`">
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
        <p>Načtěte QR Kód pomocí mobolního telefonu.Nebo kliněte <a :href="'http://'+qrdata" target="_blank">sem</a></p>
        
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