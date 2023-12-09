<template>
  <HomeContainer>
    <template #header>
      <div class="flex items-center justify-between">
          <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-white">
            Pexeso
          </h3>
          <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" to="/home/games" />
      </div>
    </template>
    <iframe src="/games/cards" class="bg-primary rounded-lg" width="360" height="460"></iframe>
  </HomeContainer>
</template>

<script lang="ts" setup>

</script>

<style>

</style>

