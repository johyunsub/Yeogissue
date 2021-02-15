<template>

  <v-container>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col id="opinion_main">
        <v-sheet lighten-5>
       
        </v-sheet>
        <!-- 카테고리 -->
        <!-- <opinion-category /> -->

        <!-- 내용 -->
        <v-row class="mr-tp">
          <v-col v-if="viewType == 'list'"><opinion-table /></v-col>
          <v-col v-if="viewType == 'card'"
            >
            <v-list two-line>
            <card-list
              v-for="(item, index) in opinionPaging"
              :key="`${index}_items`"
              :data="item"
            />
            </v-list>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="auto" class="mr-auto"></v-col>
          <v-col cols="auto">
                <!-- <v-btn class="ma-2 btnLC" outlined large fab color="indigo"  @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn> -->
           <v-btn class="btnLC" color="blue" rounded @click="MovePage('write')"> <v-icon color="white">mdi-pencil</v-icon>
           <span style="color: white;"> 글쓰기 </span></v-btn>
          </v-col>
        </v-row>

        <!-- paging -->
        <div class="text-center">
          <v-pagination v-model="page" :length="pagingCnt" circle></v-pagination>
        </div>
      </v-col>

      <!-- <v-col cols="2">
        <v-sheet rounded="lg" id="opinion_side" class="sticky">
          <side-list name="인기 많은순"></side-list>
          <v-divider class="my-2"></v-divider>
          <side-list name="댓글 많은순"></side-list>
        </v-sheet>
      </v-col> -->
      <div style="float: right;">
      <v-col cols="1"></v-col>
      <v-btn class="ma-2 btnLC v-btn--example" bottom right outlined large fab color="indigo" @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn>
      </div>
    </v-row>
  </v-container>
</template>

<script>
import CardList from '../../components/Opinion/CardList.vue';
import OpinionTable from '../../components/Opinion/OpinionTable.vue';
// import SideList from '../../components/Opinion/SideList.vue';
import { mapState, mapActions } from 'vuex';
// import OpinionCategory from '../../components/Opinion/OpinionCategory.vue';

export default {
  components: { OpinionTable, CardList },
  computed: {
    ...mapState('opinionStore', ['opinionPaging', 'pagingCnt','top_hashtags']),
  },
  data: function() {
    return {
      checkbox: true,
      cateBtn: 'center',
      search: '',
      viewType: 'card',
      page: 1,
    };
  },
  watch: {
    page: function(newVal) {
      this.$store.commit('opinionStore/SET_OPINION_PAGING', (newVal - 1) * 10);
    },
  },
  methods: {
    ...mapActions('opinionStore', ['opinionList', 'opinionDetail','hashOpinionList','hash_top10']),
    ChageType(type) {
      this.viewType = type;
    },
    MovePage: function(check) {
      switch (check) {
        case 'write':
          this.$router.push(`/opinionWrite?type=write`);
          break;
      }
    },
    search_hashtag() {
      this.hashOpinionList({name:this.search});
    },
    gotoList() {
      this.opinionList();
    },
    hashtagClick(hash) {
      this.hashOpinionList({name:hash})
      this.search = hash
    }
  },
  created() {
    this.opinionList();
    this.hash_top10();
  },
};
</script>

<style lang="scss">
#opinion_main {
  margin-top: 20px;
  margin-right: 10px;
  // border-right: 1px solid rgb(238, 238, 238);
  padding-right: 20px;
  padding-top: 5px;
}

#opinion_main_content {
  margin-top: 100px;
}

.btnLC {
  margin-top: 20px;
  border: 1px solid rgb(238, 238, 238);
}

// .sticky {
//   display: inline-block;
//   position: sticky;
//   background: blue;
// }

// .scroll-downs {
//   position: absolute;
// }

.v-btn--example {
    bottom: 0;
    position:fixed;
    margin: 0 0 16px 16px;
    right: 100;
  }
</style>
