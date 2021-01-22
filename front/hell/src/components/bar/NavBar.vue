<template>
    <v-app-bar
      app
      color="white"
      flat
      id="navbar"
    >
      <v-container class="py-0 fill-height" >
        <v-avatar
          class="mr-10"
          color="grey darken-1"
          size="32"
          @click="MovePage('home')"
        >로고</v-avatar>

        <v-btn text @click="MovePage('opinion')">의견나눔공간</v-btn>
        <v-btn text @click="MovePage('suggest')">제안하기</v-btn>
        <v-btn text @click="MovePage('issue')">이슈모음</v-btn>

        <v-spacer></v-spacer>

        <notification/>
        <v-app-bar-nav-icon x-large @click="OnOffMenu()"></v-app-bar-nav-icon>

      </v-container>
    </v-app-bar>
</template>

<script>
import Notification from './Notification.vue';

export default {
  components: { Notification },
    methods: {
    OnOffMenu: function() {
      console.log(this.$store.state.drawer);
      this.$store.commit('CHANGE_DRAWER', true);
    },
    MovePage : function(check){
        switch(check){
          case 'opinion' : this.$router.push({ name: 'Opinion' }); break;
          case 'home' : this.$router.push({ name: 'Home' }); break;
          case 'suggest' : this.$router.push({ name: 'Suggest' }); break;
          case 'issue' : this.$router.push({ name: 'Issue' }); break;
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