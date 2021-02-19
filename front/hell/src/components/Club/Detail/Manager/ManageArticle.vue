<template>
  <v-container>
    <!-- <h1>게시글 관리 - 게시물 번호,  코멘트, 게시물 url, 작성자</h1> -->
    <v-card>
      <v-card-title>
        게시물 관리
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="clubManageArticleList"
        :search="search"
      >
        <template v-slot:item.actions="{ item }">
          <v-icon small @click="deleteItem(item)">
            mdi-delete
          </v-icon>
        </template>
        <template v-slot:no-data>
          <p>게시물이 아직 없어요 ㅠ.ㅠ</p>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>
<script>
import { mapState, mapActions } from "vuex";
export default {
  computed: {
    ...mapState("clubStore", ["clubManageMemberList", "clubManageArticleList"]),
  },
  data() {
    return {
      search: "",
      headers: [
        { text: "카테고리", value: "category" },
        // { text: '제목', value: 'title' },
        { text: "내용", value: "comment" },
        { text: "게시글 링크", value: "url" },
        { text: "작성일", value: "created_at" },
        { text: "삭제", value: "actions", sortable: false },
      ],
    };
  },
  methods: {
    ...mapActions("clubStore", ["clubManageArticle", "clubDetailUrlDelete"]),
    
    deleteItem(item){
      console.log(item.id)
      this.clubDetailUrlDelete(item.id)
    }
  },
  created() {
    this.clubManageArticle();
  },
};
</script>
