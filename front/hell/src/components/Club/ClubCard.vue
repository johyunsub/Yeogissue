<template>
  <v-hover v-slot="{ hover }" open-delay="200" >
    <v-card
      class="mx-auto my-5 elevation-5 choice_cursor { 'on-hover': hover }"
      max-width="600"
      :elevation="hover ? 16 : 2"
      
    >
      <div @click="MovePage('detail')" >

      <v-img height="150" src="https://cdn.vuetifyjs.com/images/cards/cooking.png">
          <v-expand-transition>
          <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-3 white--text"
            style="height: 100%;"
          >
            소개글 여기 적을까? 투명하게 해서
          </div>
        </v-expand-transition>
      
      </v-img>

      <!-- 글짜 ... 해주는거 text-truncate -->
      <v-card-title  class="headline mb-0 h6">{{ clubInfo.title }}
      </v-card-title>

        <v-card-text>
          <v-row align="center" class="mx-0"> </v-row>

          <div class="my-2 subtitle-4 text-truncate">
            카테고리: {{ clubInfo.category }} 
          </div>

        </v-card-text>

        <v-divider class="mx-4"></v-divider>

        <v-card-text>
          <v-chip>모집중 | 게시글 n 개 넘으면 활발/보통/저조 표시</v-chip>
        </v-card-text>
      </div>

      <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
        @click="show = !show"
      >
        소개글 보기
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          <div class="body-1 text-truncate">{{ clubInfo.content }}</div>
        </v-card-text>
      </div>
    </v-expand-transition>

    </v-card>
  </v-hover>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'clubCard',
  computed: {
    ...mapState('clubStore', ['clubManageMemberList']),
    ...mapState(['userInfo']),
  },
  data() {
    return {
      show: false,
    };
    
  },
  props: {
    clubInfo: Object,
  },
  created() {},
  methods: {
    MovePage: function(check) {
      switch (check) {
        case 'detail':
          this.isLogin();
          break;
      }
    },
    isLogin(){
      if(this.userInfo != null){
        this.$router.push(`/clubDetail?id=${this.clubInfo.id}`);
      }
      else{
        this.$fire({
        title: "로그인후 이용하실 수 있습니다.",
        type: "error" ,
        }); 
      }
    }
  },
};
</script>

<style lang="sass"></style>
