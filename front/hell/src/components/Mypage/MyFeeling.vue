<template>
  <div class="ml-7">
    <p class="text-h4 font-weight-black ml-7">
      나의 감정 분석
      <i class="fas fa-kiss-beam"></i>
    </p>
    <hr class="ml-7" width="98%" color="green" />
    <div class="mt-7"></div>
    <!-- 내용 -->
    <v-row class="mr-tp">
      <div>
        <graph-bubblecloud
          class="mt-10"
          :width="800"
          :height="500"
          :padding-top="10"
          :padding-bottom="0"
          :padding-left="0"
          :padding-right="0"
          :values="myEmotion"
          :colors="colors"
          :render-interval="0"
        >
        </graph-bubblecloud>
      </div>
    </v-row>
    <div class="text-center mt-10">
      <span
        >당신은 <span style="color:blue">'{{ bestEmotion }}'</span>의 감정이 많군요 ^^</span
      >
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState(["userInfo", "myEmotion"]),
  },
  data() {
    return {
      colors: function(data) {
        if (data[2] > 4000) {
          return 2;
        } else if (data[2] > 3000) {
          return 1;
        }

        return 0;
      },
      bestEmotion: "",
    };
  },
  created() {
    window.scrollTo(0, 0);
    let index = 0;
    for (let i = 0; i < 8; i++) {
      if (index < this.myEmotion[i][1]) {
        this.bestEmotion = this.myEmotion[i][0];
        index = this.myEmotion[i][1];
      }
    }
  },
};
</script>

<style></style>
