<template>
  <div class="flex gap-3 mx-4 my-10">
    <slot name="outside" />
    <div class="flex flex-col gap-5">
      <img src="/logo.svg" class="w-20 mx-auto pt-2">
      <div class="bg-cool-100 dark:bg-cool-900 p-2 rounded-lg border border-gray-200 dark:border-gray-700">
        <UVerticalNavigation :links="links" />
      </div>
    </div>
   
    
    <div class="flex-1">
      <slot />
    </div>
  </div>
  
</template>

<script setup>
const links = [{
  label: 'Profile',
  avatar: {
    src: 'https://avatars.githubusercontent.com/u/739984?v=4'
  },
  badge: 100
}, {
  label: 'Installation',
  icon: 'i-heroicons-home',
  to: '/getting-started/installation'
}, {
  label: 'Vertical Navigation',
  icon: 'i-heroicons-chart-bar',
  to: '/navigation/vertical-navigation'
}, {
  label: 'Command Palette',
  icon: 'i-heroicons-command-line',
  to: '/navigation/command-palette'
}]
</script>

<style>

</style>

