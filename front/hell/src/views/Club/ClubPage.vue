<template>
  <v-container>
    <v-row class="justify-center">
      
      <img :src="require('../../assets/모여 이슈.png')" style="height:250; width:100%; position: relative;" alt="">
       <v-btn class="btnLC" style="position: absolute; top:450px; left:500px" color="blue" x-large rounded @click="OnOff">
      <span style="color: white;" class="mr-tp mr-bt"> 클럽 생성 </span></v-btn>


      <v-row class="mr-tp"></v-row>
      <!-- <v-row>
      <v-col cols="2"></v-col>
      <v-col> -->
      <div class="ma-auto mt-10" style="width: 80%">
        <!-- 카테고리 -->
        <club-category />

        <!-- card -->
        <v-row class="mr-tp">
          <v-col
            v-for="(clubInfo, n) in clubsPaging"
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
          <v-pagination v-model="page" :length="clubsPaginCnt" circle></v-pagination>
        </div>
        <!-- </v-col> -->
        <v-col cols="2"></v-col>
        <!-- </v-row> -->
        <club-create :type="'create'" />
      </div>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import ClubCard from '../../components/Club/ClubCard.vue';
import ClubCreate from '../../components/Club/ClubCreate.vue';
import ClubCategory from '../../components/Club/ClubCategory.vue';

export default {
  components: { ClubCard, ClubCreate, ClubCategory },
  computed: {
    ...mapState('clubStore', ['clubsPaging', 'clubsPaginCnt']),
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
  watch: {
    page: function(newVal) {
      this.$store.commit('clubStore/SET_CLUBS_PAGING', (newVal - 1) * 10);
    },
  },
  created() {
    this.clubList();
  },
  methods: {
    ...mapActions('clubStore', ['clubList']),
    OnOff() {
      console.log('클럽생성');
      this.$store.commit('clubStore/CLUB_CREATE_DIALOG', true);
    },
  },
};
</script>
