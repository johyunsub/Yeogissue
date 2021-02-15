<template>
  <div>
    <v-card class="mx-auto my-5 ml-5 elevation-5" style="border-radius: 15px;" max-width="400" :elevation="2">
      <!-- 글짜 ... 해주는거 text-truncate -->
      <v-card-title class="headline pl-6 h6" style="background-color: #765D5D;">
        <span class="ma-auto" style="color: #FAEAD4;">
          <i v-if="category=='정치'" class="fas fa-landmark"></i>
          <i v-else-if="category=='해외'" class="fas fa-globe"></i>
          <i v-else-if="category=='사회/생활'" class="fas fa-users"></i>
          <i v-else-if="category=='스포츠'" class="fas fa-running"></i>
          <i v-else-if="category=='경제'" class="fas fa-comment-dollar"></i>
          <i v-else-if="category=='IT/과학'" class="fas fa-flask"></i>
          <i v-else-if="category=='연예'" class="fas fa-crown"></i>
           <span class="ml-3">{{ category }}</span>
           
          </span>
      </v-card-title>

      <v-card-text class="mt-4">
        <div v-for="(item, n) in getCategory(category)" :key="item.id" @mouseout="stp(item, n + 1)">
          <div
            :class="
              'text-ellipsis issue-span mt-5 choice_cursor ' +
                (item.category + (n + 1)).replace('/', '')
            "
            @mouseover="moveMarquee(item, n + 1)"
            @click="Movepage(item, n)"
          >
            <span class="issue-number">{{ n + 1 }}</span>
            <span class="ml-4">{{ item.content }}</span>
          </div>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import $ from 'jquery';

export default {
  props: {
    category: { type: String },
    date: { type: String },
  },
  computed: {
    ...mapState('issueStore', [
      'issueEntertainment',
      'issueITScience',
      'issueWorld',
      'issueEconomy',
      'issueSports',
      'issuePolitics',
      'issueSociety',
    ]),
  },
  data() {
    return {
      issueData: {
        date: this.date,
        category: this.category,
        content: '',
      },
      flag: false,
    };
  },
  methods: {
    getCategory(check) {
      let ob = null;
      switch (check) {
        case '연예':
          ob = this.issueEntertainment;
          break;
        case 'IT/과학':
          ob = this.issueITScience;
          break;
        case '해외':
          ob = this.issueWorld;
          break;
        case '경제':
          ob = this.issueEconomy;
          break;
        case '스포츠':
          ob = this.issueSports;
          break;
        case '정치':
          ob = this.issuePolitics;
          break;
        case '사회/생활':
          ob = this.issueSociety;
          break;
      }
      return ob;
    },

    Movepage(item, no) {
      this.$router.push(`/issueDetail?category=${item.category}&date=${item.date}&no=${no}`);
    },

    moveMarquee(item, number) {
      if (this.flag == true) return;

      let str = 'div.' + item.category + number;
      str = str.replace('/', '');
      // console.log(str);
      // <marquee direction="right" scrolldelay="100">${number}.&nbsp;${item.content}</marquee>
      $(str).html(
        `<marquee direction="left" scrolldelay="100" scrollamount="15">${item.content}</marquee>`
      );
      this.flag = true;
    },

    stp(item, number) {
      this.flag = false;
      let str = 'div.' + item.category + number;
      str = str.replace('/', '');
      // console.log("아웃" + str);
      $(str).html(
        `<span class="issue-number">${number}</span> <span class="ml-4">${item.content}</span>`
      );
    },
  },

  created() {},
};
</script>

<style>
.issue-span:hover {
  background-color: #FAEAD4;
  border-radius: 20px 20px 20px 20px;
  padding: 4px;
}

.issue-number {
  color: #6B5A4F;
}
</style>
