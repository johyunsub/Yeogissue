<template>
  <v-row class="mr-tp justify-center">
    <v-sheet height="auto" width="100%" color="lime lighten-4">
      <v-row class="mt-1">
         <v-col
          ><v-img
            src="../../../assets/logo.png"
            max-height="270"
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
                  <div class="mt-3">멤버수 - {{clubManageMemberList.length}}</div>
                  <div class="mt-3">매니저 - {{ clubData.master }}</div>
                  <div class="mt-3">개설일 - {{ clubData.created_at }}</div>
                <!-- </v-sheet> -->
              </v-col>
             
              <v-col cols="auto"></v-col>
            </v-row>
          </div>
          <v-row class="mt-4 my-1 mr-l">
            <v-col cols="auto" class="mr-auto"></v-col>
            <div>
              <v-col cols="auto" >
                <div class="mr-3" v-if="clubDetailManegerBtn === false">
                  <v-btn v-if="clubData.master == userInfo.id" color="blue darken-1" text @click="managerOnOff(true)">관리</v-btn>
                </div>
                <v-btn v-if="clubData.master != userInfo.id && clubDetailIsMember" color="blue darken-1" text @click="doLeave()">클럽탈퇴</v-btn>
                <v-btn v-if="clubData.master != userInfo.id && !clubDetailIsMember &&  clubDetailIsWaiting" color="blue darken-1" text>가입대기중</v-btn>
                <v-dialog  
                  v-if="clubData.master != userInfo.id && !clubDetailIsMember && !clubDetailIsWaiting && clubData.is_private"
                  transition="dialog-bottom-transition"
                  max-width="600"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="blue darken-1"
                      text
                      v-bind="attrs"
                      v-on="on"
                    >가입하기</v-btn>
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
                        <v-div @click="dialog.value = false">
                        <v-btn
                          text
                          @click="goJoin"
                        >제출</v-btn>
                        </v-div>
                        <v-btn
                          text
                          @click="dialog.value = false"
                        >닫기</v-btn>
                      </v-card-actions>
                    </v-card>
                  </template>
                </v-dialog>
                <div class="mr-3" v-if="clubDetailManegerBtn === true && clubData.master == userInfo.id">
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
    }
  },
  created(){
    this.isClubMember( {user: this.userInfo.id})
  }
};
</script>
