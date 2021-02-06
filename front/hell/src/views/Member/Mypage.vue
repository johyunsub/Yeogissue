<template>
    <v-container>
        <v-row class="py-5">
            <h1>My 이슈</h1>
            <h1>안녕하세요, {{nickname}} 님</h1>
        </v-row>
        <v-row class="py-5">
            <v-col cols="3">
                <v-row class="py-4" justify="center">
                    <v-avatar
                        class="profile"
                        color="grey"
                        size="164"
                        rounded
                    >
                        <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
                    </v-avatar>
                </v-row>
                <v-row justify="center" class="py-4">
                    <v-expansion-panels accordion>
                    <v-expansion-panel>
                        <v-expansion-panel-header>내 보관함</v-expansion-panel-header>
                        <v-expansion-panel-content>
                        <v-list dense>
                            <v-list-item-group>
                                <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title @click="OnOff('scrap')">내가 스크랩한 의견 목록</v-list-item-title>
                                </v-list-item-content>
                                </v-list-item>
                                <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title @click="OnOff('write')">내가 작성한 의견</v-list-item-title>
                                </v-list-item-content>
                                </v-list-item>
                                <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title @click="OnOff('club')">내가 가입한 클럽</v-list-item-title>
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
                                <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title @click="OnOff('feeling')">내가 쓴 글 감정분석</v-list-item-title>
                                </v-list-item-content>
                                </v-list-item>
                                <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title @click="OnOff('recently')">최근에 본 게시물</v-list-item-title>
                                </v-list-item-content>
                                </v-list-item>
                                <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title @click="OnOff('graph')">자주 보는 카테고리 그래프</v-list-item-title>
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
                                <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title @click="OnOff('update')">회원정보 수정</v-list-item-title>
                                </v-list-item-content>
                                </v-list-item>
                            </v-list-item-group>
                            </v-list>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                    </v-expansion-panels>
                </v-row>


            </v-col>
            <v-col cols="9">
                <my-club v-if="club" />
                <my-feeling v-if="feeling" />
                <my-graph v-if="graph" />
                <my-recently v-if="recently" />
                <my-scrap v-if="scrap" />
                <my-update v-if="update" />
                <my-write v-if="write" />
            </v-col>
            
        </v-row>
    </v-container>    
</template>

<script>
import MyClub from '../../components/Mypage/MyClub.vue';
import MyFeeling from '../../components/Mypage/MyFeeling.vue';
import MyGraph from '../../components/Mypage/MyGraph.vue';
import MyRecently from '../../components/Mypage/MyRecently.vue';
import MyScrap from '../../components/Mypage/MyScrap.vue';
import MyUpdate from '../../components/Mypage/MyUpdate.vue';
import MyWrite from '../../components/Mypage/MyWrite.vue';


export default {
  components: { MyClub, MyFeeling, MyGraph, MyRecently, MyScrap, MyUpdate, MyWrite },
  data: function() {
      return {
          club: false,
          feeling: false,
          graph: false,
          recently: false,
          scrap: false,
          update: false,
          write: false,
          nickname: '',
      }
  },
  methods: {
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
          break;
        case 'feeling':
          this.club = false;
          this.feeling = true;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = false;
          break;
        case 'graph':
          this.club = false;
          this.feeling = false;
          this.graph = true;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = false;
          break;
        case 'recently':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = true;
          this.scrap = false;
          this.write = false;
          this.update = false;
          break;
        case 'scrap':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = true;
          this.write = false;
          this.update = false;
          break;
        case 'write':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = true;
          this.update = false;
          break;
        case 'update':
          this.club = false;
          this.feeling = false;
          this.graph = false;
          this.recently = false;
          this.scrap = false;
          this.write = false;
          this.update = true;
          break;

      }
    },
  }
}
</script>