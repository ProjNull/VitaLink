<template>
  <div :style="{'font-size': size}">
    <slot></slot>
  </div>
</template>

<script setup>
  defineProps(["size"])
  
</script>