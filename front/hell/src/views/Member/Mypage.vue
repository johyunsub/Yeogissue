<template>
  <v-container>
    <v-sheet height="80"></v-sheet>
    <div class="ml-10">
      <v-row class="py-5">
        <v-col sm="3">
          <h1>My 이슈</h1>
          <h2>
            안녕하세요, <a text @click="ProfileOn('profile')" >{{ userInfo.nickname }}</a>님
          </h2>

          <v-row class="py-4" justify="center">
            <v-avatar class="profile mt-5" color="grey" size="164" rounded>
              <v-img :src="image"></v-img>
            </v-avatar>
          </v-row>
          <v-row justify="center" class="py-4">
            <v-expansion-panels accordion>
              <v-expansion-panel>
                <v-expansion-panel-header>내 보관함</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list dense>
                    <v-list-item-group>
                      <v-list-item @click="OnOff('scrap')">
                        <v-list-item-content>
                          <v-list-item-title>나의 스크랩 보관함</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <v-list-item @click="OnOff('write')">
                        <v-list-item-content>
                          <v-list-item-title>내가 작성한 의견</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <v-list-item @click="OnOff('club')">
                        <v-list-item-content>
                          <v-list-item-title @click="OnOff('club')"
                            >내가 가입한 클럽</v-list-item-title
                          >
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header>내 활동 통계</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list dense>
                    <v-list-item-group>
                      <v-list-item @click="OnOff('feeling')">
                        <v-list-item-content>
                          <v-list-item-title>내가 쓴 글 감정분석</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header>회원정보</v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-list dense>
                    <v-list-item-group>
                      <v-list-item @click="OnOff('update')">
                        <v-list-item-content>
                          <v-list-item-title>회원정보 수정</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                  <v-list dense>
                    <v-list-item-group>
                      <v-list-item @click="OnOff('changepw')">
                        <v-list-item-content>
                          <v-list-item-title>비밀번호 변경</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-row>
        </v-col>
        <v-col>
          <my-club v-if="club" />
          <my-feeling v-if="feeling" />
          <my-graph v-if="graph" />
          <my-recently v-if="recently" />
          <my-scrap v-if="scrap" />
          <my-update v-if="update" :image="image" />
          <my-write v-if="write" />
          <my-changepw v-if="changepw" />
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import MyClub from '../../components/Mypage/MyClub.vue';
import MyFeeling from '../../components/Mypage/MyFeeling.vue';
import MyScrap from '../../components/Mypage/MyScrap.vue';
import MyUpdate from '../../components/Mypage/MyUpdate.vue';
import MyWrite from '../../components/Mypage/MyWrite.vue';
import MyChangepw from '../../components/Mypage/MyChangepw.vue';

import { mapState, mapActions } from 'vuex';
import { API_BASE_URL } from "../../config";


export default {
  components: { MyClub, MyFeeling, MyScrap, MyUpdate, MyWrite, MyChangepw },
  computed: {
    ...mapState(['userInfo','profileData']),
  },
  data: function() {
    return {
      club: false,
      feeling: false,
      graph: false,
      recently: false,
      scrap: true,
      update: false,
      write: false,
      changepw: false,

      nickname: '',
      image: '',
    };
  },
  methods: {
    ...mapActions(['getProfile']),

    setImage: function() {
      this.image = API_BASE_URL + this.userInfo.image.substr(1);
    //   this.image =  + this.userInfo.image;
      
    },
    ProfileOn: function(message) {
      switch (message) {
        case 'profile':
          this.getProfile(this.userInfo.id);
          this.$store.commit('CHANGE_PROFILE', true);
          break;
      }
    },
    OnOff: function(message) {
      switch (message) {
        case 'club':
          this.club = true;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = false;
          this.changepw = false;

          break;
        case 'feeling':
          this.club = false;
          this.feeling = true;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = false;
          this.changepw = false;

          break;
        case 'graph':
          this.club = false;
          this.feeling = false;
          this.graph = true;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = false;
          this.changepw = false;

          break;
        case 'recently':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = true;
          this.scrap = false;
          this.write = false;
          this.update = false;
          this.changepw = false;

          break;
        case 'scrap':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = true;
          this.write = false;
          this.update = false;
          this.changepw = false;

          break;
        case 'write':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = true;
          this.update = false;
          this.changepw = false;

          break;
        case 'update':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = true;
          this.changepw = false;
          break;
        case 'changepw':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = false;
          this.changepw = true;
          break;
      }
    },
  },
  created() {
    window.scrollTo(0,0);
    this.$store.dispatch('userData', localStorage.getItem('email'));
    this.setImage();
    this.$store.dispatch('getEmotion');
  },
};
</script>
