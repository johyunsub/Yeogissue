<template>
  <v-sheet height="12vh">
    <div class="title mt-10 ml-2">기사제목ㅇㅇ</div>
    <div class="body-2 mt-3 ml-2">Url : {{ urlData.url }}</div>
    <div class="body-2 mt-8 ml-2" v-if="type === 'club'">코멘트 : {{ urlData.comment }}</div>
    <v-divider class="my-3"></v-divider>
  </v-sheet>
</template>

<script>
export default {
  props: {
    type: String,
    urlData: Object,
  },
  methods: {
    data() {
      return { qqqq: this.urlData };
    },
  },
  created() {
    console.log(this.data());
  },
};
</script>
