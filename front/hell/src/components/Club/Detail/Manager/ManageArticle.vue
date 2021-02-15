<template>
    <v-container>
    <!-- <h1>게시글 관리 - 게시물 번호,  코멘트, 게시물 url, 작성자</h1> -->
    <v-card>
      <v-card-title>
        가입요청 관리
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
        :items="clubManageMemberList"
        :search="search"
      >
      <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="approve(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="disapprove(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <p>가입요청 회원이 아직 없어요 ㅠ.ㅠ</p>
    </template>
    </v-data-table>
    </v-card>
  </v-container>
</template>
<script>
import {mapState } from 'vuex';
export default {
    computed:{
        ...mapState('clubStore', [ 'clubManageMemberList' ])
    },
    data () {
      return {
        search: '',
        headers: [
          { text: 'No.', value: 'no' },
          { text: '카테고리', value: 'category' },
          { text: '제목', value: 'title' },
          { text: '가입동기', value: 'comment' },
          { text: '게시글 링크', value: 'url' },
          { text: '작성자', value: 'writer' },
          { text: '승인 | 취소', value: 'actions',sortable: false },
        ],
      }
    },
}
</script>