<template>
    <v-app-bar
      app
      color="white"
      flat
      id="navbar"
    >
      <v-container class="py-0 fill-height" >
        <v-col>
        <v-avatar
          class="mr-10"
          color="grey darken-1"
          size="32"
          @click="MovePage('home')"
        >로고</v-avatar>

        <v-btn text @click="MovePage('opinion')">의견나눔공간</v-btn>
        <v-btn text @click="MovePage('club')">클럽</v-btn>
        <v-btn text @click="MovePage('issue')">이슈모음</v-btn>
        <v-btn text @click="MovePage('data')">데이터</v-btn>
        </v-col>
        
        <v-btn text @click="OnOff('login')">로그인</v-btn>
        <notification/>
        <v-app-bar-nav-icon x-large @click="OnOff('menu')"></v-app-bar-nav-icon>
        <login/>

      </v-container>
    </v-app-bar>
</template>

<script>
import Login from '../Login/Login.vue'
import Notification from './Notification.vue';

export default {
  components: { Notification, Login },
    methods: {
    OnOff: function(message) {
      switch(message){
          case 'menu' : this.$store.commit('CHANGE_DRAWER', true); break;
          case 'login' : this.$store.commit('CHANGE_DIALOG', true); break;
        }
    },
    MovePage : function(check){
        switch(check){
          case 'opinion' : this.$router.push({ name: 'Opinion' }); break;
          case 'home' : this.$router.push({ name: 'Home' }); break;
          case 'club' : this.$router.push({ name: 'Club' }); break;
          case 'issue' : this.$router.push({ name: 'Issue' }); break;
          case 'data' : this.$router.push({ name: 'data' }); break;
        }
    }
  },
}
</script>

<style lang="scss">
#navbar{
  border-bottom: 2px ridge black;
}
</style>