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
        :items="member"
        :search="search"
      ></v-data-table>
    </v-card>
  </v-container>
</template>
<script>
import axios from 'axios';
import { API_BASE_URL } from "../../../../config";

export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'No.',
            align: 'start',
            sortable: false,
            value: 'no',
          },
          { text: '닉네임', value: 'nickname' },
          { text: '이름', value: 'name' },
          { text: '가입사유', value: 'motive' },
          { text: '가입일', value: 'date' },
        ],
        member: [
          {
            no: 1,
            nickname: 'Frozen Yogurt',
            name: 159,
            fat: 6.0,
            motive: 24,
            date: 4.0,
          },
          
        ],
      }
    },
    methods: {
        getList() {
            axios.get(`${ API_BASE_URL }club/member_check/${this.$route.query.id}/`,)
        }
    },
    created() {
        this.getList();
    }
};
</script>