<script setup>
const config = useAppConfig()
config.ui.primary = localStorage.getItem("color") ? localStorage.getItem("color") : "red"
</script>

<template>
    <UContainer>
        <UCard>

        </UCard>
    </UContainer>
    
</template>