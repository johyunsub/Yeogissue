<template>
  <v-container>
    <v-card>
      <v-card-title>
        클럽 멤버 관리
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
        @click="deleteItem(item)"
      >
        fas fa-users-slash
      </v-icon>
    </template>
    <template v-slot:no-data>
      <p>가입한 회원이 아직 없어요 ㅠ.ㅠ</p>
    </template>
    </v-data-table>
    </v-card>
  </v-container>
</template>
<script>
import {mapState, mapActions } from 'vuex';
// import axios from 'axios';
// import { API_BASE_URL } from "../../../../config";

export default {
    computed:{
        ...mapState('clubStore', [ 'clubManageMemberList'])
    },
    data () {
      return {
        search: '',
        headers: [
          { text: '이름', value: 'username' },
          { text: '가입동기', value: 'comment' },
          { text: '가입일', value: 'created_at' },
          { text: '게시글수', value: 'article_cnt' },
          { text: '추방', value: 'actions',sortable: false },
        ],
      }
    },
    methods: {
        ...mapActions( 'clubStore', ['clubMangeList', 'clubMemberRemove']),
        getList() {
            // axios.post(`${ API_BASE_URL }club/member_check/${this.$route.query.id}/`, '')
            // .then((res) => {
                // console.log(res.data)
            // })
            this.clubMangeList({type: '승인'});
            
        },
        deleteItem(item){
          console.log(item)
          this.clubMemberRemove({ user: item.user })
        }
    },
    created() {
        this.getList();
    }
};
</script>