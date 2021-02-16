<template>
<div>
    <p class="text-h4 font-weight-black ml-7">
      내가 가입한 클럽 리스트
      <i class="fas fa-network-wired"></i>
    </p>
    <hr class="ml-7" width="98%" color="purple" />
    
    <v-row class="justify-center">
      
    <!-- <div style="clear:both;"></div> -->

    <v-row class="mr-tp"></v-row>
      <!-- <v-row>
      <v-col cols="2"></v-col>
      <v-col> -->
      <div class="ma-auto mt-10" style="width: 80%">
        <!-- 카테고리 -->
        

        <!-- card -->
        <v-row class="mr-tp">
          <v-col
            v-for="(clubInfo, n) in myclubData"
            :key="n"
            :clubInfo="clubInfo"
            class="d-flex child-flex"
          >
            <v-row align="center" justify="center">
              <club-card :clubInfo="clubInfo" />
            </v-row>
          </v-col>
        </v-row>

        
        <!-- </v-col> -->
        <v-col cols="2"></v-col>
        <!-- </v-row> -->
      </div>
    </v-row>
 
  </div>
</template>

<script>
import { mapState } from 'vuex';
import ClubCard from '../../components/Club/ClubCard.vue';
import axios from 'axios';
import { API_BASE_URL } from '../../config';

export default {
  components: { ClubCard },
  computed: {
    ...mapState('clubStore', ['clubsPaging', 'clubsPaginCnt']),
    ...mapState(['userInfo']),
  },
  data: function() {
    return {
      page: 1,
      pageCnt: 3,
      myclubData: [
        {
          id: '',
          title: '',
          category: '',
          content: '',
          master: '',
          created_at: '',
          is_private: '',
          member_cnt: '',
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
    this.myclubList();
  },
  methods: {
   
    myclubList(){
       axios
        .post(`${API_BASE_URL}club/myclub/`, { user : this.userInfo.id })
        .then((res) => {
          this.myclubData = res.data;
        })
        .catch((err) => console.log(err.response));
    }
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