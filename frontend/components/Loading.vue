<script setup>
  defineProps(["show"])
</script>
<template>
  <div class="fixed w-screen h-screen bg-cool-900 top-0 left-0 z-[222] transition-opacity duration-500" :class="{'opacity-0 pointer-events-none':! show}">
    <div class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
      <svg class="absolute w-20 h-20 pulse text-primary-300 transition-colors duration-500" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="m11.645 20.91l-.007-.003l-.022-.012a15.247 15.247 0 0 1-.383-.218a25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25C2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052A5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25c0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17a15.247 15.247 0 0 1-.383.219l-.022.012l-.007.004l-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z"/></svg>

      <svg class="w-20 h-20 pulse-small text-primary-500 transition-colors duration-500" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="m11.645 20.91l-.007-.003l-.022-.012a15.247 15.247 0 0 1-.383-.218a25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25C2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052A5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25c0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17a15.247 15.247 0 0 1-.383.219l-.022.012l-.007.004l-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z"/></svg>
      
    </div>
  </div>

</template>

<style scoped>
  .pulse {
    animation: pulse 1000ms ease-out infinite;
  }

  .pulse-small {
    animation: pulse-small 1000ms ease-in-out infinite;
  }

  @keyframes pulse {
    0% {
      transform: scale(1);
      opacity: 0.3;
    }
    100% {
      transform: scale(3);
      opacity: 0;
    }
  }

  @keyframes pulse-small {
    0% {
      transform: scale(1);
    }
    10% {
      transform: scale(1.2);
    }
    60% {
      transform: scale(1);
    }
  }
</style>
<script setup lang="ts">
</script>