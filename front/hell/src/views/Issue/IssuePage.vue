<template>
  <v-sheet height="140vh" color="#EEEEEE" lighten-5>
    <v-sheet height="15vh" color="#EEEEEE" lighten-5></v-sheet>
    <div class="text-center display-2" style="font-weight: 550">
      <span style="color: red">핫</span>한 트렌드가 궁금할 때
    </div>
    <div class="text-center display-1 mt-6" style="font-weight: 550; color: #42a5f5">
      하루 검색 이슈 랭킹

      <v-tooltip right>
        <template v-slot:activator="{ on, attrs }">
          <v-icon color="primary" v-bind="attrs" v-on="on">
            mdi-alert-circle
          </v-icon>
        </template>
        <span
          >본 검색은 당일 많이 생성된 이슈를 기반으로 합니다. 만약 검색어가 별로 없다면 그날은 해당
          카테고리에 이슈가 적다는 걸 의미합니다.</span
        >
      </v-tooltip>
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
import VueSlickCarousel from 'vue-slick-carousel';
import 'vue-slick-carousel/dist/vue-slick-carousel.css';
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css';
import IssueCategoryCard from '../../components/Issue/IssueCategoryCard.vue';

export default {
  components: { VueSlickCarousel, IssueCategoryCard },
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,

    slickOptions: {
      slidesToShow: 3,
      slidesToScroll: 3,
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
        'SPORTS',
        'ECONOMY',
        'IT_SCIENCE',
        'ENTERTAINMENT',
        'WORLD',
        'POLITICS',
        'SOCIETY/LIVING',
      ];

      for (let i = 0; i < 7; i++) {
        this.$store.dispatch('issueStore/issueCategory', {
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
