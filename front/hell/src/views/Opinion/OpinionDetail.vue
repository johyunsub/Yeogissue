<template>
  <v-container>
    <v-row class="mr-tp">
      <v-col cols="2"></v-col>
      <v-col>
        <p class="blue--text mr-bt text-center">
          <v-icon small>fas fa-bars</v-icon> {{ opinionData.category }}
        </p>
        <p class="display-2 text-center py-4">{{ opinionData.title }}</p>

        <!-- 밑으로 float 적용 안되게 -->
        <div style="clear: both"></div>

        <div class="grey--text text-center">
          by <a text @click="ProfileOn('profile')">{{ opinionData.username }}</a> | 날짜
          {{ opinionData.created_at.substr(0, 10) }}
          <span v-if="opinionData.user == userInfo.id">
            <span>| </span><span class="choice_cursor text-bt" @click="opUpdate">수정</span> |
            <span class="choice_cursor text-bt" @click="opDelete">삭제</span>
          </span>
        </div>
        <v-divider class="my-10"></v-divider>

        <Viewer v-if="content != ''" :initialValue="content" />

        <v-sheet height="10vh" lighten-5></v-sheet>

        <!-- 해시태그 -->
        <v-row class="mr-tp mb-5">
          <v-chip-group>
            <v-chip
              outlined
              v-for="tag in opinionData.hashtags"
              :key="tag.name"
              @click="search(tag.name)"
            >
              <span style="color: black; font-weight: 600">
                <v-icon small color="pink">fas fa-hashtag</v-icon>
                {{ tag.name }}
              </span>
            </v-chip>
          </v-chip-group>
          <!-- 클럽 -->
          <v-chip outlined v-if="opinionData.clubname != ''" @click="movePage()"
            ><span style="color: blue; font-weight: 600">
              <v-icon small color="blue">fas fa-hashtag</v-icon>
              {{ opinionData.clubname }}</span
            ></v-chip
          >
          <v-col cols="4"></v-col>
        </v-row>
        <v-divider></v-divider>

        <v-row class="mt-3">
          <v-icon
            v-if="!opinionData.like_users.includes(userInfo.id)"
            medium
            color="red"
            class="choice_cursor"
            @click="isLogin"
            >far fa-heart</v-icon
          >
          <v-icon
            v-if="opinionData.like_users.includes(userInfo.id)"
            medium
            color="red"
            class="choice_cursor"
            @click="isLogin"
            >fas fa-heart</v-icon
          >
          <span class="ml-3">
            {{ opinionData.like_users_count }}
          </span>

          <v-spacer></v-spacer>
          <span>스크랩 하기</span>
          <v-icon
            medium
            color="yellow"
            style="float: right; cursor: pointer"
            class="ml-2"
            v-if="!opinionData.scrap_users.includes(userInfo.id) || isLoginToken == ''"
            @click="bookmarkChange('far')"
            >far fa-bookmark</v-icon
          >
          <v-icon
            medium
            color="yellow"
            style="float: right; cursor: pointer"
            v-if="opinionData.scrap_users.includes(userInfo.id)"
            @click="bookmarkChange('fas')"
            >fas fa-bookmark</v-icon
          >

          <!-- <p class="text-right"><span class="choice_cursor text-bt" @click="opUpdate">수정</span> | <span class="choice_cursor text-bt" @click="opDelete">삭제</span></p> -->
        </v-row>
        <v-row>
          <v-col></v-col>
        </v-row>
        <v-row style="height: 100px"></v-row>

        <div>
          <v-col cols="1"></v-col>
          <v-alert color="cyan" border="left" elevation="2" colored-border icon="fas fa-volume-up">
            <span>
              올바른 댓글 문화를 양성하기 위해 작성한 댓글의 감정을 AI로 분석하여 나타냅니다.</span
            >
            <br />
            <span>
              댓글의 감정이 '혐오' 또는 '분노'로 나타날 경우 한 번 더 검토해보실 것을 권장합니다.
            </span>
          </v-alert>
        </div>

        <!-- 그래프 -->
        <v-row class="mt-5" v-if="!opinionData.comment_type">
          <v-col></v-col>
          <v-card>
            <div>
              <pros-and-cons-chart :id="parseInt(this.$route.query.id)" />
            </div>
          </v-card>
          <v-col></v-col>
        </v-row>

        <!-- 댓글 -->
        <v-row class="mt-10 mb-10">
          <v-col cols="1"></v-col>
          <v-col class="mr-auto"> <comment-create :type="'create'" :propContent="''"/></v-col>
        </v-row>

        <v-row>
          <v-col cols="1"></v-col>
          <v-col class="mr-auto"
            ><comment
              v-for="item in opinionCommentPaging"
              :key="item.id"
              :id="item.id"
              :badcomment="item.badcomment"
              :opinion_type="item.opinion_type"
              :content="item.content"
              :created_at="item.created_at"
              :updated_at="item.updated_at"
              :user="item.user"
              :article="item.article"
              :emotion="item.emotion"
              :like_users_count="item.like_users_count"
              :like_users="item.like_users"
              :username="item.username"
              :board_type="opinionData.comment_type"
              @take="take"
          /></v-col>
        </v-row>

        <!-- 댓글 paging -->
        <div class="text-center mr-tp">
          <v-pagination v-model="page" :length="opinionCommentPagingCnt" circle></v-pagination>
        </div>
      </v-col>
      <v-col cols="2"></v-col>

      <!-- footer쓸까? -->
    </v-row>
  </v-container>
