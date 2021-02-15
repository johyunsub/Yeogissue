<template>
  <v-container>
    <v-row class="mr-tp">
      <v-col cols="2"></v-col>
      <v-col>
        <p class="blue--text mr-bt text-center">
          <v-icon small>fas fa-bars</v-icon> {{ opinionData.category }}
          <v-icon
            medium
            color="yellow"
            style="float:right; cursor: pointer"
            v-if="!opinionData.scrap_users.includes(userInfo.id) || isLoginToken == ''"
            @click="bookmarkChange('far')"
            >far fa-bookmark</v-icon
          >
          <v-icon
            medium
            color="yellow"
            style="float:right; cursor: pointer"
            v-if="opinionData.scrap_users.includes(userInfo.id)"
            @click="bookmarkChange('fas')"
            >fas fa-bookmark</v-icon
          >
        </p>
        <p class="display-2 text-center py-4">{{ opinionData.title }}</p>

        <!-- 밑으로 float 적용 안되게 -->
        <div style="clear:both;"></div>

        <div class="grey--text text-center">
          by {{ opinionData.username }} | 날짜 {{ opinionData.created_at.substr(0, 10) }}
          <span v-if="opinionData.user == userInfo.id">
            <span>| </span><span class="choice_cursor text-bt" @click="opUpdate">수정</span> |
            <span class="choice_cursor text-bt" @click="opDelete">삭제</span>
          </span>
        </div>

        <v-divider class="my-10"></v-divider>

        <Viewer v-if="content != ''" :initialValue="content" />

        <v-sheet height="10vh" lighten-5></v-sheet>

        <!-- 그래프 -->
        <v-row v-if="!opinionData.comment_type">
          <v-col></v-col>
          <v-card>
            <div >
            <pros-and-cons-chart :id="parseInt(this.$route.query.id)" />
            </div>
          </v-card>
          <v-col></v-col>
        </v-row>

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
          <v-col cols="4"></v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row class="mt-3">
          <v-icon v-if="!getLike" medium color="red" class="choice_cursor" @click="isLogin"
            >far fa-heart</v-icon
          >
          <v-icon v-if="getLike" medium color="red" class="choice_cursor" @click="isLogin"
            >fas fa-heart</v-icon
          >
          <span class="ml-3">
            {{ opinionData.like_users_count }}
          </span>
          <v-spacer></v-spacer>
          <!-- <p class="text-right"><span class="choice_cursor text-bt" @click="opUpdate">수정</span> | <span class="choice_cursor text-bt" @click="opDelete">삭제</span></p> -->
        </v-row>
        <v-row>
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
              @take="take"
          /></v-col>
        </v-row>

        <!-- 댓글 paging -->
        <div class="text-center mr-tp">
          <v-pagination v-model="page" :length="opinionCommentPagingCnt" circle></v-pagination>
        </div>
<<<<<<< HEAD

        <!-- 댓글 등록 -->
        <v-row class="mt-10 mb-10">
          <v-col cols="1"></v-col>
          <v-col class="mr-auto"> <comment-create :type="'create'" :propContent="''"/></v-col>
        </v-row>
=======
        
>>>>>>> 340db38a25b22fe079df7a3b1d4410089bbaee7e
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
    };
  },
  watch: {
    page: function(newVal) {
      this.$store.commit("opinionStore/SET_OPINION_COMMENT_SELECT", (newVal - 1) * 10);
      this.$store.commit("opinionStore/SET_OPINION_COMMENT_PAGING", (newVal - 1) * 10);
    },
  },
  methods: {
    ...mapActions("opinionStore", ["opinionDetail", "opinionDelete", "bookmarkUpdate"]),
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
      this.thumbUp();
    },
    thumbUp() {
      axios.post(`${API_BASE_URL}articles/${this.$route.query.id}/like/`, {
        user: this.$store.state.userInfo.id,
      });
      if (this.getLike) {
        this.opinionData.like_users_count--;
      } else {
        this.opinionData.like_users_count++;
      }
      this.opinionDetail(this.opinionData.id);
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
  },
  created() {
    // this.opinionDetail(this.$route.query.id);

    axios
      .get(`${API_BASE_URL}articles/${this.$route.query.id}/`)
      .then((res) => {
        console.log(res.data.content);
        this.content = res.data.content;
        this.$store.commit("opinionStore/SET_OPINION_DETAIL", res.data);
        this.$store.commit("opinionStore/SET_OPINION_COMMENT", res.data.comment_set);
        this.$store.commit("opinionStore/SET_OPINION_COMMENT_PAGING", 0);
      })
      .catch((err) => console.log(err.response));
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
