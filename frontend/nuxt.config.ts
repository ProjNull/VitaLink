// https://nuxt.com/docs/api/configuration/nuxt-config
export default {
  head: {
    script: [
        { src: './fetchApi.js' },
        // Add other global scripts here
    ],
  },
  devtools: { enabled: true },
  modules: [
    "@nuxt/ui",
    "@hypernym/nuxt-anime",
    'nuxt-icon',
    "@vite-pwa/nuxt",
  ],
}