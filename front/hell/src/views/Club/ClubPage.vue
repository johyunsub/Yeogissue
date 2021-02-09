<template>
  <!-- <v-container> -->
    <div>
      <v-banner class="pl-16" style="text-align : center" width='1200'>
    <h2 class="text-left font-weight-bold display-1 mr-tp">클럽</h2>
      <h5 class="text-left font-weight-bold display-1 mr-tp">클럽 소개글</h5>
      </v-banner>
        <v-sheet
      color="grey darken-2"
      height="500"
      width="100%"
    ></v-sheet>
    <v-row class="mr-tp"></v-row>
    <v-row>
      <v-col cols="2"></v-col>

      <v-col>
        <!-- 카테고리 -->
        <v-row class="mr-tp text-center">
          <v-tabs color="deep-purple accent-3" center-active>
            <v-tab outlined>전체</v-tab>
            <v-tab outlined>정치</v-tab>
            <v-tab outlined>경제</v-tab>
            <v-tab outlined>IT/과학</v-tab>
            <v-tab outlined>스포츠</v-tab>
            <v-tab outlined>연예</v-tab>
            <v-tab outlined>유머</v-tab>
            <v-tab outlined>여행</v-tab>
            <v-tab outlined>건강</v-tab>
            <v-tab outlined>쇼핑</v-tab>
            <v-tab outlined>교육</v-tab>
            <v-tab outlined>게임</v-tab>
          </v-tabs>
        </v-row>

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

        <v-row>
          <v-col cols="auto" class="mr-auto"></v-col>
          <v-col cols="auto">
            <v-btn class="btnLC" color="blue" rounded @click="OnOff">
              <span style="color: white;"> 클럽 생성 </span></v-btn>
          </v-col>
        </v-row>

        <!-- paging -->
        <div class="text-center mr-tp">
          <v-pagination v-model="page" :length="pageCnt" circle></v-pagination>
        </div>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <club-create :type="'create'" />
    </div>
  <!-- </v-container> -->
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
