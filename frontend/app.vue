<script setup>
const show = ref(true)
onMounted(()=> {
  show.value = false
})
</script>
<template>
  
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
  <Loading :show="show"></Loading>
  <UNotifications />
</template>


<style>
.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>