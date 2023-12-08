<template>
  <div class="fixed top-0 sm:top-auto sm:bottom-0 bg-primary-600 h-5 w-full blur-2xl transition-colors opacity-0" style="animation: bgshow 1s forwards;">
    
  </div>
</template>

<script setup>
  function rand() {
    return Math.floor(Math.random() * 100)
  }
  const colors = ["400","500","600","700"]
</script>

<style>
@keyframes bgshow {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>

