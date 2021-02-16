<template>
  <v-container>
    <news-card v-for="(urlData, n) in clubDetailUrl" :key="n" :urlData="urlData" :type="'club'" />
  </v-container>
</template>

<script>
import NewsCard from '../../NewsCard.vue';
import { mapState, mapActions } from 'vuex';

export default {
  components: { NewsCard },
  computed: {
    ...mapState('clubStore', ['clubDetailUrl']),
  },
  props: {
    categoryType: { Type: String },
  },
  methods: {
    ...mapActions('clubStore', ['clubDetailUrlListNews']),
  },
  created() {
    console.log('되나?');
    this.clubDetailUrlListNews();
  },
};
</script>
