<template>
  <v-container>
    <v-row class="mr-tp">
      <v-col cols="2"></v-col>
      <v-col>
        <p class="blue--text mr-bt">{{ detailData.category }}</p>
        <p class="display-2">{{ detailData.title }}</p>
        <p class="grey--text">
          {{ detailData.user }} | 날짜 | 조회수 {{ detailData.read_count }} |
          <span class="choice_cursor text-bt" @click="opUpdate">수정</span> |
          <span class="choice_cursor text-bt" @click="opDelete">삭제</span>
        </p>
        <v-divider class="my-4"></v-divider>

        <!-- <p class="text-justify">
          {{ opinionData.content }}
        </p> -->

        <Viewer v-if="detailData.content != null" :initialValue="detailData.content" /> 


        <v-row>
          <v-col></v-col>
          <v-col class="mr-auto">
            <v-icon v-if="!isLike" large class="choice_cursor" @click="thumbUp">mdi-thumb-up-outline</v-icon>
            <v-icon v-if="isLike" large class="choice_cursor" @click="thumbDown">mdi-thumb-up</v-icon>
            <p>{{ likeCnt }}</p>
          </v-col>
        </v-row>

        <!-- 댓글 -->
        <v-row>
          <v-col cols="1"></v-col>
          <v-col class="mr-auto"
            ><comment
              v-for="item in opinionCommentPaging"
              :key="item.id"
              :type="item.opinion_type"
              :content="item.content"
              :created_at="item.created_at"
              :updated_at="item.updated_at"
              :user="item.user"
              :article="item.article"
          /></v-col>
        </v-row>

        <!-- 댓글 paging -->
        <div class="text-center mr-tp">
          <v-pagination v-model="page" :length="opinionCommentPagingCnt" circle></v-pagination>
        </div>

        <!-- 댓글 등록 -->
        <v-row class="mt-10 mb-10">
          <v-col cols="1"></v-col>
          <v-col class="mr-auto"> <comment-create /></v-col>
        </v-row>
      </v-col>
      <v-col cols="2"></v-col>

      <!-- footer쓸까? -->
    </v-row>
  </v-container>
</template>

<script>
import Comment from '../../components/Opinion/Comment.vue';
import CommentCreate from '../../components/Opinion/CommentCreate.vue';
import { mapState, mapActions } from 'vuex';

import "codemirror/lib/codemirror.css"; 
import "@toast-ui/editor/dist/toastui-editor.css"; 
import { Viewer } from "@toast-ui/vue-editor";

import axios from 'axios';
import { API_BASE_URL } from "../../config";


export default {
  components: { Comment, CommentCreate, Viewer },
  computed: {
    ...mapState('opinionStore', [
      'opinionComment',
      'opinionCommentPaging',
      'opinionCommentPagingCnt',
      'likedOpinion',
    ]),
  },
  data: function() {
    return {
      page: 1,
      pageCnt: 3,
      detailData : Object,
      isLike: false,
      likeCnt: 0,
    };
  },
  watch: {
    page: function(newVal) {
      this.$store.commit('opinionStore/SET_OPINION_COMMENT_PAGING', (newVal - 1) * 10);
    },
  },
  methods: {
    ...mapActions('opinionStore', ['opinionDetail', 'opinionDelete', 'opinionLike']),
    opUpdate() {
      this.$router.push(`/opinionWrite?type=update`);
    },
    opDelete() {
      this.opinionDelete(this.detailData.id);
      this.$router.push({ name: 'Opinion' });
    },
    thumbUp() {
      this.isLike = !this.isLike;
      this.opinionLike(this.opinionData.user)
    },
    thumbDown() {
      this.isLike = !this.isLike;
      //좋아요 취소 미완성
    }
  },
  created() {
    axios
        .get(`${API_BASE_URL}articles/${this.$route.query.id}`)
        .then((res) => {
          this.$store.commit('opinionStore/SET_OPINION_DETAIL', res.data);
          this.$store.commit('opinionStore/SET_OPINION_COMMENT', res.data.comment_set);
          this.$store.commit('opinionStore/SET_OPINION_COMMENT_PAGING', 0);
          this.detailData = res.data;
        })
        .catch((err) => {
          console.log(err.response);
        });
  },
  updated() {
    this.likeCnt = this.opinionData.like_users.length;
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
