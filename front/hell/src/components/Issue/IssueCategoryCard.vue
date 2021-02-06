<template>
  <v-card class="mx-auto my-5 ml-5 elevation-5 choice_cursor" max-width="250" :elevation="2">
    <!-- 글짜 ... 해주는거 text-truncate -->
    <v-card-title class="headline pl-6 h6" style="background-color:#5845EA">
      {{ category }}
    </v-card-title>

    <v-card-text class="mt-8">
      <v-row align="center"> </v-row>
      <v-btn text rounded @click="Move()"> 1. 순위 </v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    category: { type: String },
    date: { type: String },
  },
  data() {
    return {
      // data
    };
  },
  methods: {
    Move() {},
  },
  created() {
    //여기서 카테고리 값 받아오기
  },
};
</script>
