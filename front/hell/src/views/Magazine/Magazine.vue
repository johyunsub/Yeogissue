<template>
  <v-row class="justify-center">
    <img
      :src="require('../../assets/매거진메인.png')"
      style="height: 250; width: 100%; position: relative"
      alt=""
    />

    <!-- 해시태그 워드 클라우드 -->
    <wordcloud
      :data="defaultWords"
      nameKey="name"
      valueKey="value"
      color="Accent"
      :showTooltip="true"
      :wordClick="wordClickHandler"
    >
    </wordcloud>
    {{hashAll[0].name}}
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
    }
  },
  data() {
    return {
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],
      emotionData : {},
      hashAll:{},
      defaultWords: [
        {
          name: "Cat",
          value: 26,
        },
        {
          name: "fish",
          value: 19,
        },
        {
          name: "things",
          value: 18,
        },
        {
          name: "look",
          value: 16,
        },
        {
          name: "two",
          value: 15,
        },
        {
          name: "fun",
          value: 9,
        },
        {
          name: "know",
          value: 9,
        },
        {
          name: "good",
          value: 9,
        },
        {
          name: "play",
          value: 6,
        },
      ],
    };
  },
  created(){
    this.getHashAll();
  }
};
</script>

<style>
</style>