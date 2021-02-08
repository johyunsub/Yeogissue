<template>
  <v-row class="mr-tp mr-le" style="padding-top: 20px;">
    <v-tabs fixed-tabs v-model="cateBtn" color="deep-purple accent-3" group borderless>
      <v-tab class="" outlined @click="categoryChange('전체')">전체</v-tab>
      <v-tab class="" outlined @click="categoryChange('연예')">연예</v-tab>
      <v-tab class="" outlined @click="categoryChange('IT/과학')">IT/과학</v-tab>
      <v-tab class="" outlined @click="categoryChange('해외')">해외</v-tab>
      <v-tab class="" outlined @click="categoryChange('경제')">경제</v-tab>
      <v-tab class="" outlined @click="categoryChange('스포츠')">스포츠</v-tab>
      <v-tab class="" outlined @click="categoryChange('정치')">정치</v-tab>
      <v-tab class="" outlined @click="categoryChange('사회')">사회</v-tab>
      <v-tab class="" outlined @click="categoryChange('생활')">생활</v-tab>
    </v-tabs>
  </v-row>
  
</template>

<script>
import { mapActions } from 'vuex';
// import $ from 'jquery';

export default {
  data: function() {
    return {
      cateBtn: 0,
    };
  },
  // updated() {
  //     $('#allclick').trigger('click');
  // },
  methods: {
    ...mapActions('opinionStore', ['opinionCategorySelelct']),
    categoryChange: function(change) {
      this.opinionCategorySelelct(change);
    },
  },
};
</script>
