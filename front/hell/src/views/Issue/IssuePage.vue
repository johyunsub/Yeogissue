<template>
    <v-container>
      <v-row class="mr-tp">
        <v-col cols="2"></v-col>
        <v-col>
          <v-row class="mr-tp">
            <issue-category/>
            <v-date-picker
              v-model="picker"
              year-icon="mdi-calendar-blank"
              prev-icon="mdi-skip-previous"
              next-icon="mdi-skip-next"
            ></v-date-picker>
          </v-row>

          <!-- 뉴스 테이블 -->
          <p class="display-1 mr-tp">뉴스 목록</p>
          <v-row class="mr-tp">
            <news-table/>
          </v-row>

          <!-- 유투브 테이블 -->
          <p class="display-1 mr-tp">유투브 목록</p>
          <v-row class="mr-tp">
            <youtube-table/>
          </v-row>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>
  </v-container>
</template>

<script>
import IssueCategory from '../../components/Issue/IssueCategory.vue';
import NewsTable from '../../components/Issue/NewsTable.vue';
import YoutubeTable from '../../components/Issue/YoutubeTable.vue';

export default {
  components : { IssueCategory, NewsTable, YoutubeTable },
  data () {
      return {
        picker: new Date().toISOString().substr(0, 10),
      }
    },
}
</script>
