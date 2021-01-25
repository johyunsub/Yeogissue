<template>
    <v-container>
        <v-row>
          <v-col cols="1"></v-col>
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
              
              <v-row class="mr-tp">
                <v-col cols="auto" class="mr-auto"></v-col>
                <v-col cols="auto">
                  <v-btn class="btnLC" icon @click="ChageType('card')"><v-icon>mdi-format-list-bulleted</v-icon></v-btn>
                  <v-btn class="btnLC" icon @click="ChageType('list')"><v-icon>mdi-view-grid</v-icon></v-btn>
                </v-col>
              </v-row>

              <!-- 내용 -->
              <v-row class="mr-tp">
                  <v-col v-if=" viewType =='card' "><opinion-table/></v-col>
                  <v-col v-if=" viewType =='list' ">1 </v-col>
              </v-row>

              <v-row>
                <v-col cols="auto" class="mr-auto"></v-col>
                <v-col cols="auto">
                  <v-btn class="btnLC" color="blue" @click="ChageType()">글쓰기</v-btn>
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

          <v-col cols="2" >
            <v-sheet rounded="lg" id="opinion_side">
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
import OpinionTable from '../../components/Opinion/OpinionTable.vue';
import SideList from '../../components/Opinion/SideList.vue';
export default {
  components : {SideList, OpinionTable},
  data: function() {
    return {
      search : 'dd',
      viewType: 'card',
      page: 1,
      pageCnt : 3,
    };
  },
  methods:{
    ChageType(type) {
      this.viewType = type;
      console.log(type);
    },
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
  margin-top:20px;
  border: 1px solid rgb(238, 238, 238);
}
</style>