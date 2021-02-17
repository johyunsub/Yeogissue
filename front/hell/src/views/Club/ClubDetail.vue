<template>
  <div>
    <!-- <v-container> -->
    <!-- <h2 class="text-center mr-tp mr-bt display-1">Club</h2> -->
    <v-row>
      <v-col id="">
        <!-- 클럽 정보 -->
        <club-detail-card class="mb-10" />

        <!-- <v-divider class="my-10"></v-divider> -->

        <!-- 관리자창x && 관리자o => 클럽게시판 보이게 -->
        <club-detail-content v-if="!clubDetailManegerBtn && clubData.master == userInfo.id" />
        <!-- 클럽멤버o && 관리자x  => 클럽게시판 보이게 -->
        <club-detail-content
          v-if="clubDetailIsMember && clubData.master != userInfo.id && clubData.is_private"
        />
        <!-- 클럽멤버x && 공개게시판  => 클럽게시판 보이게 -->
        <club-detail-content v-if="!clubDetailIsMember && !clubData.is_private" />
        <!-- 클럽멤버o && 공개게시판  => 클럽게시판 보이게 -->
        <club-detail-content v-if="clubDetailIsMember && clubData.master != userInfo.id && !clubData.is_private" />
        <!-- 관리자창o && 관리자o && 공개 게시판=> 관리자창 보이게 -->
        <club-detail-manager-content
          v-if="clubDetailManegerBtn && clubData.master == userInfo.id"
        />
        <!-- 클럽멤버o && 관리자x && 비공개게시판 => 클럽소개페이지 보이게-->
        <club-detail-Intro
          v-if="!clubDetailIsMember && clubData.master != userInfo.id && clubData.is_private"
        />

        <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
      </v-col>
    </v-row>
    <!-- </v-container> -->
  </div>
</template>

<script>
import ClubDetailContent from '../../components/Club/Detail/ClubDetailContent.vue';
import ClubDetailIntro from '../../components/Club/Detail/ClubDetailIntro.vue';
import ClubDetailManagerContent from '../../components/Club/Detail/Manager/ClubDetailManagerContent.vue';
import ClubDetailCard from '../../components/Club/Detail/ClubDetailCard.vue';

import { mapState, mapActions } from 'vuex';

export default {
  components: {
    ClubDetailContent,
    ClubDetailCard,
    ClubDetailManagerContent,
    ClubDetailIntro,
  },
  computed: {
    ...mapState('clubStore', ['clubData', 'clubDetailManegerBtn', 'clubDetailIsMember']),
    ...mapState(['userInfo']),
  },
  data: function() {
    return {
      count : 0,
    };
  },
  updated(){
    if(this.count ==0) this.isClubMember({ id: this.$route.query.id, user: this.userInfo.id });
    this.count++;
  },
  methods: {
    ...mapActions('clubStore', ['clubDetail', 'isClubMember']),
  },
  created() {
    console.log(this.$route.query.id);
    console.log(this.userInfo.id);
    window.scrollTo(0, 0);
    // this.clubDetail(this.$route.query.id);
    this.isClubMember({ id: this.$route.query.id, user: this.userInfo.id });
  },
};
</script>

<style lang="scss" scoped>
.category {
  margin-top: 40px;
}
</style>
