<template>
  <div>
    <div v-if="isUpdate == false">
      <v-alert class="border-line" :border="bor" colored-border :color="borderColor">
        <v-row>
          <v-col>
            <div class="text--primary ">
              <a text @click="ProfileOn('profile')">{{ username }}</a> |
              {{ updated_at.replace("T", " ").substr(0, 16) }}
            </div>
          </v-col>
          <v-col cols="auto" v-if="!like_users.includes(userInfo.id)">
            <div class="choice_cursor" @click="thumbUp">
              <v-icon small>mdi-thumb-up-outline</v-icon> {{ like_users_count }}
            </div>
          </v-col>
          <v-col cols="auto" v-if="like_users.includes(userInfo.id)" >
            <div class="choice_cursor" @click="thumbUp">
              <v-icon small>mdi-thumb-up</v-icon> {{ like_users_count }}
            </div>
          </v-col>
          <v-col cols="auto"> <comment-menu :id="id" v-on:CommentUp="changeUpdate(true)"/></v-col>
        </v-row>

        <v-row>
          <v-col cols="2">
            <div v-if="emotion == '기쁨'">
              <i class="far fa-grin-squint positive fa-2x"></i><br />
              기쁨
            </div>

            <div v-else-if="emotion == '감정불가'">
              감정불가
            </div>

            <div v-else-if="emotion == '신뢰'">
              <i class="far fa-grin-stars positive fa-2x"></i>
              <br />
              신뢰
            </div>

            <div v-else-if="emotion == '놀라움'">
              <i class="far fa-surprise positive fa-2x"></i><br />놀라움
            </div>

            <div v-else-if="emotion == '슬픔'">
              <i class="far fa-sad-tear positive fa-2x"></i><br />슬픔
            </div>

            <div v-else-if="emotion == '공포'">
              <i class="far fa-grimace positive fa-2x"></i><br />공포
            </div>

            <div v-else-if="emotion == '기대'">
              <i class="far fa-kiss-beam positive fa-2x"></i><br />기대
            </div>

            <div v-else-if="emotion == '혐오'">
              <i class="far fa-dizzy bad fa-2x"></i><br />혐오
            </div>

            <div v-else><i class="far fa-angry bad fa-2x"></i><br />분노</div>
          </v-col>

          <v-col cols="9">
            <span class="ml-5" v-if="badcomment >= 30" style="color: red">
              신고회수가 30회 이상입니다.</span
            >
            <span class="ml-5" v-if="badcomment < 30">{{ content }}</span>
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

import { mapState, mapActions } from "vuex";
import axios from "axios";
import { API_BASE_URL } from "../../config";

export default {
  components: { CommentMenu, CommentCreate },
  computed: {
    ...mapState("opinionStore", ["opinionComment"]),
    ...mapState(["isLoginToken", "userInfo"]),
  },
  props: {
    id: { type: Number },
    badcomment: { type: Number },
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
    board_type: { type: Boolean },
  },
  data: () => {
    return {
      isLike: false,
      articleno: "",
      isUpdate: false,
      borderColor: "white",
      bor: "top",
    };
  },
  methods: {
    ...mapActions(["getProfile"]),

    ProfileOn: function(message) {
      switch (message) {
        case "profile":
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
      // console.log("저장이유");
      // this.commentThumUp({
      //   id: this.$route.query.id,
      //   user:this.userInfo.id
      // });
      axios
        .post(`${API_BASE_URL}articles/${this.id}/comment_like/`, {
          user: this.$store.state.userInfo.id,
        })
        .then((res) => {
          console.log(res);
          this.$store.dispatch("opinionStore/opinionDetail", this.article);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    changeUpdate(check) {
      this.isUpdate = check;
    },

    getBorder() {
      console.log("ddd", this.board_type);
      if (this.board_type) {
        this.bor = "top";
        this.borderColor = "white";
        return "";
      }

      this.bor = "left";
      this.borderColor = "#2962FF";
      if (this.opinion_type == false) {
        this.bor = "right";
        this.borderColor = "#D50000";
      }
    },
  },
  created() {
    this.getBorder();
  },
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
  color: #d4473b;
}
.positive {
  color: #5d9783;
}
</style>
