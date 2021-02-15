//type에 따라 찬반, 의견으로 버튼이 보이고 안보이고 성질에 따라
<template>
  <div>
    <div v-if="isUpdate == false">
      <v-alert
        class="border-line"
        :border="getBorder(opinion_type)"
        colored-border
        :color="borderColor"
      >
        <v-row>
          <v-col>
            <div class="text--primary ">
                    <v-avatar class="profile ml-3 mr-2" color="grey" size="50">
            <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
          </v-avatar>
              <a text @click="ProfileOn('profile')">{{ username }}</a> | {{ updated_at.replace("T", " ").substr(0, 16) }}
            </div>
        

          </v-col>
          <v-col
            v-if="!getLike"
            cols="auto"
            class="choice_cursor"
            @click="thumbUp"
          >
            <v-icon small>mdi-thumb-up-outline</v-icon> {{ like_users_count }}
          </v-col>
          <v-col
            v-if="getLike"
            cols="auto"
            class="choice_cursor"
            @click="thumbUp"
          >
            <v-icon small>mdi-thumb-up</v-icon> {{ like_users_count }}
          </v-col>
          <v-col cols="auto">
            <comment-menu :id="id" v-on:CommentUp="changeUpdate(true)"
          /></v-col>
        </v-row>

        <v-row>
          <v-col cols="2">
            <div v-if="emotion == '기쁨'">
              <i class="far fa-grin-squint positive fa-2x" ></i>기쁨
            </div>

            <div v-else-if="emotion == '감정불가'">
              감정불가
            </div>

            <div v-else-if="emotion == '신뢰'">
              <i class="far fa-grin-stars positive fa-2x"></i>
              <br>
              신뢰
            </div>

            <div v-else-if="emotion == '놀라움'">
              <i class="far fa-surprise positive fa-2x">놀라움</i>
            </div>

            <div v-else-if="emotion == '슬픔'">
              <i class="far fa-sad-tear positive fa-2x">슬픔</i>
            </div>

            <div v-else-if="emotion == '공포'">
              <i class="far fa-grimace bad fa-2x">공포</i>
            </div>

            <div v-else-if="emotion == '기대'">
              <i class="far fa-kiss-beam positive fa-2x">기대</i>
            </div>

            <div v-else-if="emotion == '혐오'">
              <i class="far fa-dizzy bad fa-2x">혐오</i>
            </div>

            <div v-else>
              <i class="far fa-angry">분노</i>
            </div>

      
          </v-col>

          <v-col cols="9">
            <span class="ml-5">{{ content }}</span>
          </v-col>
        </v-row>
      </v-alert>
    </div>

    <div v-if="isUpdate == true">
      <comment-create
        :type="'update'"
        :propContent="content"
        :no="id"
        v-on:CommentDown="changeUpdate(false)"
      />
    </div>
  </div>
</template>

<script>
import CommentCreate from "../../components/Opinion/CommentCreate.vue";
import CommentMenu from "./CommentMenu.vue";

import { mapState,mapActions } from "vuex";
import axios from "axios";
import { API_BASE_URL } from "../../config";

export default {
  components: { CommentMenu, CommentCreate },
  computed: {
    ...mapState("opinionStore", ["opinionComment"]),
    ...mapState(["isLoginToken", "userInfo"]),
    
    getLike: {
      get: function() {
        if (this.like_users.includes(this.$store.state.userInfo.id)) {
          return true;
        }
        return false;
      },
    },
  },
  props: {
    id: { type: Number },
    opinion_type: { type: Boolean },
    content: { type: String },
    created_at: { type: String },
    updated_at: { type: String },
    user: { type: Number },
    article: { type: Number },
    emotion: { type: String },
    like_users_count: { type: Number },
    like_users: { type: Array },
    username: { type: String },
  },
  data: () => {
    return {
      isLike: false,
      // likeCnt: this.like_users_count,
      articleno: "",
      isUpdate: false,
      borderColor: "#2962FF",
    };
  },
  methods: {
    ...mapActions(['getProfile']),

    ProfileOn: function(message) {
      switch (message) {
          case "profile":
          console.log("ADfadf"+this.user);
          this.getProfile(this.user);
          this.$store.commit("CHANGE_PROFILE", true);
          break;
      }
    },
    thumbUp() {
      if (this.isLoginToken == "") {
        this.$store.commit("CHANGE_DIALOG", true);
        return;
      }
      axios
        .post(`${API_BASE_URL}articles/${this.id}/comment_like/`, {
          user: this.$store.state.userInfo.id,
        })
        .then((res) => {
          console.log(res);
          if (this.getLike) {
            this.like_users_count--;
            console.log(this.like_users_count);
          } else {
            this.like_users_count++;
            console.log(this.like_users_count);
          }
          this.$store.dispatch("opinionStore/opinionDetail", this.article);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    changeUpdate(check) {
      this.isUpdate = check;
    },

    getBorder(type) {
      let choice = 'right';
      this.borderColor = '#D50000';
      if (type == true) {
        choice = 'left';
        this.borderColor = '#2962FF';
      }

      return choice;
    },
  },
  created() {},
};
</script>

<style scoped>
.mr-le {
  margin-left: 15px;
}

.border-line {
  border: 1px solid #cfd8dc;
  margin-bottom: 7px;
}
.bad {
  color:red;
}
.positive {
  color: goldenrod;
}
</style>
