<template>
  <v-container>
    <v-sheet height="10vh"></v-sheet>
    <v-row>
      <!-- 옆 사이드 -->
      <v-col cols="auto" class="mr-auto" sm="3">
        <div class="mt-5">
          <v-list flat>
            <h3 class="ml-1">"{{getCategory()}}"에 대한 이슈</h3>
            <v-divider class="my-2"></v-divider>

            <v-list-item-group v-model="selectedItem" color="primary">
              <v-list-item v-for="(item, i) in items" :key="i">
                <v-list-item-content>
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                  <v-divider class="my-2"></v-divider>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
      </v-col>

      <!-- 본문 -->
      <v-col id="opinion_main">
        <v-row class="ml-1">
          <v-col cols="auto" class="mr-auto">
            <span class="display-1">블랙핑크지수 연관 키워드</span>
          </v-col>
          <v-col cols="auto"><span style="color: #BDBDBD">기간: 2020-10-13</span></v-col>
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
          <div v-if="categoryType == 'news'">
            <v-col><issue-detail-news /></v-col>
          </div>
          <div v-if="categoryType == 'youtube'">
            <v-col><issue-detail-youtube /></v-col>
          </div>
        </v-row>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>
  </v-container>
</template>

<script>
import IssueDetailNews from '../../components/Issue/IssueDetailNews.vue';
import IssueDetailYoutube from '../../components/Issue/IssueDetailYoutube.vue';

export default {
  components: { IssueDetailNews, IssueDetailYoutube },
  computed: {
    
  },
  data: () => ({
    selectedItem: 1,
    categoryType: 'news',
    items: [{ text: 'Real-Time' }, { text: 'Audience' }, { text: 'Conversions' }],
  }),
  watch: {},
  methods: {
    SelectCategory(type) {
      this.categoryType = type;
    },
    getCategory(check) {
      let ob = '';
      switch (check) {
        case "ENTERTAINMENT":
          ob = '연예';
          break;
        case "IT_SCIENCE":
          ob = 'IT/과학';
          break;
        case "WORLD":
          ob = '해외';
          break;
        case "ECONOMY":
          ob = '경제';
          break;
        case "SPORTS":
          ob = '스포츠';
          break;
        case "POLITICS":
          ob = '정치';
          break;
        case "SOCIETY/LIVING":
          ob = '사회/생활';
          break;
      }
      return ob;
    },

  },
  created() {
  },
};
</script>

<style scoped></style>
