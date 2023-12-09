<script setup>

const nalada = ref(35)
const config = useAppConfig()
onMounted(() => {
    config.ui.primary = localStorage.getItem("color") ? localStorage.getItem("color") : "red"
})

</script>


<template>
    <HomeContainer>
        
        <img src="/logo.svg" class="w-20 mx-auto pt-2">
        <h1 class="text-center font-bold text-2xl">Vítej uzivatel.prezdivka</h1>
        <h2 class="pb-4 pt-1 text-gray-600 dark:text-gray-400">Společně se vyléčíme.</h2>

        <UDivider></UDivider>
        <div class="py-2 relative">
            <h2 class="font-bold">Náladoměr</h2>
            <div class="border-4 border-primary w-fit p-1 rounded-full mx-auto">
                <span v-if="nalada < 20" class="text-blue-500"><Icon name="i-fluent-emoji:loudly-crying-face" size="4rem"></Icon></span>
                <span v-else-if="nalada < 40" class="text-amber-500"><Icon name="i-fluent-emoji:disappointed-face" size="4rem"></Icon></span>
                <span v-else-if="nalada < 60" class="text-orange-500"><Icon name="i-fluent-emoji:face-with-diagonal-mouth" size="4rem"></Icon></span>
                <span v-else-if="nalada < 80" class="text-orange-500"><Icon name="i-fluent-emoji:slightly-smiling-face" size="4rem"></Icon></span>
                <span v-else class="text-green-500 font-bold"><Icon name="i-fluent-emoji:smiling-face-with-heart-eyes" size="4rem"></Icon></span>
            </div>
            <span v-if="nalada < 20" class="text-red-500">Smutný</span>
            <span v-else-if="nalada < 40" class="text-amber-500">Nepříjemný</span>
            <span v-else-if="nalada < 60" class="text-cyan-500">Neutrál</span>
            <span v-else-if="nalada < 80" class="text-emerald-500">Veselý</span>
            <span v-else class="text-green-500 font-bold">Šťastný</span>
        </div>
        <UDivider></UDivider>
        <div class="flex flex-col md:flex-row gap-2 p-2 flex-wrap justify-center">
            <UButton class="sec flex flex-col">
                <div class="relative">
                    <h3 class="block text-xl font-bold">Nálada</h3>
                    <Icon name="i-fluent-emoji:smiling-face-with-heart-eyes" class="main-img drop-shadow-xl m-4" size="10rem"></Icon>
                    <Icon name="i-fluent-emoji-expressionless-face" class="left-img drop-shadow-xl left-2 rotate-[-40deg] bottom-9 absolute" size="4rem"></Icon>
                    <Icon name="i-fluent-emoji-fearful-face" class="right-img drop-shadow-xl right-0 rotate-[30deg] top-8 absolute" size="4rem"></Icon>
                </div>
            </UButton>
            <!-- <UButton class="sec flex flex-col">
                <h3 class="block text-xl font-bold ">Otázky</h3>
                <div class="relative">
                    <Icon name="i-fluent-emoji-thinking-face" class="main-img drop-shadow-xl m-4" size="10rem"></Icon>
                    <Icon name="i-fluent-emoji-red-exclamation-mark" class="left-img drop-shadow-xl left-2 rotate-[-20deg] bottom-9 absolute" size="4rem"></Icon>
                    <Icon name="i-fluent-emoji-red-question-mark" class="right-img drop-shadow-xl right-0 rotate-[20deg] top-3 absolute" size="4rem"></Icon>
                </div>
            </UButton> -->
            <UButton to="/home/message" class="sec flex flex-col">
                <h3 class="block text-xl font-bold ">Zprávy / Otázky</h3>
                <div class="relative">
                    <Icon name="i-fluent-emoji-face-with-raised-eyebrow" class="main-img drop-shadow-xl m-4" size="10rem"></Icon>
                    <Icon name="i-fluent-emoji-left-speech-bubble" class="left-img drop-shadow-xl left-2 rotate-[-20deg] bottom-9 absolute" size="4rem"></Icon>
                    <Icon name="i-fluent-emoji-red-question-mark" class="right-small-img drop-shadow-xl right-0 rotate-[0deg] top-0 absolute" size="4rem"></Icon>
                </div>
                <!-- <Icon name="i-fluent-emoji-thought-balloon" class="drop-shadow-xl m-4" size="10rem"></Icon> -->
            </UButton>
            <UButton to="/home/games" class="sec flex flex-col">
                <h3 class="block text-xl font-bold ">Hry</h3>
                <div class="relative">
                    <Icon name="i-fluent-emoji-beaming-face-with-smiling-eyes" class="main-img drop-shadow-xl m-4" size="10rem"></Icon>
                    <Icon name="i-fluent-emoji-game-die" class="left-img drop-shadow-xl left-2 rotate-[-20deg] bottom-9 absolute" size="4rem"></Icon>
                    <Icon name="i-fluent-emoji-trophy" class="right-small-img drop-shadow-xl right-1 rotate-[20deg] top-3 absolute" size="4rem"></Icon>
                </div>
                <!--  -->
                <!-- <Icon name="i-fluent-emoji-thought-balloon" class="drop-shadow-xl m-4" size="10rem"></Icon> -->
            </UButton>
            <URange v-model="nalada" name="range" />
        </div>
        

    </HomeContainer>

    
    
</template>

<style scoped>
    .sec * {
        @apply transition-all duration-200;
        transition-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .sec:hover .main-img {
        @apply scale-110
    }

    .left-img,
    .right-img,
    .right-small-img {
        @apply opacity-0;
    }
    .sec:hover .left-img {
        @apply delay-[30ms];
        @apply scale-110 -translate-x-3 translate-y-3 rotate-[-46deg] opacity-100
        
    }
    .sec:hover .right-img {
        @apply delay-[50ms];
        @apply scale-110 translate-x-3 -translate-y-3 rotate-[46deg] opacity-100
    }

    .sec:hover .right-small-img {
        @apply delay-75;
        @apply scale-110 translate-x-3 translate-y-1 rotate-[10deg] opacity-100
    }
</style>