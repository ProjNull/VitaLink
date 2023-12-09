// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxt/ui",
    "@hypernym/nuxt-anime",
    'nuxt-icon',
    "@vite-pwa/nuxt",
  ],
})