</template>

<script>
import Comment from "../../components/Opinion/Comment.vue";
import ProsAndConsChart from "../../components/Opinion/ProsAndConsChart.vue";
import CommentCreate from "../../components/Opinion/CommentCreate.vue";

import { mapState, mapActions } from "vuex";

import "codemirror/lib/codemirror.css";
import "@toast-ui/editor/dist/toastui-editor.css";
import { Viewer } from "@toast-ui/vue-editor";

import axios from "axios";
import { API_BASE_URL } from "../../config";

export default {
  components: { Comment, CommentCreate, Viewer, ProsAndConsChart },
  computed: {
    ...mapState("opinionStore", [
      "opinionData",
      "opinionComment",
      "opinionCommentPaging",
      "opinionCommentPagingCnt",
    ]),
    ...mapState(["userInfo", "isLoginToken"]),
    getLike: {
      get: function() {
        if (this.opinionData.like_users.includes(this.$store.state.userInfo.id)) {
          return true;
        }
        return false;
      },
      set: function() {},
    },
  },
  data: function() {
    return {
      page: 1,
      pageCnt: 3,
      content: "",
      alert: true,
      clubTag: "",
      club_pk: "",
      creat: false,
    };
  },
  watch: {
    page: function(newVal) {
      this.$store.commit("opinionStore/SET_OPINION_COMMENT_SELECT", (newVal - 1) * 10);
      this.$store.commit("opinionStore/SET_OPINION_COMMENT_PAGING", (newVal - 1) * 10);
    },
  },
  methods: {
    ...mapActions("opinionStore", ["opinionDetail", "opinionDelete", "bookmarkUpdate", "thumbUp"]),
    ...mapActions(["getProfile"]),
    ProfileOn: function(message) {
      switch (message) {
        case "profile":
          this.getProfile(this.opinionData.user);
          this.$store.commit("CHANGE_PROFILE", true);
          break;
      }
    },
    opUpdate() {
      this.$router.push(`/opinionWrite?type=update`);
    },
    opDelete() {
      this.opinionDelete(this.opinionData.id);
      this.$router.push({ name: "Opinion" });
    },
    isLogin() {
      if (this.isLoginToken == "") {
        this.$store.commit("CHANGE_DIALOG", true);
        return;
      }
      console.log("좋아요 버튼" + this.$route.query.id);
      this.thumbUp({ id: this.$route.query.id, user: this.userInfo.id });
    },

    take() {
      console.log("받음");
    },

    bookmarkChange(check) {
      let message = "";
      if (check == "far") {
        if (this.isLoginToken == "") {
          this.$store.commit("CHANGE_DIALOG", true);
          return;
        }
        message = "저장 되었습니다.";
      } else message = "취소 되었습니다.";

      this.bookmarkUpdate(this.userInfo.id);
      this.$toasted.show(message, {
        theme: "outline",
        position: "bottom-center",
        duration: 500,
      });
    },

    search(search) {
      this.$router.push(`/opinion?search=${search}`);
    },

    getClubTagName() {
      if (this.data.club_pk != 0) {
        axios
          .get(`${API_BASE_URL}club/club_detail/${this.club_pk}/`)
          .then((res) => {
            this.clubTag = res.data.title;
          })
          .catch((err) => console.log(err.response));
      }
    },
    movePage() {
      this.$router.push(`/clubDetail?id=${this.club_pk}`);
    },
    getDetail() {
      axios
        .get(`${API_BASE_URL}articles/${this.$route.query.id}/`)
        .then((res) => {
          console.log(res.data.content);
          this.content = res.data.content;
          this.club_pk = res.data.club_pk;
          // this.getClubTagName();
          this.$store.commit("opinionStore/SET_OPINION_DETAIL", res.data);
          this.$store.commit("opinionStore/SET_OPINION_COMMENT", res.data.comment_set);
          this.$store.commit("opinionStore/SET_OPINION_COMMENT_PAGING", 0);
        })
        .catch((err) => console.log(err.response));
    },
  },

  updated() {
    console.log("의견디테일 업데이트");
  },

  created() {
    // this.opinionDetail(this.$route.query.id);
    window.scrollTo(0, 0);
    this.getDetail();
  },
};
</script>

<style scoped>
#recommend {
  margin-right: 10px;
}
.text-bt:hover {
  border-bottom: 1px solid gray;
}
</style>
