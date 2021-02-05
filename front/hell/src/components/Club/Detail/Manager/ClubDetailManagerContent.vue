<template>
  <div>
    <!-- 등록 -->
    <v-row>
      <v-col cols="auto" class="mr-auto"></v-col>
      <v-col cols="auto">
        <v-btn class="btnLC" color="blue" @click="OnOff">정보 수정</v-btn>
      </v-col>
    </v-row>

    <!-- 카테고리 if문 처리-->
    <v-row class="category">
      <v-tabs>
        <v-tab @click="SelectCategory('member')">멤버관리</v-tab>
        <v-tab @click="SelectCategory('board')">게시물 관리</v-tab>
        <v-tab @click="SelectCategory('join')">가입요청</v-tab>
      </v-tabs>
    </v-row>

    <!-- 내용 -->
    <!-- <v-row class="mr-tp">
      <v-col v-if="categoryType == 'member'"><club-detail-intro /></v-col>
      <v-col v-if="categoryType == 'board'"><club-detail-news /></v-col>
      <v-col v-if="categoryType == 'join'"><club-detail-youtube /></v-col>
    </v-row> -->

    <!-- paging -->

    <!-- 수정 -->
    <club-create :type="'update'" />
  </div>
</template>

<script>
// import ClubDetailIntro from './ClubDetailIntro';
// import ClubDetailNews from './ClubDetailNews';
// import ClubDetailYoutube from './ClubDetailYoutube';
// import ClubDetailEtc from './ClubDetailEtc';
// import ClubDetailOpinion from './ClubDetailOpinion';
import ClubCreate from '../../ClubCreate.vue';

export default {
  components: {
    // ClubDetailIntro,
    // ClubDetailNews,
    // ClubDetailYoutube,
    // ClubDetailEtc,
    // ClubDetailOpinion,
    ClubCreate,
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
      this.$store.commit('clubStore/CLUB_CREATE_DIALOG', true);
    },
  },
  created() {
    //멤버 정보와 게시물 정보 가입 정보
  },
};
</script>
