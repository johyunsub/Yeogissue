<template>
  <v-row class="mr-tp mr-le" style="padding-top: 20px;">
    <v-btn-toggle v-model="cateBtn" color="deep-purple accent-3" group borderless>
      <v-btn class="border-bt" outlined @click="categoryChange('전체')">전체</v-btn>
      <v-btn class="border-bt" outlined @click="categoryChange('연예')">연예</v-btn>
      <v-btn class="" outlined @click="categoryChange('IT/과학')">IT/과학</v-btn>
      <v-btn class="" outlined @click="categoryChange('해외')">해외</v-btn>
      <v-btn class="" outlined @click="categoryChange('경제')">경제</v-btn>
      <v-btn class="" outlined @click="categoryChange('스포츠')">스포츠</v-btn>
      <v-btn class="" outlined @click="categoryChange('정치')">정치</v-btn>
      <v-btn class="" outlined @click="categoryChange('사회')">사회</v-btn>
      <v-btn class="" outlined @click="categoryChange('생활')">생활</v-btn>
    </v-btn-toggle>
  </v-row>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data: function() {
    return {
      cateBtn: 'center',
    };
  },
  methods: {
    ...mapActions('opinionStore', ['opinionCategorySelelct']),
    categoryChange: function(change) {
      this.opinionCategorySelelct(change);
    },
  },
};
</script>
