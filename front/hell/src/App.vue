<template>
  <v-app id="inspire">
    <nav-bar />
    <menu-bar />
    <v-main class="">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import NavBar from './components/bar/NavBar.vue';
import MenuBar from './components/bar/MenuBar.vue';

export default {
  components: { NavBar, MenuBar },
  created() {
    if (localStorage.getItem('email') != '') {
      this.$store.dispatch(localStorage.getItem('email'));
      this.$store.commit('SET_LOGIN_TOKEN', localStorage.getItem('token'));
    }
  },
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

.border-bt {
  border-bottom: 1px solid rgb(238, 238, 238);
}

.btn-border {
  border: 1px solid black;
}

.mr-tp {
  margin-top: 20px;
}

.mr-bt {
  margin-bottom: 20px;
}

.mr-le {
  margin-left: 10px;
}

.mr-rt {
  margin-right: 10px;
}

.choice_cursor {
  cursor: pointer;
}

.back-gray:hover {
  background-color: rgb(204, 200, 200);
}
</style>
