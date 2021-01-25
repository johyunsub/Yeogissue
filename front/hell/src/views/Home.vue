<template>
<<<<<<< HEAD
  <v-container>
    <issue/>
    <opinion-slider/>
    <suggest-slider/>
  </v-container>
=======
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    </div>
>>>>>>> a78e6030ef30d1e78791c04fd4fbc81c75a5c125
</template>

<script>
import Issue from '../components/Home/Issue.vue';
import OpinionSlider from '../components/Home/OpinionSlider.vue';
import SuggestSlider from '../components/Home/SuggestSlider.vue';

export default {
  name: 'Home',
  components: { Issue, OpinionSlider, SuggestSlider },
}
</script>
