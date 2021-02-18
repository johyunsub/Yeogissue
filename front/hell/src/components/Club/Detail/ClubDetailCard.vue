<template>
  <v-row class="justify-center">
    <v-sheet height="200" width="100%" color="#F1D883">
      <v-card-title class="justify-center mt-7">
        <h1 class="font-weight-bold display-3 basil--text mb-3"  style="color:#1565C0">
          {{ clubData.title }}
        </h1>
      </v-card-title>

      <v-row class="mx-auto mb-6">
        <v-col cols="5"></v-col>
        <v-col cols="4">
          <div class="mx-4">
            <v-img
              :src="image"
              max-height="370"
              aspect-ratio="1.5"
              contain
              alt="이미지 넣어줘"
              class="club-pr"
            />
          </div>
        </v-col>
        <v-col cols="auto">
          <span class="ml-10">
            <span>
              <v-btn v-if="!clubDetailManegerBtn" text color="blue darken-1" @click="isClubJoin">
                <v-icon midium class="fas fa-plus mr-1" ></v-icon><span style="color: blue;">URL 등록 </span>
              </v-btn>
              <!-- 수정 -->
              <v-btn v-if="clubDetailManegerBtn" text color="blue darken-1" @click="OnOffCreate">
                <v-icon class="mr-1">fas fa-wrench</v-icon>
                <span style="color: blue;">클럽수정 </span> 
              </v-btn>
            </span>
            <span v-if="clubDetailManegerBtn === false">
              <v-btn
                v-if="clubData.master == userInfo.id"
                color="blue darken-1"
                text
                @click="managerOnOff(true)"
              >
                <v-icon color="blue">fas fa-user-cog</v-icon>
                <span style="color: blue;">관리 </span>
              </v-btn>
            </span>
            <v-btn
              v-if="clubData.master != userInfo.id && clubDetailIsMember"
              color="blue darken-1"
              text
              @click="doLeave()"
              >
              <v-icon class="fas fa-door-open"></v-icon>
              <span style="color: blue;">클럽탈퇴</span>
            </v-btn>
            <v-btn
              v-if="clubData.master != userInfo.id && !clubDetailIsMember && clubDetailIsWaiting"
              color="blue darken-1"
              text
              >
              <v-icon class="far fa-pause-circle"></v-icon>
              <span style="color: blue;">가입대기중</span></v-btn
            >
            <v-btn color="blue darken-1" text v-if="isLoginToken == ''" @click="isLogin">
              <v-icon color="blue">fas fa-user-friends</v-icon>
              <span style="color: blue;">가입하기</span>
            </v-btn>
            <v-dialog
              v-if="clubData.master != userInfo.id && !clubDetailIsMember && !clubDetailIsWaiting && isLoginToken != ''"
              transition="dialog-bottom-transition"
              max-width="600"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="blue darken-1" text v-bind="attrs" v-on="on">
                  <v-icon color="blue">fas fa-user-friends</v-icon>
                  <span style="color: blue;">가입하기</span>
                </v-btn>

              </template>
              <template v-slot:default="dialog">
                <v-card>
                  <v-toolbar color="primary" dark> {{ clubData.title }}클럽 가입신청서</v-toolbar>
                  <v-card-text>
                    <div class="text-h6 font-weight-black pa-12">
                      반가워요 {{ userInfo.nickname }}님.
                    </div>
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
                      v-model="content"
                    ></v-textarea>
                  </v-sheet>
                  <v-card-actions class="justify-end">
                    <v-div @click="dialog.value = false">
                      <v-btn text @click="goJoin">제출</v-btn>
                    </v-div>
                    <v-btn text @click="dialog.value = false">닫기</v-btn>
                  </v-card-actions>
                </v-card>
              </template>
            </v-dialog>
            <span v-if="clubDetailManegerBtn === true && clubData.master == userInfo.id">
              <v-btn color="blue darken-1" text @click="managerOnOff(false)">
                <v-icon midium class="fas fa-home mr-1" color="blue"></v-icon>
                <span style="color: blue;">홈으로</span>
              </v-btn>
            </span>
          </span>
        </v-col>
      </v-row>
    </v-sheet>
    <club-create :type="'update'" />

    <div class="text-center" v-if="clubData.is_private">
    <v-bottom-sheet
      v-model="sheet"
      inset
    >
      <v-sheet
        class="text-center"
        height="200px"
      >
        <v-btn
          class="mt-6"
          text
          color="error"
          @click="sheet = !sheet"
        >
          close
        </v-btn>
        <div class="my-3">
          비공개 클럽입니다. 게시물 열람은 가입 후 가능합니다.
        </div>
      </v-sheet>
    </v-bottom-sheet>
  </div>
  </v-row>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import ClubCreate from '../ClubCreate.vue';
