<template>
  <v-row class="justify-center">
    <div class="home-image" id="out">
      <v-sheet height="10vh" color="#F4CECE"></v-sheet>
      <div class="ma-auto mt-10" id="in">
        <VueSlickCarousel v-bind="slickData" :style="{ height: '250px' }">
          <div><img :src="require('../assets/메인1.png')" class="main-image" alt="" /></div>
          <div><img :src="require('../assets/메인2.png')" class="main-image" alt="" /></div>
          <div><img :src="require('../assets/메인3.png')" class="main-image" alt="" /></div>
          <div><img :src="require('../assets/메인4.png')" class="main-image" alt="" /></div>
        </VueSlickCarousel>
      </div>
      <div class="mt-10">
        <v-row>
          <v-col cols="4" class="mr-auto"></v-col>
          <v-text-field
            @keypress.enter="search_hashtag"
            color="purple"
            label="다른 사람의 의견이 궁금한 주제를 검색해보세요!"
            v-model="search"
            single-line
            rounded
            outlined
            background-color="white"
            prepend-inner-icon="fas fa-hashtag"
            clear-icon="mdi-close-circle-outline"
          ></v-text-field>
          <v-col cols="4" class="mr-auto"></v-col>
        </v-row>
      </div>

      <div>
        <v-row>
          <v-col cols="2" class="mr-auto"></v-col>
          <v-chip
            v-for="tag in top_hashtags"
            :key="tag.name"
            @click="search_tag(tag.name)"
            medium
            class="justify-center mr-1 main-chip"
            color="#F4CECE"
          >
            <span style="color: black; font-weight: 600;">
              <v-icon small color="pink">fas fa-hashtag</v-icon>
              {{ tag.name }}</span
            >
          </v-chip>
          <v-col cols="2" class="mr-auto"></v-col>
        </v-row>
      </div>

      <v-sheet height="15vh" color="#F4CECE"></v-sheet>
      <v-row>
        <v-col class="mx-auto"></v-col>
        <div data-aos="fade-up" data-aos-duration="1000" v-for="item in items" :key="item.content">
          <main-card :data="item" />
        </div>
        <v-col class="mx-auto"></v-col>
      </v-row>
    </div>
  </v-row>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import { mapState, mapActions } from "vuex";
import MainCard from "../components/Home/MainCard.vue";

export default {
  name: "Home",
  components: { VueSlickCarousel, MainCard },
  computed: {
    ...mapState("opinionStore", ["top_hashtags"]),
  },
  data: () => ({
    search: "",

    slickData: {
      slidesToShow: 1,
      slidesToScroll: 1,
      speed: 400,
      autoplay: true,
      arrows: false,
      autoplaySpeed: 1500,
      vertical: true,
      verticalSwiping: true,
    },
    items: [
      {
        id: 1,
        title: "의견이슈",
        content: "다양한 이슈와 생각을 가득한 곳! 여러분의 의견을 공유하고,",
        content2: "#해시태그로 다른 사람의 의견을 검색해보세요!",
      },
      {
        id: 2,
        title: "모여이슈",
        content: "소통해보고 싶은 관심사가 있나요?",
        content2: "클럽을 생성하여 사람들을 모아보세요!",
      },
      {
        id: 3,
        title: "이슈랭킹",
        content: "핫한 트렌드가 궁금할 때!",
        content2: "하루 검색 이슈랭킹에서 확인하세요!",
      },
      {
        id: 4,
        title: "매거진",
        content: "댓글 많은 게시글과 많은 사람들의 공감을 얻은 좋아요 많은 게시글을 확인해보세요!",
        content2:''
      },
    ],
  }),
  methods: {
    ...mapActions("opinionStore", ["hash_top10", "hashOpinionList"]),
    search_hashtag() {
      console.log("ggg");
      this.hashOpinionList({ name: this.search });
      this.$router.push(`/opinion?search=${this.search}`);
    },
    search_tag(search) {
      this.$router.push(`/opinion?search=${search}`);
    },
  },
  created() {
    window.scrollTo(0, 0);
    this.hash_top10();
  },
};
</script>

<style>
.home-image {
  width: 100%;
  height: 1000px;
  background-color: #F4CECE;
  background-size: 100% 600px;
}

#out {
  width: 100%;
  text-align: center;
}
#in {
  display: inline-block;
  width: 500px;
  height: 98px;
}

#card-out {
  text-align: center;
}

#card-in {
  display: inline-block;
  width: 2000px;
  height: 98px;
}



.main-chip:hover{
  color: #8C05F7;
}
</style>
