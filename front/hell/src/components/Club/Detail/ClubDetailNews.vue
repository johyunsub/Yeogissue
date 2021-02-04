<template>
  <v-container>
    <news-card :type="'club'" />
  </v-container>
</template>

<script>
import NewsCard from '../../NewsCard';
export default {
  components: { NewsCard },
};
</script>
