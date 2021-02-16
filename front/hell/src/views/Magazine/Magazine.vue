<template>
  <v-row class="justify-center">
    <img
      :src="require('../../assets/매거진메인.png')"
      style="height: 250; width: 100%; position: relative"
      alt=""
    />

    <!-- 인기 순위 -->
    <v-card class="mx-auto my-5 ml-5 elevation-5" style="border-radius: 15px;" max-width="400" :elevation="2">
     <v-card-title class="headline pl-6 h6" style="background-color: white;">
        <span class="ma-auto" style="">
           <span class="ml-3">댓글 많은 순</span>
          </span>
      </v-card-title>
      <v-divider></v-divider>

     <v-card-text class="mt-4">
        <div v-for="(item, n) in commentRank" :key="item.id">
            <span style="color:blue;">{{ n + 1 }}</span>
            <span class="ml-4">{{ item.title }}</span>
          </div>
      </v-card-text>
    </v-card>

        <!-- 좋아요 순위 -->
    <v-card class="mx-auto my-5 ml-5 elevation-5" style="border-radius: 15px;" max-width="400" :elevation="2">
     <v-card-title class="headline pl-6 h6" style="background-color: white;">
        <span class="ma-auto" style="">
           <span class="ml-3">좋아요 많은 순</span>
          </span>
      </v-card-title>
      <v-divider></v-divider>

     <v-card-text class="mt-4">
        <div v-for="(item, n) in likeRank" :key="item.id">
            <span style="color:blue;">{{ n + 1 }}</span>
            <span class="ml-4">{{ item.title }}</span>
          </div>
      </v-card-text>
    </v-card>

    <!-- 해시태그 워드 클라우드 -->
    <wordcloud
      :data="hashAll"
      nameKey="name"
      valueKey="post_cnt"
      color="Accent"
      :showTooltip="true"
      :wordClick="wordClickHandler"
    >
    </wordcloud>

  </v-row>
</template>

<script>
import wordcloud from "vue-wordcloud";
import axios from 'axios';
import { API_BASE_URL } from '../../config';

export default {
  name: "Magazine",
  components: {
    wordcloud,
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log("wordClickHandler", name, value, vm);
    },
    getHashTag(){
        axios.post(`${API_BASE_URL}articles/hash_emotion`, {hashtag: '문제인'})
        .then((res) => {
          this.emotionData = res.data;
        })
        .catch((err) => console.log(err.response));
    },
    getHashAll(){
      axios.get(`${API_BASE_URL}articles/hash_all/`)
        .then((res) => {
          this.hashAll = res.data;
          console.log(this.hashAll[0]);
        })
        .catch((err) => console.log(err.response));
    },
    getCommentRank(){
      axios.get(`${API_BASE_URL}articles/comment_rank/`)
      .then((res) => {
        this.commentRank = res.data;
        console.log(this.commentRank);
      })
      .catch((err) => console.log(err.response));
    },
    getLikeRank(){
      axios.get(`${API_BASE_URL}articles/like_rank/`)
      .then((res) => {
        this.likeRank = res.data;
        console.log(this.likeRank);
      })
      .catch((err) => console.log(err.response));
    }
  },
  data() {
    return {
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],
      emotionData : {},
      hashAll:{},
      commentRank:{},
      likeRank:{},
     
    };
  },
  created(){
    this.getHashAll();
    this.getCommentRank();
    this.getLikeRank();
  }
};
</script>

<style>
</style>