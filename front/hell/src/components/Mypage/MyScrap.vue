<template>
  <div class="ml-7">
    <p class="text-h4 font-weight-black ml-7">
      나의 스크랩 보관함
      <i class="fas fa-book mx-3"></i>
    </p>
    <hr class="ml-7" width="98%" color="purple" />
    <div class="mt-7"></div>
    <!-- 카테고리 -->
    <!-- <opinion-category /> -->

    <!-- 내용 -->
    <v-row class="mr-tp">
      <v-col v-if="viewType == 'card'">
        <v-list two-line>
          <card-list v-for="(item, index) in opinionData" :key="`${index}_items`" :data="item" />
        </v-list>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import CardList from '../../components/Opinion/CardList.vue';
// import SideList from '../../components/Opinion/SideList.vue';
import { mapState, mapActions } from 'vuex';
import axios from 'axios';
import { API_BASE_URL } from '../../config';
// import OpinionCategory from '../../components/Opinion/OpinionCategory.vue';

export default {
  components: { CardList },
  computed: {
    ...mapState('opinionStore', ['opinionPaging', 'pagingCnt', 'top_hashtags']),
    ...mapState(['userInfo']),
  },
  data: function() {
    return {
      checkbox: true,
      cateBtn: 'center',
      search: '',
      viewType: 'card',
      page: 1,
      id: '',
      opinionData: [],
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

    gotoList() {
      this.opinionList();
    },

    myscrapList() {
      console.log(this.userInfo.id);

      axios
        .get(`${API_BASE_URL}articles/myscrap/${this.userInfo.id}`)
        .then((res) => {
          console.log(res.data);
          this.opinionData = res.data;
        })
        .catch((err) => console.log(err.response));
    },
  },
  created() {
    this.myscrapList();
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
  position: fixed;
  margin: 0 0 16px 16px;
  right: 100;
}
</style>