import { API_BASE_URL } from "../../../config";
import axios from "axios";

export default {
  components: { ClubCreate },
  computed: {
    ...mapState('clubStore', [
      'clubData',
      'clubDetailManegerBtn',
      'clubDetailIsMember',
      'clubDetailIsWaiting',
      'clubManageMemberList',
    ]),
    ...mapState(['userInfo', 'isLoginToken']),
  },
  data() {
    return {
      content: '',
      image:'',
      sheet: true,
    };
  },
  props: {
    clubInfo: { type: Object },
  },
  methods: {
    ...mapActions('clubStore', ['clubJoin', 'clubLeave', 'isClubMember']),
    managerOnOff(check) {
      this.$store.commit('clubStore/SET_CLUB_MANAGER_BTN', check);
    },
    goJoin() {
      this.clubJoin({ user: this.userInfo.id, comment: this.content });
      this.$fire({
        title: '가입신청 완료',
        text: '클럽장의 승인이 있을때까지 기다려주세요',
        type: 'success',
      });
    },
    doLeave() {
      this.clubLeave({ user: this.userInfo.id });
      this.$fire({
        title: '가입탈퇴 완료',
        text: '클럽 탈퇴되었습니다',
        type: 'success',
      });
    },
    isClubJoin() {
      if (this.clubDetailIsMember || this.userInfo.id == this.clubData.master) {
        this.OnOff();
      } else {
        this.$fire({
          title: '이용하시려면 클럽가입 먼저 해주세요',
          type: 'error',
        });
      }
    },
    OnOff: function() {
      this.$store.commit('clubStore/CLUB_DETAIL_URL_DIALOG', true);
    },
    OnOffCreate: function() {
      this.$store.commit('clubStore/CLUB_CREATE_DIALOG', true);
    },
    setImage: function() {
      console.log(this.$route.query.id)
      console.log(this.clubData.image)
      axios.get(`${API_BASE_URL}club/club_detail/${this.$route.query.id}/`)
            .then((res)=>{
              
              if (res.data.image) 
              { this.image = API_BASE_URL + this.clubData.image.substr(1); console.log(this.image,'image') }
              else if (res.data.category == "IT/과학") {this.image = `${API_BASE_URL}media/images/%EA%B3%BC%ED%95%99.JPG` }
              else if (res.data.category == "경제") {this.image = `${API_BASE_URL}media/images/%EA%B2%BD%EC%A0%9C.JPG`}
              else if (res.data.category == "사회") {this.image = `${API_BASE_URL}media/images/%EC%82%AC%ED%9A%8C.JPG`}
              else if (res.data.category == "생활") {this.image = `${API_BASE_URL}media/images/%EC%8A%A4%ED%8F%AC%EC%B8%A0.JPG`}
              else if (res.data.category == "스포츠") {this.image = `${API_BASE_URL}media/images/%EC%8A%A4%ED%8F%AC%EC%B8%A0.JPG`}
              else if (res.data.category == "연예") {this.image = `${API_BASE_URL}media/images/%EC%97%B0%EC%98%88.JPG`}
              else if (res.data.category == "정치") {this.image = `${API_BASE_URL}media/images/%EC%A0%95%EC%B9%98.JPG`}
              else if (res.data.category == "해외") {this.image = `${API_BASE_URL}media/images/%ED%95%B4%EC%99%B8.JPG`}
            })
    //   this.image = 'http://i4d108.p.ssafy.io:8000' + this.userInfo.image;
    },
    isLogin(){
      console.log("여기여기")
      if (this.isLoginToken == '') {
        this.$store.commit('CHANGE_DIALOG', true);
      }
    }
  },
  created(){
    this.setImage();

    // this.isClubMember( {user: this.userInfo.id})
  },
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
