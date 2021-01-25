<template>
<<<<<<< HEAD
  <v-app id="inspire">
    <nav-bar/>
    <menu-bar/>
    <v-main class="">
=======
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> 
    </div>
>>>>>>> a78e6030ef30d1e78791c04fd4fbc81c75a5c125
    <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import NavBar from './components/bar/NavBar.vue';
import MenuBar from './components/bar/MenuBar.vue';

export default {
    components: { NavBar, MenuBar },
  };
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.border-bt{
  border-bottom: 1px solid rgb(238, 238, 238);
}
</style>
