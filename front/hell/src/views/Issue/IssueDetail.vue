<template>
  <v-container>
    <v-sheet height="10vh"></v-sheet>
    <v-row>
      <!-- 옆 사이드 -->
      <v-col cols="auto" class="mr-auto" sm="3">
        <div class="mt-5">
          <v-list flat>
            <span class="ml-1 text-xl"
              >"{{ changeNameCategory(category) }}"에 대한 이슈</span
            >
            <v-menu
              v-model="menu1"
              :close-on-content-click="false"
              :nudge-right="40"
              offset-y
              transition="scale-transition"
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon x-small color="primary" fab dark v-bind="attrs" v-on="on">
                  <v-icon>mdi-format-list-bulleted</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item v-for="(item, index) in categoryKorean" :key="index" @click="changeCategory(index)">
                  <v-list-item-title>{{ item }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <v-divider class="my-2"></v-divider>

            <v-list-item-group v-model="selectedItem" color="primary">
              <v-list-item elevation="2" v-for="(item, i) in categoryItems" :key="i">
                <v-list-item-title
                  v-text="item.content"
                  class="border-bt pb-3 pl-3"
                  style="font-size: 90%;"
                ></v-list-item-title>
                <v-divider class="my-2"></v-divider>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
      </v-col>

      <!-- 본문 -->
      <v-col id="opinion_main">
        <v-row class="ml-1">
          <v-col cols="auto" class="mr-auto">
            <span class="display-1">"{{ issue }}" 검색</span>
          </v-col>
          <v-col cols="auto"
            ><span style="color: #bdbdbd">날짜: {{ date }}</span>
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              :nudge-right="40"
              offset-y
              transition="scale-transition"
              left
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon x-small color="primary" fab dark v-bind="attrs" v-on="on">
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </template>
              <v-date-picker v-model="datePicker" @input="menu2 = false" :events="changeDate()"></v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
        <div class="mt-5">
          <v-tabs background-color="" class="my-2 ml-5">
            <v-tab @click="SelectCategory('news')">뉴스</v-tab>
            <v-tab @click="SelectCategory('youtube')">유투브</v-tab>
            <v-tab @click="SelectCategory('twitter')">트위터</v-tab>
          </v-tabs>
        </div>
        <v-divider class="ml-5"></v-divider>

        <!-- 카테고리 별로 보여주는 곳 -->
        <!-- 내용 -->
        <v-row class="mr-tp ml-3">
          <!-- <select><v-select> -->
          <div v-if="categoryType == 'news'">
            <v-col><issue-news-list /></v-col>
          </div>
          <div v-if="categoryType == 'youtube'">
            <v-col><issue-youtube-list /></v-col>
          </div>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Axios from "axios";
import { API_BASE_URL } from "../../config";
import { mapActions, mapState } from "vuex";
import IssueNewsList from "../../components/Issue/IssueNewsList.vue";
import IssueYoutubeList from "../../components/Issue/IssueYoutubeList.vue";

export default {
  components: { IssueNewsList, IssueYoutubeList },
  computed: {
    ...mapState("issueStore", [
      "issueDetail",
      "issueEntertainment",
      "issueITScience",
      "issueWorld",
      "issueEconomy",
      "issueSports",
      "issuePolitics",
      "issueSociety",
    ]),
  },
  data: () => ({
    selectedItem: 1,
    categoryType: "news",
    ob: "",

    category: "",
    issue:"",
    date: "",

    datePicker:"",

    menu1: false,
    menu2: false,

    categoryItems: {},

    categoryKorean: ["연예", "스포츠", "해외", "IT/과학", "경제", "정치", "사회/생활"],
    categoryEnglish: [
      "ENTERTAINMENT",
      "SPORTS",
      "WORLD",
      "IT_SCIENCE",
      "ECONOMY",
      "POLITICS",
      "SOCIETY/LIVING",
    ],

    //-----------------------뉴스 태그용
    newsCurPage: 0,
    newsPageCnt: 0,
    sort: 'sim',

  }),

  methods: {
    ...mapActions("issueStore", ["issueCategory"]),
    SelectCategory(type) {
      this.categoryType = type;
    },

    changeDate(){
      if(this.date == this.datePicker) return;

      this.date = this.datePicker;
      this.issueAixos(this.category, this.date)
    },

    changeCategory(no){
      this.menu1 = false;
      this.category = this.categoryEnglish[no];
      this.issueAixos(this.category, this.date)
    },

    changeNameCategory(check) {
      let ob = null;
      switch (check) {
        case "ENTERTAINMENT":
          ob = "연예";
          break;
        case "IT_SCIENCE":
          ob = "IT/과학";
          break;
        case "WORLD":
          ob = "해외";
          break;
        case "ECONOMY":
          ob = "경제";
          break;
        case "SPORTS":
          ob = "스포츠";
          break;
        case "POLITICS":
          ob = "정치";
          break;
        case "SOCIETY/LIVING":
          ob = "사회/생활";
          break;
      }
      return ob;
    },

    getObject(check) {
      let ob = null;
      switch (check) {
        case "연예":
        case "ENTERTAINMENT":
          ob = this.issueEntertainment;
          break;
        case "IT/과학":
        case "IT_SCIENCE":
          ob = this.issueITScience;
          break;
        case "해외":
        case "WORLD":
          ob = this.issueWorld;
          break;
        case "경제":
        case "ECONOMY":
          ob = this.issueEconomy;
          break;
        case "스포츠":
        case "SPORTS":
          ob = this.issueSports;
          break;
        case "정치":
        case "POLITICS":
          ob = this.issuePolitics;
          break;
        case "사회/생활":
        case "SOCIETY/LIVING":
          ob = this.issueSociety;
          break;
      }
      return ob;
    },

    issueAixos(category, date){
       Axios.post(`${API_BASE_URL}issue/`, {category : category, date: date})
      .then((res) => {
          this.category = res.data[0].category;
          this.date = res.data[0].date;
          this.datePicker = res.data[0].date;
          this.issue = res.data[0].content;
          this.categoryItems = res.data;
      })
      .catch((err) => {
        console.log(err.response);
      });
    },

    newsAixos(){
      Axios.post(`${API_BASE_URL}issue/issue_search/news/`, {sort : this.sort, contnet: this.issue, start: (newsCurPage*10)+1})
      .then((res) => {
          this.category = res.data[0].category;
          this.date = res.data[0].date;
          this.datePicker = res.data[0].date;
          this.issue = res.data[0].content;
          this.categoryItems = res.data;
      })
      .catch((err) => {
        console.log(err.response);
      });
    }
  },
  created() {
    this.issueAixos(this.$route.query.category, this.$route.query.date)
    this.selectedItem = Number(this.$route.query.no);
  },
};
</script>

<style scoped></style>
