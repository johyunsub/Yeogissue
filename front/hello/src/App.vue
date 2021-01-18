<template>
  <v-app>
    <nav-bar></nav-bar>

    <v-main>
      <Home/>
    </v-main>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar.vue';
import Home from './views/Home';

export default {
  name: 'App',

  components: {
    Home,
    NavBar,
  },

  data: () => ({
    //
  }),
};
</script>
