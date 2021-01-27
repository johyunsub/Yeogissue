<template>
    <v-container>
        <v-row class="mr-tp">
        <v-col cols="2"></v-col>
        <v-col>
            <p class="blue--text mr-bt">카테고리</p>
            <p class="display-2">제목</p>
            <p class="grey--text">글쓴이, 작성일, 수정, 삭제, 조회수, 북마크</p>
            <v-divider class="my-4"></v-divider>
            
            <p class="text-justify">
                Morbi mattis ullamcorper velit. Donec orci lectus, aliquam ut, faucibus non, euismod id, nulla. Fusce convallis metus id felis luctus adipiscing. Aenean massa. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus.
                Nulla consequat massa quis enim. Praesent venenatis metus at tortor pulvinar varius. Donec venenatis vulputate lorem. Phasellus accumsan cursus velit. Pellentesque ut neque.
            </p>

            <v-row>
            <v-col></v-col>
            <v-col class="mr-auto">
                <v-icon large>mdi-thumb-up-outline</v-icon><p>100</p>
            </v-col>
            </v-row>
            
            <v-row>
                <v-col cols="1"></v-col>
                <v-col class="mr-auto"><comment v-for="item in items" :key="item.tab"/></v-col>
            </v-row>

            <!-- paging -->
            <div class="text-center mr-tp">
                <v-pagination
                  v-model="page"
                  :length="pageCnt"
                  circle
                ></v-pagination>
            </div>
        </v-col>
        <v-col cols="2"></v-col>
        <!-- footer쓸까? -->
        </v-row>
      </v-container>
</template>

<script>
import Comment from '../../components/Comment.vue';

export default {
    components : {Comment},
    data: function() {
    return {
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
}
</script>

<style scoped>
#recommend{
    margin-right: 10px;
}
</style>