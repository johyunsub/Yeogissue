<template>
  <v-container>
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
        :items="clubManageJoinList"
        :search="search"
      >
      <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="approve(item)"
      >
        fas fa-check
      </v-icon>
      <v-icon
        small
        @click="disapprove(item)"
      >
        fas fa-ban
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
import {mapState, mapActions } from 'vuex';

export default {
    computed:{
        ...mapState('clubStore', [ 'clubManageJoinList' ])
    },
    data () {
      return {
        search: '',
        headers: [
          { text: '이름', value: 'username' },
          { text: '가입동기', value: 'comment' },
          { text: '가입일', value: 'created_at' },
          { text: '게시글수', value: 'article_cnt' },
          { text: '승인 | 취소', value: 'actions',sortable: false },
        ],
      }
    },
    methods: {
      ...mapActions( 'clubStore', ['clubMangeList', 'clubManageJoinApprove', 'clubManageJoinDisApprove']),
     
      approve(item) {
        this.clubManageJoinApprove({ member: item.user })
        console.log(item.user)
      },
      disapprove(item) {
        this.clubManageJoinDisApprove({ member: item.user })
      }
    },
    created() {
        this.clubMangeList({type: ''});
    }
};
</script>

<style scoped>
.fa-square-o{
  border : 1px solid black;
}
</style>