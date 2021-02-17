<template>
  <v-row class="justify-center">
    <div class="opinion-image">
        <div style="height:450px"></div>
        <div style="width:65%; float:right">
      </div>
      </div>
<div style="clear:both;"></div>

    
    <v-sheet class="px-12" height="100" width="100%" color="white"></v-sheet>

    <div class="ma-auto mt-10" style="width: 80%">
      <!-- <v-row>
      <v-col cols="1"></v-col>
      <v-col id="opinion_main"> -->
        <!-- 검색 -->
        <v-row>
          <v-col cols="3" class="mr-auto"></v-col>
           <v-text-field
            @keypress.enter='search_hashtag'
            v-model="search"
            label="다른 사람의 의견이 궁금한 주제를 검색해보세요!"
            prepend-inner-icon="fas fa-hashtag"
            single-line
            rounded
            outlined
            color="purple"
            clearable
            @click:clear="gotoList"
            clear-icon="mdi-close-circle-outline"
            flat
            text-field-filled-margin-top="100px"
          ></v-text-field>
          <v-col cols="2" class="mr-auto"></v-col>
        </v-row>
        <v-row>
          <v-col cols="3" class="mr-auto"></v-col>
          <span class="mr-2 mt-1">인기 검색어 :</span>
        <v-chip v-for="tag in top_hashtags" :key="tag.name" @click='hashtagClick(tag.name)' medium outlined class="justify-center mr-3"> 
          <span  style="color: black; font-weight: 600">
              <v-icon small color="pink">fas fa-hashtag</v-icon>
              {{ tag.name }}</span
            >
        </v-chip>
      <v-col cols="2" class="mr-auto"></v-col>
        </v-row>

        <v-sheet class="px-12" height="100" width="100%" color="white"></v-sheet>

       
        <!-- 카테고리 -->
        <opinion-category />

        <div class="mt-15"></div>
 
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
              @search="hashtagClick"
            />
          </v-list>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="auto" class="mr-auto"></v-col>
        <v-col cols="auto">
          <!-- <v-btn class="ma-2 btnLC" outlined large fab color="indigo"  @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn> -->
          <v-btn class="btnLC" color="blue" rounded @click="MovePage('write')">
            <v-icon color="white">mdi-pencil</v-icon>
            <span style="color: white;"> 글쓰기 </span></v-btn
          >
        </v-col>
      </v-row>

      <!-- paging -->
      <div class="text-center">
        <v-pagination v-model="page" :length="pagingCnt" circle></v-pagination>
      </div>
      <!-- </v-col> -->

      <!-- <v-col cols="2">
        <v-sheet rounded="lg" id="opinion_side" class="sticky">
          <side-list name="인기 많은순"></side-list>
          <v-divider class="my-2"></v-divider>
          <side-list name="댓글 많은순"></side-list>
        </v-sheet>
      </v-col> -->
      <div style="float: right;">
        <v-col cols="1"></v-col>
        <v-btn
          class="ma-2 ml-10 btnLC v-btn--example"
          bottom
          right
          outlined
          large
          fab
          color="indigo"
          @click="MovePage('write')"
        >
          <v-icon>mdi-pencil</v-icon></v-btn
        >
      </div>
      <!-- </v-row> -->
    </div>
  </v-row>
</template>

<script>
import CardList from '../../components/Opinion/CardList.vue';
// import SideList from '../../components/Opinion/SideList.vue';
import { mapState, mapActions } from 'vuex';
import OpinionCategory from '../../components/Opinion/OpinionCategory.vue';

export default {
  components: { CardList, OpinionCategory },
  computed: {
    ...mapState('opinionStore', ['opinionPaging', 'pagingCnt', 'top_hashtags']),
  },
  data: function() {
    return {
      checkbox: true,
      cateBtn: 'center',
      search: '',
      viewType: 'card',
      page: 1,
      selectedItem: 1,
    };
  },
  watch: {
    page: function(newVal) {
      this.$store.commit('opinionStore/SET_OPINION_PAGING', (newVal - 1) * 10);
    },
  },
  methods: {
    ...mapActions('opinionStore', [
      'opinionList',
      'opinionDetail',
      'hashOpinionList',
      'hash_top10',
    ]),
    ChageType(type) {
      this.viewType = type;
    },
    MovePage: function(check) {
      switch (check) {
        case 'write':
          this.$router.push(`/opinionWrite?type=write&club_pk=0`);
          break;
      }
    },
    search_hashtag() {
      this.hashOpinionList({ name: this.search });
    },
    gotoList() {
      this.opinionList();
    },
    hashtagClick(hash) {
      this.hashOpinionList({ name: hash });
      this.search = hash;
    },
  },
  created() {
    window.scrollTo(0,0);
    this.hash_top10();
    if (this.$route.query.search != undefined) {
      this.search = this.$route.query.search;
      this.hashOpinionList({ name: this.search });
    } else {
      this.opinionList();
    }
  },
};
</script>

<style lang="scss">
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

.v-btn--example {
  bottom: 0;
  position: fixed;
  margin: 0 0 16px 16px;
  right: 100;
}
.opinion-image{
  width:100%;
  height: 600px;
  background-image: url("../../assets/의견 이슈.png");
  background-size: 100% 600px;
}
</style>
