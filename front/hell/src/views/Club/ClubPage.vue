<template>
    <v-row class="justify-center">
      <div class="club-image">
        <div style="height:450px"></div>
        <div style="width:65%; float:right">
       <v-btn class="btnLC"  color="blue" x-large rounded @click="OnOff">
      <span style="color: white;" class="mr-tp mr-bt"> 클럽 생성 </span></v-btn>
      </div>
      </div>
<div style="clear:both;"></div>

    <v-row class="mr-tp"></v-row>
    <!-- <v-row>
      <v-col cols="2"></v-col>
      <v-col> -->
      <div class="ma-auto mt-10" style="width: 80%">
        <!-- 카테고리 -->
        <v-row class="mr-tp text-center">
          <v-tabs color="deep-purple accent-3" center-active>
            <v-tab outlined>전체</v-tab>
            <v-tab outlined>정치</v-tab>
            <v-tab outlined>경제</v-tab>
            <v-tab outlined>IT/과학</v-tab>
            <v-tab outlined>스포츠</v-tab>
            <v-tab outlined>연예</v-tab>
            <v-tab outlined>생활</v-tab>
            <v-tab outlined>사회</v-tab>
            <v-tab outlined>해외</v-tab>
          </v-tabs>
        </v-row>

    </div>
        <!-- card -->
        <v-row class="mr-tp">
          <v-col
            v-for="(clubInfo, n) in clubs"
            :key="n"
            :clubInfo="clubInfo"
            class="d-flex child-flex"
          >
            <v-row align="center" justify="center">
              <club-card :clubInfo="clubInfo" />
            </v-row>
          </v-col>
        </v-row>



        <!-- paging -->
        <div class="text-center mr-tp">
          <v-pagination v-model="page" :length="pageCnt" circle></v-pagination>
        </div>
      <!-- </v-col> -->
      <v-col cols="2"></v-col>
    <!-- </v-row> -->
    <club-create :type="'create'" />
    </v-row>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import ClubCard from '../../components/Club/ClubCard.vue';
import ClubCreate from '../../components/Club/ClubCreate.vue';

export default {
  components: { ClubCard, ClubCreate },
  computed: {
    ...mapState('clubStore', ['clubs']),
  },
  data: function() {
    return {
      page: 1,
      pageCnt: 3,
      clubData: [
        {
          id: '',
          title: '',
          category: '',
          content: '',
          master: '',
          created_at: '',
        },
      ],
    };
  },
  created() {
    this.clubList();
  },
  methods: {
    ...mapActions('clubStore', ['clubList']),
    OnOff() {
      console.log('하이');
      this.$store.commit('clubStore/CLUB_CREATE_DIALOG', true);
    },
  },
};
</script>

<style>
.club-image{
  width:100%;
  height: 600px;
  background-image: url("../../assets/모여 이슈.png");
  background-size: 100% 600px;
}
</style>