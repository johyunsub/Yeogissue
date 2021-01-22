<template>
  <v-container>
    <issue/>
    <opinion-slider/>
    <suggest-slider/>
  </v-container>
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
