<template>
  <v-row class="justify-center">
    <img
      :src="require('../../assets/매거진메인.png')"
      style="height: 250; width: 100%; position: relative"
      alt=""
    />

<v-sheet height="100" width="100%" color=""></v-sheet>
  
      <h1>1활발한 논쟁이 이루어지고 있는 댓글 많은 게시글과 많은 사람들의 공감을 얻은 좋아요 많은 게시글을 확인해보세요!</h1>

    <!-- 인기 순위 -->
    <v-card class="mx-auto my-5 ml-5 elevation-5" style="border-radius: 15px;" max-width="400" :elevation="2">
     <v-card-title class="headline pl-6 h6" style="background-color: white;">
        <span class="ma-auto" style="">
           <span class="ml-3">댓글 많은 게시글</span>
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
           <span class="ml-3">좋아요 많은 게시글</span>
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
   
   <div>
  <graph-bubblecloud
            :width="500"
            :height="500"
            :padding-top="5"
            :padding-bottom="0"
            :padding-left="0"
            :padding-right="0"
            :values="emotionData"
            :colors="colors"
            :render-interval="0"
            @click="onClickEvent">
        <note :text="'Bubble Cloud (Created by luavis)'" :align="'left'"></note>
    </graph-bubblecloud>
</div>

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
      this.getHashTag(name)
      console.log(this.emotionData)
    },
    getHashTag(data){
        axios.post(`${API_BASE_URL}articles/hash_emotion/`, {hashtag: data})
        .then((res) => {
          this.emotionData = res.data;
          console.log(this.emotionData,'12312312312 ')
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
    },
    onClickEvent: function(obj) {
            console.log(obj.data);
        }
  },
  data() {
    return {
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],
      // emotionData : [],
      emotionData : [[ "/index.jsp", 100, 1000 ],
            [ "/home.jsp", 70, 2000 ],
            [ "/admin.jsp", 30, 3000 ],
            [ "/test/a.jsp", 5, 8000 ],
            [ "/test/b.jsp", 50, 5000 ],
            [ "/test/c.jsp", 1, 10000 ],
            [ "/test/d.jsp", 1, 1000 ]],
      colors: function(data) {
            if(data[2] > 4000) {
                return 2;
            } else if(data[2] > 3000) {
                return 1;
            }

            return 0;
        },
      hashAll:[],
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