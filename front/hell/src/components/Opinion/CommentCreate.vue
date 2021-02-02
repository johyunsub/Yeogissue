<template>
  <v-card class="mr-tp" max-width="1000" outlined>
    <v-card-title class="ml-2 subtitle-1">아이디</v-card-title>
    <v-card-text>
      <v-textarea
        v-model="content"
        append-icon="mdi-comment"
        class="mx-2"
        :label="massage"
        rows="5"
        auto-grow
      ></v-textarea>
      <v-row>
        <v-col cols="auto" class="mr-auto"> </v-col>
        <v-col cols="auto" class="mr-2"> <v-btn @click="CommentCreate"> 등록</v-btn> </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  data() {
    return {
      content: '',
      massage: '댓글을 입력하세요', // 로그인에 따라 내용 바꿔주고 disabled
      createData: {
        opinion_type: false, // 찬반 추후 수정
        content: '',
        user: 2, // 찬한 추후 수정
      },
    };
  },
  methods: {
    ...mapActions('opinionStore', ['opinionCommentCreate']),
    CommentCreate() {
      this.createData.content = this.content;
      this.opinionCommentCreate(this.createData);
      this.content = '';
    },
  },
};
</script>
