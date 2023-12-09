<template>
  <div class="flex justify-center items-center w-full h-screen">
    <UCard :ui="{'base': 'min-w-[20rem] max-w-[60rem] text-center'}">
      <template v-if="$slots.header"  #header>
        <slot name="header"></slot>
      </template>
      <slot></slot>
    </UCard>
  </div>
</template>

<script lang="ts" setup>

</script>

<style>

</style>

