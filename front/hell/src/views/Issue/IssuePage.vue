<template>
  <v-sheet height="100%" color="#EEEEEE" lighten-5>
    <v-sheet height="15vh" color="#EEEEEE" lighten-5></v-sheet>
    <div class="text-center display-2" style="font-weight: 550">
      <span style="color: red">핫</span>한 트렌드가 궁금할 때
    </div>
    <div
      class="text-center display-1 mt-6"
      style="font-weight: 550; color: #42a5f5"
    >
      하루 검색 이슈 랭킹
    </div>
    <div class="ma-auto mt-5" style="width: 150px">
      <v-menu
        v-model="menu2"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on }">
          <v-text-field
            v-model="date"
            append-icon="mdi-calendar"
            v-on="on"
            filled
            background-color="white"
            readonly
            single-line
          ></v-text-field>
        </template>
        <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
      </v-menu>
    </div>

    <div class="ma-auto mt-10" style="width: 60%">
      <VueSlickCarousel ref="slick" v-bind="slickOptions">
        <issue-category-card :category="'스포츠'" :date="date" />
        <issue-category-card :category="'경제'" :date="date" />
        <issue-category-card :category="'IT/과학'" :date="date" />
        <issue-category-card :category="'연예'" :date="date" />
        <issue-category-card :category="'정치'" :date="date" />
        <issue-category-card :category="'해외'" :date="date" />
        <issue-category-card :category="'사회/생활'" :date="date" />
      </VueSlickCarousel>
    </div>
  </v-sheet>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
// optional style for arrows & dots
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import IssueCategoryCard from "../../components/Issue/IssueCategoryCard.vue";

export default {
  components: { VueSlickCarousel, IssueCategoryCard },
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,

    slickOptions: {
      slidesToShow: 1,
      slidesToScroll: 1,
      speed: 400,
      autoplay: true,
      autoplaySpeed: 3000,
      responsive: [
        { breakpoint: 1600, settings: { slidesToShow: 3, slidesToScroll: 3 } },
        { breakpoint: 1200, settings: { slidesToShow: 2, slidesToScroll: 2 } },
        { breakpoint: 750, settings: { slidesToShow: 1, slidesToScroll: 1 } },
      ],
    },

    items: {},
  }),

  watch: {
    date: function() {
      this.getIssue();
    },
  },

  methods: {
    getIssue() {
      // ENTERTAINMENT | IT_SCIENCE | WORLD | ECONOMY | SPORTS | POLITICS | SOCIETY/LIVING
      let cate = [
        "ENTERTAINMENT",
        "IT_SCIENCE",
        "WORLD",
        "ECONOMY",
        "SPORTS",
        "POLITICS",
        "SOCIETY/LIVING",
      ];

      for (let i = 0; i < 7; i++) {
        this.$store.dispatch("issueStore/issueCategory", {
          category: cate[i],
          date: this.date,
        });
      }
    },
  },

  created() {
    this.getIssue();
  },
};
</script>

<style>
#carousel .slick-list {
  border-radius: 12px;
  overflow: hidden;
}
</style>
