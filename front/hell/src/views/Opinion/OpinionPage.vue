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
            v-model="search"
            label="Search KeyWord"
            flat
            color="purple"
            solo-inverted
            hide-details
            text-field-filled-margin-top="100px"
            clearable
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
        <v-row class="mr-tp mr-le" style="padding-top: 20px">
          <v-btn class="" outlined @click="categoryChange('전체')">전체</v-btn>
          <v-btn class="" outlined @click="categoryChange('연예')">연예</v-btn>
          <v-btn class="" outlined @click="categoryChange('IT/과학')">IT/과학</v-btn>
          <v-btn class="" outlined @click="categoryChange('해외')">해외</v-btn>
          <v-btn class="" outlined @click="categoryChange('경제')">경제</v-btn>
          <v-btn class="" outlined @click="categoryChange('스포츠')">스포츠</v-btn>
          <v-btn class="" outlined @click="categoryChange('정치')">정치</v-btn>
          <v-btn class="" outlined @click="categoryChange('사회')">사회</v-btn>
          <v-btn class="" outlined @click="categoryChange('생활')">생활</v-btn>
        </v-row>

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
            ><card-list
              v-for="(item, index) in opinionPaging"
              :key="`${index}_items`"
              :id="item.id"
              :title="item.title"
              :user="item.user"
            />
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="auto" class="mr-auto"></v-col>
          <v-col cols="auto">
            <v-btn class="btnLC" color="blue" @click="MovePage('write')">글쓰기</v-btn>
          </v-col>
        </v-row>

        <!-- paging -->
        <div class="text-center">
          <v-pagination v-model="page" :length="pagingCnt" circle></v-pagination>
        </div>
      </v-col>

      <v-col cols="2">
        <v-sheet rounded="lg" id="opinion_side" class="sticky">
          <side-list name="인기 많은순"></side-list>
          <v-divider class="my-2"></v-divider>
          <side-list name="댓글 많은순"></side-list>
        </v-sheet>
      </v-col>

      <v-col cols="1"></v-col>
    </v-row>
  </v-container>
</template>

<script>
import CardList from '../../components/Opinion/CardList.vue';
import OpinionTable from '../../components/Opinion/OpinionTable.vue';
import SideList from '../../components/Opinion/SideList.vue';
import { mapState, mapActions } from 'vuex';

export default {
  components: { SideList, OpinionTable, CardList },
  computed: {
    ...mapState('opinionStore', ['opinionPaging', 'pagingCnt']),
  },
  data: function() {
    return {
      search: 'dd',
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
    ...mapActions('opinionStore', ['opinionList', 'opinionCategorySelelct']),
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
    categoryChange: function(change) {
      this.opinionCategorySelelct(change);
    },
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
  border-right: 1px solid rgb(238, 238, 238);
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
</style>
