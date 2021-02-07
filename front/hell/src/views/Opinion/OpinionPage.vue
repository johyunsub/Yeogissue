<template>
  <v-container>
    <h2 class="text-center mr-tp mr-bt">의견나눔</h2>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col id="opinion_main">
        <!-- 검색 -->
        <v-row>
          <v-col cols="2" class="mr-auto"></v-col>
          <v-text-field
            @keypress.enter='search_hashtag'
            v-model="search"
            label="Search KeyWord"
            flat
            color="purple"
            solo-inverted
            hide-details
            text-field-filled-margin-top="100px"
            clearable
            @click:clear="gotoList"
            clear-icon="mdi-close-circle-outline"
          ></v-text-field>
          <v-col cols="2" class="mr-auto"></v-col>
        </v-row>

        <!-- 해시태그 -->
        <v-row class="mr-tp">
          <v-col cols="2"></v-col>
          #해시태그
          <v-col cols="2" class="mr-auto"></v-col>
        </v-row>

        <!-- 카테고리 -->
        <opinion-category />

        <!-- 보여주기 형태 -->
        <v-row class="mr-tp">
          <v-col cols="auto" class="mr-auto"></v-col>
          <v-col cols="auto">
            <v-btn class="btnLC" icon @click="ChageType('list')"
              ><v-icon>mdi-format-list-bulleted</v-icon></v-btn
            >
            <v-btn class="btnLC" icon @click="ChageType('card')"
              ><v-icon>mdi-view-grid</v-icon></v-btn
            >
          </v-col>
        </v-row>

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
                <v-btn class="ma-2 btnLC" outlined large fab color="indigo"  @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn>
            <!-- <v-icon>mdi-pencil</v-icon> <v-btn class="btnLC" color="blue" @click="MovePage('write')"> 글쓰기</v-btn> -->
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

      <v-col cols="1"></v-col>
      <v-btn class="ma-2 btnLC" outlined large fab color="indigo"  @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn>
    </v-row>
  </v-container>
</template>

<script>
import CardList from '../../components/Opinion/CardList.vue';
import OpinionTable from '../../components/Opinion/OpinionTable.vue';
// import SideList from '../../components/Opinion/SideList.vue';
import { mapState, mapActions } from 'vuex';
import OpinionCategory from '../../components/Opinion/OpinionCategory.vue';

export default {
  components: { OpinionTable, CardList, OpinionCategory },
  computed: {
    ...mapState('opinionStore', ['opinionPaging', 'pagingCnt']),
  },
  data: function() {
    return {
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
    ...mapActions('opinionStore', ['opinionList', 'opinionDetail','hashOpinionList']),
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
    }
  },
  created() {
    this.opinionList();
  },
};
</script>

<style lang="scss" scoped>
#opinion_main {
  margin-top: 20px;
  margin-right: 10px;
  // border-right: 1px solid rgb(238, 238, 238);
  padding-right: 20px;
  padding-top: 20px;
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
</style>
