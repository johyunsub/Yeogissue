<template>
  <v-sheet height="12vh">
    <div class="title mt-5 ml-2">기사제목ㅇㅇ</div>
    <div class="body-2 mt-3 ml-2">기사내용</div>
    <div class="body-2 mt-8 ml-2" v-if="type === 'club'">코멘트</div>
    <v-divider class="my-3"></v-divider>
  </v-sheet>
</template>

<script>
export default {
  props: {
    type: { Type: String },
  },
  methods: {},
  created() {},
};
</script>
