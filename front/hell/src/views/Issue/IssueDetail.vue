<template>
  <v-container>
    <v-sheet height="10vh"></v-sheet>
    <v-row>
      <!-- 옆 사이드 -->
      <v-col cols="auto" class="mr-auto" sm="3">
        <div class="mt-5">
          <v-list flat>
            <span class="ml-1 text-xl">"{{ changeNameCategory(category) }}"에 대한 이슈</span>
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
                <v-list-item
                  v-for="(item, index) in categoryKorean"
                  :key="index"
                  @click="changeCategory(index)"
                >
                  <v-list-item-title>{{ item }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <v-divider class="my-2"></v-divider>

            <v-list-item-group v-model="selectedItem" color="primary">
              <v-list-item
                elevation="2"
                v-for="(item, i) in categoryItems"
                :key="i"
                @click="search(item.content)"
              >
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
      <v-col>
        <v-row class="ml-1">
          <v-col cols="auto" class="mr-auto">
            <span class="display-1">"{{ issue }}" 검색</span>
          </v-col>
          <v-col cols="auto"
            ><span style="color: #bdbdbd; fontSize: 13px;">날짜: {{ date }}</span>
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
              <v-date-picker
                v-model="datePicker"
                @input="menu2 = false"
                :events="changeDate()"
              ></v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
        <div class="mt-5">
          <v-tabs background-color="" class="my-2 ml-5">
            <v-tab @click="SelectCategory('news')">뉴스</v-tab>
            <v-tab @click="SelectCategory('youtube')">유튜브</v-tab>
          </v-tabs>
        </div>
        <v-divider class="ml-5"></v-divider>

        <v-row class="mt-5">
          <v-col cols="auto" class="mr-auto"></v-col>
          <v-col cols="auto">
            <div style="width:130px;">
              <v-select
                outlined
                :items="selectItem"
                label="유사도순"
                v-model="selectNews"
                dense
                solo
              ></v-select>
            </div>
          </v-col>
        </v-row>
        <!-- 카테고리 별로 보여주는 곳 -->
        <!-- 뉴스 내용 -->
        <div v-if="categoryType == 'news'">
          <!-- Select 박스 부분 -->

          <div style="clear:both;"></div>

          <!-- 뉴스 리스트 부분 -->
          <v-list two-line>
            <div class="text-center" v-if="newsData.length ==0"><span>뉴스 자료가 없네요...</span></div>
            <issue-news-list v-for="(item, index) in newsData" :key="index" :data="item" />
          </v-list>
        </div>

        <!-- 유튜브 내용 -->
        <div v-if="categoryType == 'youtube'">
          <div style="clear:both;"></div>

          <!-- 유튜브 리스트 부분 -->
          <v-list two-line>
            <div class="text-center" v-if="youtuData.length ==0"><span>유튜브 자료가 없네요...</span></div>
            <issue-youtube-list v-for="(item, index) in youtuData" :key="index" :data="item" />
          </v-list>
        </div>
      </v-col>
    </v-row>
    <!-- 로딩 -->
    <v-overlay :z-index="0" :value="overlay">
      <div style="text-align: center">
        <div>
          어머! 최초로 누르셨네요! 불러오는 중...
          <v-img src="https://i.ibb.co/hRsHwmt/image.gif" />
        </div>
        <div>
          <v-progress-circular class="mt-5" indeterminate size="64"></v-progress-circular>
        </div>
        <v-btn class="mt-5" color="orange lighten-2" @click="overlay = false">
          로딩 나가기
        </v-btn>
      </div>
    </v-overlay>
  </v-container>
</template>

<script>
import Axios from 'axios';
import { API_BASE_URL } from '../../config';
import { mapActions, mapState } from 'vuex';
import IssueNewsList from '../../components/Issue/IssueNewsList.vue';
import IssueYoutubeList from '../../components/Issue/IssueYoutubeList.vue';

export default {
  components: { IssueNewsList, IssueYoutubeList },
  computed: {
    ...mapState('issueStore', [
      'issueDetail',
      'issueEntertainment',
      'issueITScience',
      'issueWorld',
      'issueEconomy',
      'issueSports',
      'issuePolitics',
      'issueSociety',
    ]),
  },
  data: () => ({
    selectedItem: 0,
    categoryType: 'news',
    ob: '',

    category: '',
    issue: '',
    date: '',

    datePicker: '',

    menu1: false,
    menu2: false,

    categoryItems: {},

    categoryKorean: ['연예', '스포츠', '해외', 'IT/과학', '경제', '정치', '사회/생활'],
    categoryEnglish: [
      'ENTERTAINMENT',
      'SPORTS',
      'WORLD',
      'IT_SCIENCE',
      'ECONOMY',
      'POLITICS',
      'SOCIETY/LIVING',
    ],
    // 로딩창
    overlay: false,
    //-----------------------뉴스 태그용
    newsCurPage: 0,
    newsPageCnt: 0,
    sort: 'sim',
    newsData: [],
    selectItem: ['유사도순', '최신순'],
    selectNews: '',
    newsComplete: true,

    //-----------------------유튜브 태그용
    order: 'relevance',
    youtuData: [],
    youtubeCurPage: 0,
    selectYoutu: '',
    youtubuComplete: true,
  }),

  watch: {
    selectNews: function() {
      this.changeSelect();
    },

    // 유튜브 태그
    selectYoutu: function() {
      this.changeSelect();
    },
  },

  methods: {
    ...mapActions('issueStore', ['issueCategory']),
    SelectCategory(type) {
      window.scrollTo(0, 0);
      if (type == 'news' && this.newsCurPage == 0) this.newsAixos();
      else if (type == 'youtube' && this.youtubeCurPage == 0) this.youtubeAixos();

      this.categoryType = type;
    },

    changeDate() {
      if (this.date == this.datePicker) return;
      window.scrollTo(0, 0);
      this.selectedItem = 0;
      this.newsData = [];
      this.newsCurPage = 0;
      this.youtuData = [];
      this.youtubeCurPage = 0;
      this.date = this.datePicker;
      this.issueAixos(this.category, this.date);
    },

    changeCategory(no) {
      window.scrollTo(0, 0);
      this.selectedItem = 0;
      this.menu1 = false;
      this.category = this.categoryEnglish[no];
      this.newsData = [];
      this.newsCurPage = 0;
      this.youtuData = [];
      this.youtubeCurPage = 0;
      this.issueAixos(this.category, this.date);
    },

    search(issue) {
      window.scrollTo(0, 0);
      this.newsData = [];
      this.newsCurPage = 0;
      this.youtuData = [];
      this.youtubeCurPage = 0;
      this.issue = issue;
      if (this.categoryType == 'news') this.newsAixos();
      else this.youtubeAixos();
    },

    changeSelect() {
      window.scrollTo(0, 0);
      this.newsData = [];
      this.newsCurPage = 0;
      this.youtuData = [];
      this.youtubeCurPage = 0;

      if (this.categoryType == 'news' && this.selectNews == '유사도순') this.sort = 'sim';
      else if (this.categoryType == 'youtube' && this.selectNews == '유사도순')
        this.order = 'relevance';
      else this.sort = 'date';

      if (this.categoryType == 'news') this.newsAixos();
      else if (this.categoryType == 'youtube') this.youtubeAixos();
    },

    changeNameCategory(check) {
      let ob = null;
      switch (check) {
        case 'ENTERTAINMENT':
          ob = '연예';
          break;
        case 'IT_SCIENCE':
          ob = 'IT/과학';
          break;
        case 'WORLD':
          ob = '해외';
          break;
        case 'ECONOMY':
          ob = '경제';
          break;
        case 'SPORTS':
          ob = '스포츠';
          break;
        case 'POLITICS':
          ob = '정치';
          break;
        case 'SOCIETY/LIVING':
          ob = '사회/생활';
          break;
      }
      return ob;
    },

    getObject(check) {
      let ob = null;
      switch (check) {
        case '연예':
        case 'ENTERTAINMENT':
          ob = this.issueEntertainment;
          break;
        case 'IT/과학':
        case 'IT_SCIENCE':
          ob = this.issueITScience;
          break;
        case '해외':
        case 'WORLD':
          ob = this.issueWorld;
          break;
        case '경제':
        case 'ECONOMY':
          ob = this.issueEconomy;
          break;
        case '스포츠':
        case 'SPORTS':
          ob = this.issueSports;
          break;
        case '정치':
        case 'POLITICS':
          ob = this.issuePolitics;
          break;
        case '사회/생활':
        case 'SOCIETY/LIVING':
          ob = this.issueSociety;
          break;
      }
      return ob;
    },

    onScroll() {
      if (
        window.scrollY + document.documentElement.clientHeight >
          document.documentElement.scrollHeight - 10 &&
        this.overlay == false
      ) {
        window.scrollTo(0, document.documentElement.scrollHeight - 70);
        if (this.categoryType == 'news' && this.newsComplete) this.newsAixos();
        if (this.categoryType == 'youtube' && this.youtubuComplete) this.youtubeAixos();
      }
    },

    async issueAixos(category, date) {
      await Axios.post(`${API_BASE_URL}issue/`, { category: category, date: date })
        .then((res) => {
          this.category = res.data[0].category;
          this.date = res.data[0].date;
          this.datePicker = res.data[0].date;
          if (this.issue != '') this.issue = res.data[0].content;
          else this.issue = res.data[this.selectedItem].content;
          this.categoryItems = res.data;
          console.log(this.categoryType);
          if (this.categoryType == 'news') this.newsAixos();
          else this.youtubeAixos();
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    async newsAixos() {
      this.overlay = true;
      this.newsComplete = false;
      await Axios.post(`${API_BASE_URL}issue/issue_search/news/`, {
        sort: this.sort,
        content: this.issue,
        start: this.newsCurPage * 10 + 1,
      })
        .then((res) => {
          for (let i = 1; i < res.data.news.length; i++) {
            this.newsData[this.newsData.length] = res.data.news[i];
          }
          console.log('뉴스데이터vv');
          console.log(res.data.news);
          //페이징 값
          this.newsPageCnt = Math.floor(res.data.news[0].total / 10);

          if (this.newsPageCnt == this.newsCurPage) {
            console.log('완료');
          }
          this.newsCurPage = this.newsCurPage + 1;

          this.overlay = false;
          this.newsComplete = true;
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    async youtubeAixos() {
      this.overlay = true;
      this.youtubeComplete = false;
      await Axios.post(`${API_BASE_URL}issue/issue_search/youtube/`, {
        order: this.order,
        content: this.issue,
        start: this.youtubeCurPage * 10 + 1,
      })
        .then((res) => {
          for (let i = 1; i < res.data.youtube.length; i++) {
            this.youtuData[this.youtuData.length] = res.data.youtube[i];
          }

          console.log('유튜브데이터vv');
          console.log(res.data.youtube);
          this.youtubeCurPage = this.youtubeCurPage + 1;

          this.overlay = false;
          this.youtubeComplete = true;
        })
        .catch((err) => {
          console.log('에러');
          console.log(err.response);
        });
    },
  },
  // 무한스크롤
  mounted() {
    window.addEventListener('scroll', this.onScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll);
  },
  //---- 무한스크롤

  created() {
    this.selectedItem = Number(this.$route.query.no);
    window.scrollTo(0, 0);
    this.issueAixos(this.$route.query.category, this.$route.query.date);
  },
};
</script>

<style>
.cate-select {
  border-radius: 10px;
  border: 1px solid black;
  box-shadow: 1px 1px 1px 1px gray;
}
</style>
