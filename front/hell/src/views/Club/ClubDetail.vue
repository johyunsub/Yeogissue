<template>
  <v-container>
    <h2 class="text-center mr-tp mr-bt">클럽 이름??</h2>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col id="opinion_main">
        <!-- 클럽 정보 -->
        <v-row class="mr-tp">
          <v-sheet height="30vh" width="100%" elevation="2">
            <v-row class="mt-3">
              <v-col><img src="dddd" alt="이미지 넣어줘"/></v-col>
              <v-col>
                <v-row>
                  클럽정보 (맴버수, 카테고리, 개설일, 마스터)
                </v-row>
                <v-row class="mt-3">
                  <v-btn color="blue darken-1" text @click="OnOff()">관리</v-btn>
                  <v-btn color="blue darken-1" text @click="OnOff()">가입하기</v-btn>
                </v-row>
              </v-col>
            </v-row>
          </v-sheet>
        </v-row>

        <v-divider class="my-10"></v-divider>

        <!-- 가입해야지만 보이게-->
        <club-detail-content />
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
  </v-container>
</template>

<script>
import ClubDetailContent from '../../components/Club/Detail/ClubDetailContent.vue';

export default {
  components: { ClubDetailContent },
  data: function() {
    return {};
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.category {
  margin-top: 40px;
}
</style>
