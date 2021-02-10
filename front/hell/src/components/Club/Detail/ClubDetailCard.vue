<template>
  <v-row class="justify-center">
    <v-sheet height="500" width="100%" color="lime lighten-4">
      <v-row class="mt-1">
         <v-col
          ><v-img
            src="../../../assets/logo.png"
            max-height="370"
            aspect-ratio="1.5"
            contain
            alt="이미지 넣어줘"
          />
        </v-col>
        <v-col>
          <div>
            <v-row class="mt-1 mr-auto mb-2">
              <v-col cols="2" class="mr-auto" md="10">
                <!-- <v-sheet width="90%"> -->
                  <!-- 클럽정보 (맴버수, 카테고리, 개설일, 마스터) -->
                  <div class="headline">{{ clubData.title }}</div>
                  <div class="mt-3">카테고리 - {{ clubData.category }}</div>
                  <div class="mt-3">멤버수 - {{ clubData.member_cnt }}</div>
                  <div class="mt-3">매니저 - {{ clubData.mastername }}</div>
                  <div class="mt-3">개설일 - {{ clubData.created_at }}</div>
                <!-- </v-sheet> -->
              </v-col>
             
              <v-col cols="auto"></v-col>
            </v-row>
          </div>
          <v-row class="mt-4 my-1 mr-l">
            <v-col cols="auto" class="mr-auto"></v-col>
            <div>
              <v-col cols="auto">
                <div class="mr-3" v-if="clubDetailManegerBtn === false">
                  <v-btn color="blue darken-1" text @click="managerOnOff(true)"> <v-icon color="blue">fas fa-user-cog</v-icon>
                    <span style="color: blue;">관리 </span></v-btn>
                  <v-btn color="blue darken-1" text @click="OnOff()"> <v-icon color="blue">fas fa-user-friends</v-icon>
                    <span style="color: blue;">가입하기</span>
                    </v-btn>
                </div>
                <div class="mr-3" v-if="clubDetailManegerBtn === true">
                  <v-btn color="blue darken-1" text @click="managerOnOff(false)">홈으로</v-btn>
                </div>
              </v-col>
            </div>
          </v-row>
        </v-col>
      </v-row>
    </v-sheet>
  </v-row>
</template>

<script>
import { mapState } from 'vuex';
export default {
  computed: {
    ...mapState('clubStore', ['clubData', 'clubDetailManegerBtn']),
  },
  methods: {
    managerOnOff(check) {
      this.$store.commit('clubStore/SET_CLUB_MANAGER_BTN', check);
    },
  },
};
</script>
