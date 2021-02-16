<template>
  <div>
    <!-- 카테고리 if문 처리-->
    <v-row class="category mt-15">
      <v-col cols="4"></v-col>
      <v-col>
        <v-tabs>
          <v-tab @click="SelectCategory('intro')">소개</v-tab>
          <v-tab @click="SelectCategory('news')">뉴스</v-tab>
          <v-tab @click="SelectCategory('youtube')">유튜브</v-tab>
          <v-tab @click="SelectCategory('etc')">기타</v-tab>
          <v-tab @click="SelectCategory('opinion')">의견나눔</v-tab>
        </v-tabs>
      </v-col>
      <v-col cols="3"></v-col>
    </v-row>

    <!-- 내용 -->
    <v-row class="mr-tp">
      <v-col v-if="categoryType == 'intro'"><club-detail-intro /></v-col>
      <v-col v-if="categoryType == 'news'"><club-detail-news /></v-col>
      <v-col v-if="categoryType == 'youtube'"><club-detail-youtube /></v-col>
      <v-col v-if="categoryType == 'etc'"><club-detail-etc /></v-col>
      <v-col v-if="categoryType == 'opinion'"><club-detail-opinion /></v-col>
    </v-row>

    <!-- paging -->

    <!-- url -->
    <club-detail-url-create :type="'create'" />
  </div>
</template>

<script>
import ClubDetailIntro from './ClubDetailIntro';
import ClubDetailNews from './ClubDetailNews';
import ClubDetailYoutube from './ClubDetailYoutube';
import ClubDetailEtc from './ClubDetailEtc';
import ClubDetailOpinion from './ClubDetailOpinion';
import ClubDetailUrlCreate from './ClubDetailUrlCreate.vue';

export default {
  components: {
    ClubDetailIntro,
    ClubDetailNews,
    ClubDetailYoutube,
    ClubDetailEtc,
    ClubDetailOpinion,
    ClubDetailUrlCreate,
  },

  data() {
    return {
      categoryType: 'intro',
    };
  },
  methods: {
    SelectCategory: function(category) {
      this.categoryType = category;
    },
  },
  // {% comment %} created() {
  //   this.$store.dispatch('clubStore/clubDetailUrlList');
  // }, {% endcomment %}
};
</script>
