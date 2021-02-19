<template>
  <v-row class="justify-center">
    <img
      :src="require('../../assets/매거진메인.png')"
      style="height: 250; width: 100%; position: relative"
      alt=""
    />

    <v-sheet height="100" width="100%" color=""></v-sheet>

    <div>
      <h1 style="text-align:center">
        활발한 논쟁이 이루어지고 있는 댓글 많은 게시글과 <br />
        많은 사람들의 공감을 얻은 좋아요 많은 게시글을 확인해보세요!
      </h1>
      <!-- 인기 순위 -->
      <v-row class="mt-10">
        <v-col cols="auto" class="mr-auto"></v-col>
        <v-card
          class="my-5 ml-5 elevation-5"
          style="border-radius: 15px;"
          max-width="400"
          :elevation="2"
        >
          <v-card-title class="headline pl-6 h6" style="background-color: white;">
            <span class="ma-auto" style="">
              <span class="ml-3">댓글 많은 게시글</span>
            </span>
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="mt-4">
            <div
              class="choice_cursor comment-card"
              v-for="(item, n) in commentRank"
              :key="item.id"
              @click="commentMove(item)"
            >
              <span style="color:blue;">{{ n + 1 }}</span>
              <span class="ml-4">{{ item.title }}</span>
            </div>
          </v-card-text>
          
        </v-card>

        <!-- 좋아요 순위 -->
        <v-card
          class="my-5 ml-5 elevation-5"
          style="border-radius: 15px;"
          max-width="400"
          :elevation="2"
        >
          <v-card-title class="headline pl-6 h6" style="background-color: white;">
            <span class="ma-auto" style="">
              <span class="ml-3">좋아요 많은 게시글</span>
            </span>
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="mt-4">
            <div
              class="choice_cursor comment-card"
              v-for="(item, n) in likeRank"
              :key="item.id"
              @click="commentMove(item)"
            >
              <span style="color:blue;">{{ n + 1 }}</span>
              <span class="ml-4">{{ item.title }}</span>
            </div>
          </v-card-text>
        </v-card>
        <v-col cols="auto" class="mr-auto"></v-col>
      </v-row>
    </div>

    <!-- 해시태그 워드 클라우드 -->
    <v-sheet height="100" width="100%" color=""></v-sheet>
    <h1>여기 이슈의 모든 해시태그의 감정 그래프를 확인해보세요!</h1>
    <wordcloud
      class="mt-10"
      :data="hashAll"
      nameKey="name"
      valueKey="post_cnt"
      color="Accent"
      :showTooltip="true"
      :wordClick="wordClickHandler"
    >
    </wordcloud>
    <v-col cols="12">
    <div class="text-center">
      <h3>클라우드를 클릭 해보세요! 밑에 나타납니다!</h3>
    </div>
    </v-col>
    <div>
      <graph-bubblecloud
        class="mt-10"
        :width="1000"
        :height="500"
        :padding-top="10"
        :padding-bottom="0"
        :padding-left="0"
        :padding-right="0"
        :values="emotionData"
        :colors="colors"
        :render-interval="0"
        @click="onClickEvent"
      >
      </graph-bubblecloud>
    </div>
  </v-row>
</template>

<script>
import wordcloud from "vue-wordcloud";
import axios from "axios";
import { API_BASE_URL } from "../../config";

export default {
  name: "Magazine",
  components: {
    wordcloud,
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log("wordClickHandler", name, value, vm);
      this.getHashTag(name);
      console.log(this.emotionData);
    },
    getHashTag(data) {
      axios
        .post(`${API_BASE_URL}articles/hash_emotion/`, { hashtag: data })
        .then((res) => {
          this.emotionData = res.data;
          console.log(this.emotionData);
          console.log("12312312312 ");
        })
        .catch((err) => console.log(err.response));
    },
    getHashAll() {
      axios
        .get(`${API_BASE_URL}articles/hash_all/`)
        .then((res) => {
          this.hashAll = res.data;
          console.log(this.hashAll[0]);
        })
        .catch((err) => console.log(err.response));
    },
    getCommentRank() {
      axios
        .get(`${API_BASE_URL}articles/comment_rank/`)
        .then((res) => {
          this.commentRank = res.data;
          console.log(this.commentRank);
        })
        .catch((err) => console.log(err.response));
    },
    getLikeRank() {
      axios
        .get(`${API_BASE_URL}articles/like_rank/`)
        .then((res) => {
          this.likeRank = res.data;
          console.log(this.likeRank);
        })
        .catch((err) => console.log(err.response));
    },
    onClickEvent: function(obj) {
      console.log(obj.data);
    },

    commentMove(commentData) {
      this.$router.push(`/opinionDetail?id=${commentData.id}`);
    },
  },
  data() {
    return {
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],
      // emotionData : [],
      emotionData: [],
      colors: function(data) {
        if (data[2] > 4000) {
          return 2;
        } else if (data[2] > 3000) {
          return 1;
        }

        return 0;
      },
      hashAll: [],
      commentRank: {},
      likeRank: {},
    };
  },
  created() {
    window.scrollTo(0, 0);
    this.getHashAll();
    this.getCommentRank();
    this.getLikeRank();
  },
};
</script>

<style>
.comment-card:hover {
  background-color: #faead4;
  border-radius: 20px 20px 20px 20px;
  padding: 4px;
}
.mgz {
  background-color: F4F4F4;
}
</style>
