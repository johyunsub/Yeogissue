<template>
  <v-row class="justify-center">


    <v-sheet height="200" width="100%" color="#F1D883">
      
      <v-card-title class="justify-center mt-7">
        <h1 class="font-weight-bold display-3 basil--text mb-3">
          {{ clubData.title }}
        </h1>
      </v-card-title>

        <v-row class="mx-auto mb-6">
          <v-col cols="5"></v-col>
          <v-col cols="4">
            <div class="mx-4">
              <v-img
                src="../../../assets/logo.png"
                max-height="370"
                aspect-ratio="1.5"
                contain
                alt="이미지 넣어줘"
                class="club-pr"
              />
            </div>
          </v-col>
          <v-col cols="auto">
          <v-btn class="btnLC" text color="blue darken-1" @click="isClubJoin">
            <i class="fas fa-chevron-circle-up">
              </i>URL 등록</v-btn>
          </v-col>
          <v-col cols="auto" >
                <div v-if="clubDetailManegerBtn === false">
                  <v-btn v-if="clubData.master == userInfo.id" color="blue darken-1" text @click="managerOnOff(true)"> <v-icon color="blue">fas fa-user-cog</v-icon>
                    <span style="color: blue;">관리 </span>
                  </v-btn>
                </div>
                <v-btn v-if="clubData.master != userInfo.id && clubDetailIsMember" color="blue darken-1" text @click="doLeave()">클럽탈퇴</v-btn>
                <v-btn v-if="clubData.master != userInfo.id && !clubDetailIsMember &&  clubDetailIsWaiting" color="blue darken-1" text>가입대기중</v-btn>
                <v-dialog  
                  v-if="clubData.master != userInfo.id && !clubDetailIsMember && !clubDetailIsWaiting"
                  transition="dialog-bottom-transition"
                  max-width="600"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="blue darken-1"
                      text
                      v-bind="attrs"
                      v-on="on"
                    >
                    <v-icon color="blue">fas fa-user-friends</v-icon>
                    <span style="color: blue;">가입하기</span>
                    </v-btn>
                  </template>
                  <template v-slot:default="dialog">
                    <v-card>
                      <v-toolbar
                        color="primary"
                        dark
                      > {{ clubData.title }}클럽 가입신청서</v-toolbar>
                      <v-card-text>
                        <div class="text-h6 font-weight-black pa-12">반가워요 {{ userInfo.nickname }}님. </div>
                      </v-card-text>
                      <v-sheet class="mx-8">
                        <v-textarea 
                          class="px-3"
                          label="가입동기를 적어주세요"
                          auto-grow
                          outlined
                          rows="4"
                          row-height="30"
                          shaped
                          v-model='content'
                        ></v-textarea>
                      </v-sheet>
                      <v-card-actions class="justify-end">
                        <div @click="dialog.value = false">
                        <v-btn
                          text
                          @click="goJoin"
                        >제출</v-btn>
                        </div>
                        <v-btn
                          text
                          @click="dialog.value = false"
                        >닫기</v-btn>
                      </v-card-actions>
                    </v-card>
                  </template>
                </v-dialog>
                <div v-if="clubDetailManegerBtn === true && clubData.master == userInfo.id">
                  <v-btn color="blue darken-1" text @click="managerOnOff(false)">홈으로</v-btn>
                </div>
              </v-col>
        </v-row>
        
 
      
    </v-sheet>
  </v-row>
</template>

<script>
import { mapActions, mapState } from 'vuex';
export default {
  components: {
  },
  computed: {
    ...mapState('clubStore', ['clubData', 'clubDetailManegerBtn', 'clubDetailIsMember', 'clubDetailIsWaiting', 'clubManageMemberList']),
    ...mapState( ['userInfo' ]),
  },
  data() {
    return {
      content: '',
    }
    
  },
  props: {
    clubInfo: { type: Object},
  },
  methods: {
    ...mapActions('clubStore', ['clubJoin', 'clubLeave', 'isClubMember']),
    managerOnOff(check) {
      this.$store.commit('clubStore/SET_CLUB_MANAGER_BTN', check);
    },
    goJoin() {
      this.clubJoin({user: this.userInfo.id, comment: this.content})
      this.$fire({
        title: "가입신청 완료",
        text: "클럽장의 승인이 있을때까지 기다려주세요",
        type: "success" ,
      }); 
    },
    doLeave(){
        this.clubLeave({user: this.userInfo.id})
        this.$fire({
        title: "가입탈퇴 완료",
        text: "클럽 탈퇴되었습니다",
        type: "success" ,
        }); 
    },
    isClubJoin(){
      if(this.clubDetailIsMember || this.userInfo.id == this.clubData.master ){
        this.OnOff()
      }
      else{
        this.$fire({
        title: "이용하시려면 클럽가입 먼저 해주세요",
        type: "error" ,
        }); 
      }
    },
    OnOff: function() {
      this.$store.commit('clubStore/CLUB_DETAIL_URL_DIALOG', true);
    },
  },
  created(){
    // this.isClubMember( {user: this.userInfo.id})
  }
};
</script>

<style>
.club-pr {
    width: 150px;
    height: 150px; 
    border-radius: 70%;
    overflow: hidden;
}

</style>