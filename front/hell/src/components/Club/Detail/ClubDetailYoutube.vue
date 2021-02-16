<template>
  <v-container>
    <youtube-card v-for="(urlData, n) in clubDetailUrl" :key="n" :data="urlData" :type="'club'" />
  </v-container>
</template>

<script>
import YoutubeCard from '../../YoutubeCard';
import { mapState, mapActions } from 'vuex';

export default {
  components: { YoutubeCard },
  computed: {
    ...mapState('clubStore', ['clubDetailUrl']),
  },
  props: {
    categoryType: { Type: String },
  },
  methods: {
    ...mapActions('clubStore', ['clubDetailUrlListYoutube']),
  },
  created() {
    console.log('되나?');
    this.clubDetailUrlListYoutube();
  },
};
</script>
