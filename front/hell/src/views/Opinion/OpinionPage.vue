<template>
  <v-row class="justify-center">
    <v-sheet height="500" width="100%" color="">
        <v-row class="mt-16">
      <v-col cols="1"></v-col>
      <h2 class="text-left mr-tp mr-bt">의견이슈</h2> 
      </v-row>
        <v-row class="mb-16">
      <v-col cols="1"></v-col>
      <h3 class="text-left mr-tp mr-bt">다양한 이슈와 생각이 가득한 곳! 여러분만의 의견을 공유하고, 다른 사람의 의견을 검색해보세요! </h3>
      </v-row>
       <v-sheet height="250" width="100%" color="deep-purple lighten-5">

    <!-- <marquee behavior=alternate bgcolor="" class="mt-16"> -->
      <v-slide-group
      multiple
      show-arrows
    >
      <v-slide-item v-for="tag in top_hashtags" :key="tag.name" @click='hashtagClick(tag.name)'>
      <v-chip large outlined > 
              <span style="color: black; font-weight: 600">
                  <v-icon small color="pink ">fas fa-hashtag</v-icon>
                  {{ tag.name }}</span
                >
            </v-chip>
            </v-slide-item>
            </v-slide-group>

            <!-- </marquee> -->

    <!-- <v-chip-group column class="mx-auto" max-width="1500">
            <v-chip large outlined v-for="tag in top_hashtags" :key="tag.name" @click='hashtagClick(tag.name)'> 
              <span style="color: black; font-weight: 600">
                  <v-icon small color="pink ">fas fa-hashtag</v-icon>
                  {{ tag.name }}</span
                >
            </v-chip>
          </v-chip-group> -->

     <!-- <v-list rounded>
      <v-subheader>실시간 검색어</v-subheader>
        <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
       <v-list-item v-for="tag in top_hashtags" :key="tag.name" @click='hashtagClick(tag.name)'>
        {{ tag.name }}

         </v-list-item>
      </v-list-item-group> -->
       </v-sheet>
    </v-sheet>

    

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
                <!-- <v-btn class="ma-2 btnLC" outlined large fab color="indigo"  @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn> -->
           <v-btn class="btnLC" color="blue" rounded @click="MovePage('write')"> <v-icon color="white">mdi-pencil</v-icon>
           <span style="color: white;"> 글쓰기 </span></v-btn>
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
      <v-btn class="ma-2 btnLC v-btn--example" bottom right outlined large fab color="indigo" @click="MovePage('write')"> <v-icon>mdi-pencil</v-icon></v-btn>
      </div>
    <!-- </v-row> -->
  </div>
  </v-row>
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
    ...mapState('opinionStore', ['opinionPaging', 'pagingCnt','top_hashtags']),
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
    position:fixed;
    margin: 0 0 16px 16px;
    right: 100;
  }
</style>
