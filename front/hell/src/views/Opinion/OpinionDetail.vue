<template>
  <v-container>
    <v-row class="mr-tp">
      <v-col cols="2"></v-col>
      <v-col>
        <p class="blue--text mr-bt text-center">
          <v-icon small>fas fa-bars</v-icon> {{ opinionData.category }}
        </p>
        <p class="display-2 text-center py-4">{{ opinionData.title }}</p>

        <div class="grey--text text-center">
          by {{ opinionData.username }} | 날짜 {{ opinionData.created_at.substr(0, 10) }}
          <span v-if="opinionData.user == userInfo.id">
            <span>| </span><span class="choice_cursor text-bt" @click="opUpdate">수정</span> |
            <span class="choice_cursor text-bt" @click="opDelete">삭제</span>
          </span>
        </div>

        <v-divider class="my-10"></v-divider>

        <v-row>
          <v-spacer></v-spacer>
          <h4>스크랩 기능 넣어주세용 스크랩한 기사면 채워진 아이콘으로 바뀌게,,,</h4>
          <v-icon medium color="yellow">far fa-bookmark</v-icon>
          <v-icon medium color="yellow">fas fa-bookmark</v-icon>
        </v-row>
        <v-col cols="2"></v-col>
        <!-- <p class="text-justify">
          {{ opinionData.content }}
        </p> -->

        <Viewer v-if="opinionData.content != null" :initialValue="opinionData.content" />

        <v-sheet height="10vh" lighten-5></v-sheet>

        <!-- 해시태그 -->
        <v-row class="mr-tp mb-10">
          <v-chip-group>
            <v-chip outlined v-for="tag in opinionData.hashtags" :key="tag.name">
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
          <v-col></v-col>
          <v-col class="mr-auto">
            <v-row>
              <v-icon v-if="!getLike" large class="choice_cursor" @click="isLogin"
                >mdi-thumb-up-outline</v-icon
              >
              <v-icon v-if="getLike" large class="choice_cursor" @click="isLogin"
                >mdi-thumb-up</v-icon
              >
              <v-icon large color="red">far fa-heart</v-icon>
            </v-row>
            <v-row>
              <v-chip class="ma-2" color="green" text-color="white">
                <v-avatar left class="green darken-4">
                  {{ opinionData.like_users_count }}
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
              :id="item.id"
              :type="item.opinion_type"
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

import 'codemirror/lib/codemirror.css';
import '@toast-ui/editor/dist/toastui-editor.css';
import { Viewer } from '@toast-ui/vue-editor';

import axios from 'axios';
import { API_BASE_URL } from '../../config';

export default {
  components: { Comment, CommentCreate, Viewer },
  computed: {
    ...mapState('opinionStore', [
      'opinionData',
      'opinionComment',
      'opinionCommentPaging',
      'opinionCommentPagingCnt',
    ]),
    ...mapState(['userInfo']),
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
    };
  },
  watch: {
    page: function(newVal) {
      this.$store.commit('opinionStore/SET_OPINION_COMMENT_PAGING', (newVal - 1) * 10);
    },
  },
  methods: {
    ...mapActions('opinionStore', ['opinionDetail', 'opinionDelete']),
    opUpdate() {
      this.$router.push(`/opinionWrite?type=update`);
    },
    opDelete() {
      this.opinionDelete(this.opinionData.id);
      this.$router.push({ name: 'Opinion' });
    },
    isLogin() {
      if (localStorage.getItem('token') == null) {
        alert('로그인 후 이용가능합니다.');
      } else {
        this.thumbUp();
      }
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
      console.log('받음');
    },
  },
  created() {
    this.opinionDetail(this.$route.query.id);
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
