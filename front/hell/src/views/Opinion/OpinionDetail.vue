<template>
  <v-container>
    <v-row class="mr-tp">
      <v-col cols="2"></v-col>
      <v-col>
        <p class="blue--text mr-bt">{{ opinionData.category }}</p>
        <p class="display-2">{{ opinionData.title }}</p>
        <p class="grey--text">
          {{ opinionData.user }} | 날짜 | 조회수 {{ opinionData.read_count }} |
          <span class="choice_cursor text-bt" @click="opUpdate">수정</span> |
          <span class="choice_cursor text-bt" @click="opDelete">삭제</span>
        </p>
        <v-divider class="my-4"></v-divider>

        <p class="text-justify">
          {{ opinionData.content }}
        </p>

        <v-row>
          <v-col></v-col>
          <v-col class="mr-auto">
          <v-row>
            <v-icon v-if="!isLike" large class="choice_cursor" @click="thumbUp">mdi-thumb-up-outline</v-icon>
            <v-icon v-if="isLike" large class="choice_cursor" @click="thumbUp">mdi-thumb-up</v-icon>
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
import axios from 'axios';
import { API_BASE_URL } from "../../config";


export default {
  components: { Comment, CommentCreate },
  computed: {
    ...mapState('opinionStore', [
      'opinionData',
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
      items: [
        { tab: '1' },
        { tab: '2' },
        { tab: '3' },
        { tab: '4' },
        { tab: '5' },
        { tab: '6' },
        { tab: '7' },
        { tab: '8' },
        { tab: '9' },
        { tab: '0' },
      ],
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
      this.opinionDelete(this.opinionData.id);
      this.$router.push({ name: 'Opinion' });
    },
    thumbUp() {
      this.isLike = !this.isLike;
      this.opinionLike(this.opinionData);
    },
  },
  created() {
    this.opinionDetail(this.$route.query.id);
    axios.get(`${API_BASE_URL}articles/${this.$route.query.id}`)
      .then((res) => {
        this.likeCnt = res.data.like_users.length;
        if(res.data.like_users.includes(res.data.user)){
          this.isLike = true;
        }
          this.likeCnt = res.data.like_users.length;
           console.log(this.likeCnt + " <<<<<")
      })

    },
  updated() {
    axios.get(`${API_BASE_URL}articles/${this.$route.query.id}`)
      .then((res) => {
        this.likeCnt = res.data.like_users.length;
        if(res.data.like_users.includes(res.data.user)){
          this.isLike = true;
        }
          this.likeCnt = res.data.like_users.length;
           
      })
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
