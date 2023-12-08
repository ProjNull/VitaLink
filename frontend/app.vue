<script setup>
const config = useAppConfig()
// onMounted(()=> {
//   config.ui.primary = localStorage.getItem("color") ? localStorage.getItem("color") : "red"
// })
</script>
<template>
  
  <NuxtPage />
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