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

        #해시태그
        <v-row class="mr-tp">
          <v-chip-group mandatory>
            <v-chip v-for="tag in detailData.hashtags" :key="tag.name"> 
              {{ tag.name }}
            </v-chip>
          </v-chip-group>
          <v-col cols="4"></v-col>
        </v-row>

        <v-row>
          <v-col></v-col>
          <v-col class="mr-auto">
          <v-row>
            <v-icon v-if="!isLike" large class="choice_cursor" @click="isLogin">mdi-thumb-up-outline</v-icon>
            <v-icon v-if="isLike" large class="choice_cursor" @click="isLogin">mdi-thumb-up</v-icon>
          </v-row>
          <v-row>
            <v-chip
              class="ma-2"
              color="green"
              text-color="white"
            >
              <v-avatar
                left
                class="green darken-4"
              >
                {{ likeCnt }}
              </v-avatar>
              공감
            </v-chip>
            </v-row>
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
              :emotion="item.emotion"
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
    isLogin(){
      if(localStorage.getItem('token') == null){
        alert("로그인 후 이용가능합니다.")
      }else{
        this.thumbUp();
      }
    },
    thumbUp() {
      axios.post(`${API_BASE_URL}articles/${this.$route.query.id}/like/`, {user: this.$store.state.userInfo.id})
      if(this.isLike) {
        this.likeCnt--;
      }else{
        this.likeCnt++;
      }
      this.isLike = !this.isLike;
    },

  },
  created() {
    this.loginedUserId = this.$store.state.userInfo.id;
    console.log(this.loginedUserId)
    axios
        .get(`${API_BASE_URL}articles/${this.$route.query.id}`)
        .then((res) => {
          this.$store.commit('opinionStore/SET_OPINION_DETAIL', res.data);
          this.$store.commit('opinionStore/SET_OPINION_COMMENT', res.data.comment_set);
          this.$store.commit('opinionStore/SET_OPINION_COMMENT_PAGING', 0);
          this.detailData = res.data;
          this.likeCnt = res.data.like_users.length;
          console.log(this.loginedUserId)
          if(this.detailData.like_users.includes(this.loginedUserId)){
          this.isLike = true;
          }
        })
        .catch((err) => {
          console.log(err.response);
        });
  },
  updated() {
  },
}
</script>

<style scoped>
#recommend {
  margin-right: 10px;
}
.text-bt:hover {
  border-bottom: 1px solid gray;
}
</style>
