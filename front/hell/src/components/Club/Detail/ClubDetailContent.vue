<template>
  <div>
    <!-- 등록 -->
    <v-row>
      <v-col cols="auto" class="mr-auto"></v-col>
      <v-col cols="auto">
        <v-btn class="btnLC" color="blue" @click="OnOff">URL 등록</v-btn>
      </v-col>
    </v-row>

    <!-- 카테고리 if문 처리-->
    <v-row class="category">
      <v-tabs>
        <v-tab @click="SelectCategory('intro')">소개</v-tab>
        <v-tab @click="SelectCategory('news')">뉴스</v-tab>
        <v-tab @click="SelectCategory('youtube')">유튜브</v-tab>
        <v-tab @click="SelectCategory('etc')">기타</v-tab>
        <v-tab @click="SelectCategory('opinion')">의견나눔</v-tab>
      </v-tabs>
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
    OnOff: function() {
      this.$store.commit('CLUB_DETAIL_URL_DIALOG', true);
    },
  },
};
</script>
