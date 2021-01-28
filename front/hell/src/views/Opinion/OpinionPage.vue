<template>
    <v-container>
      <h2 class='text-center mr-tp mr-bt'>의견나눔</h2>
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
                  color = purple
                  solo-inverted
                  hide-details
                  text-field-filled-margin-top ="100px"
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
              <v-row class="mr-tp mr-le" style="padding-top:20px">
                <v-btn class="" outlined>전체</v-btn>
                <v-btn class="" outlined>연예</v-btn>
                <v-btn class="" outlined>IT/과학</v-btn>
                <v-btn class="" outlined>해외</v-btn>
                <v-btn class="" outlined>경제</v-btn>
                <v-btn class="" outlined>스포츠</v-btn>
                <v-btn class="" outlined>정치</v-btn>
                <v-btn class="" outlined>사회</v-btn>
                <v-btn class="" outlined>생활</v-btn>
              </v-row>
              
              <!-- 보여주기 형태 -->
              <v-row class="mr-tp">
                <v-col cols="auto" class="mr-auto"></v-col>
                <v-col cols="auto">
                  <v-btn class="btnLC" icon @click="ChageType('list')"><v-icon>mdi-format-list-bulleted</v-icon></v-btn>
                  <v-btn class="btnLC" icon @click="ChageType('card')"><v-icon>mdi-view-grid</v-icon></v-btn>
                </v-col>
              </v-row>

              <!-- 내용 -->
              <v-row class="mr-tp">
                  <v-col v-if=" viewType =='list' "><opinion-table/></v-col>
                  <v-col v-if=" viewType =='card' "><card-list v-for="item in items" :key="item.tab"/> </v-col>
              </v-row>

              <v-row>
                <v-col cols="auto" class="mr-auto"></v-col>
                <v-col cols="auto">
                  <v-btn class="btnLC" color="blue" @click="MovePage('write')">글쓰기</v-btn>
                </v-col>
              </v-row>

              <!-- paging -->
              <div class="text-center">
                <v-pagination
                  v-model="page"
                  :length="pageCnt"
                  circle
                ></v-pagination>
              </div>
          </v-col>

          <v-col cols="2">
            <v-sheet rounded="lg" id="opinion_side" class="sticky">
              <side-list name='인기 많은순'></side-list>
              <v-divider class="my-2"></v-divider>
              <side-list name='댓글 많은순'></side-list>
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
export default {
  components : {SideList, OpinionTable, CardList},
  data: function() {
    return {
      search : 'dd',
      viewType: 'card',
      page: 1,
      pageCnt : 3,
      items: [
          { tab: '',},
          { tab: '',},
          { tab: '',},
          { tab: '',},
          { tab: '',},
          { tab: '',},
          { tab: '',},
          { tab: '',},
          { tab: '',},
          { tab: '',},
        ],
    };
  },
  methods:{
    ChageType(type) {
      this.viewType = type;
    },
    MovePage : function(check){
        switch(check){
          case 'write' : this.$router.push({ name: 'OpinionWrite' }); break;
        }
    }
  },
}
</script>

<style lang="scss" scoped>
#opinion_main{
  margin-top: 20px;
  margin-right: 10px;
  border-right: 1px solid rgb(238, 238, 238);
  padding-right :20px;
  padding-top :20px;
}

#opinion_main_content{
  margin-top:100px;
}

.btnLC{
<<<<<<< HEAD
  margin-top:20px;
=======
>>>>>>> 60c2a4dd377f80bfee33da3be9e47e1d81878210
  border: 1px solid rgb(238, 238, 238);
}

// .sticky {
//   display: inline-block;
//   position: sticky;
//   background: blue;
// }
</style>