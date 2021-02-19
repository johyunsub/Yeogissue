<template>
  <v-app id="app">
    <nav-bar />
    <v-main class="">
      <router-view />
    </v-main>
    <foot/>
  </v-app>
</template>

<script>
import NavBar from './components/bar/NavBar.vue';
import Foot from './components/Footer.vue';

export default {
  name: 'App',
  components: { NavBar, Foot},
  created() {
    if (localStorage.getItem('token') != null) {
      console.log(localStorage.getItem('token') + '<<<adfdddd');
      this.$store.commit('SET_LOGIN_TOKEN', localStorage.getItem('token'));
      this.$store.dispatch('userData', localStorage.getItem('email'));
    }
  },
};
</script>

<style lang="scss">
@font-face {
  font-family: 'S-CoreDream-4Regular';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-4Regular.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}
#app {
  font-family: 'S-CoreDream-4Regular', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
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

.text-ellipsis {
  text-align: left;
  text-overflow: ellipsis;
  width: 90%;
  overflow: hidden;
  white-space: nowrap;
}
</style>
