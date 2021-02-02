<template>
  <v-container>
    <v-row class="mr-tp"></v-row>
    <h2 class="text-center font-weight-bold display-1 mr-tp">클럽</h2>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col>
        <!-- 카테고리 -->
        <v-row class="mr-tp text-center">
          <v-tabs background-color="light-blue accent-4" center-active dark>
            <v-tab>전체</v-tab>
            <v-tab>정치</v-tab>
            <v-tab>경제</v-tab>
            <v-tab>IT/과학</v-tab>
            <v-tab>스포츠</v-tab>
            <v-tab>연예</v-tab>
            <v-tab>유머</v-tab>
            <v-tab>여행</v-tab>
            <v-tab>건강</v-tab>
            <v-tab>쇼핑</v-tab>
            <v-tab>교육</v-tab>
            <v-tab>게임</v-tab>
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
            <v-btn class="btnLC" color="blue" @click="OnOff">클럽 생성</v-btn>
          </v-col>
        </v-row>

        <!-- paging -->
        <div class="text-center mr-tp">
          <v-pagination v-model="page" :length="pageCnt" circle></v-pagination>
        </div>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <club-create />
  </v-container>
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
      this.$store.commit('CLUB_CREATE_DIALOG', true);
    },
  },
};
</script>
