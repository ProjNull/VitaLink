<template>
  <HomeContainer>
    <div class="flex items-center justify-between">
          <span></span>
          <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" to="/home/" />
      </div>
    <h3 class="block text-xl font-bold ">Hry</h3>
    <div class="relative w-[12rem] h-[12rem] mx-auto">
        <Icon name="i-fluent-emoji-beaming-face-with-smiling-eyes" class="main-img drop-shadow-xl m-4" size="10rem"></Icon>
        <Icon name="i-fluent-emoji-game-die" class="left-img drop-shadow-xl left-2 rotate-[-20deg] bottom-9 absolute" size="4rem"></Icon>
        <Icon name="i-fluent-emoji-trophy" class="right-small-img drop-shadow-xl right-1 rotate-[20deg] top-3 absolute" size="4rem"></Icon>
    </div>
    <!-- <h2>Nejlepší skóre</h2>
    <div class="w-fit mx-auto p-5 bg-cool-600 rounded-xl ">
        932809
    </div> -->
    <div class="flex flex-col md:flex-row gap-2 p-2 flex-wrap justify-center">
            <UButton to="/home/games/cards" class="sec flex flex-col">
                <div class="relative">
                    <h3 class="block text-xl font-bold">Pexeso</h3>
                    <Icon name="i-fluent-emoji-flower-playing-cards" class="main-img drop-shadow-xl m-4" size="10rem"></Icon>

                </div>
            </UButton>
            <UButton to="/home/games/snake" class="sec flex flex-col">
                <h3 class="block text-xl font-bold ">Had</h3>
                <div class="relative">
                    <Icon name="i-fluent-emoji-snake" class="main-img drop-shadow-xl m-4" size="10rem"></Icon>
                </div>
            </UButton>
            <UButton to="/home/games/tictactoe" class="sec flex flex-col">
                <h3 class="block text-xl font-bold ">Tic-Tac-Toe</h3>
                <div class="relative h-[12rem] w-[12rem]">
                    <Icon name="i-fluent-emoji-record-button" class="main-img drop-shadow-xl m-4 left-0 top-0 absolute" size="5rem"></Icon>
                    <Icon name="i-fluent-emoji-cross-mark-button" class="main-img drop-shadow-xl m-4 bottom-0 right-0 absolute" size="5rem"></Icon>
                </div>
                <!-- <Icon name="i-fluent-emoji-thought-balloon" class="drop-shadow-xl m-4" size="10rem"></Icon> -->
            </UButton>
        </div>
    <!--  -->
  </HomeContainer>
</template>

<script lang="ts" setup>

</script>

<style>

</style>

