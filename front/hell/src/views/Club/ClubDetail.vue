<template>
  <v-container>
    <h2 class="text-center mr-tp mr-bt">클럽 이름??</h2>
    <v-row>
      <v-col cols="3"></v-col>
      <v-col id="opinion_main">
        <!-- 클럽 정보 -->
        <v-row class="mr-tp">
          <v-sheet height="50%" width="100%" elevation="2">
            <v-row>
              <v-col><img src="dddd" alt="이미지 넣어줘"/></v-col>
              <v-col>클럽정보 (맴버수, 카테고리, 개설일, 마스터)</v-col>
            </v-row>
          </v-sheet>
        </v-row>

        <v-divider class="my-10"></v-divider>

        <!-- 가입해야지만 보이게-->

        <!-- 카테고리 if문 처리-->
        <v-row class="category">
          <v-tabs>
            <v-tab>소개</v-tab>
            <v-tab>뉴스</v-tab>
            <v-tab>유튜브</v-tab>
            <v-tab>기타</v-tab>
            <v-tab>의견나눔</v-tab>
          </v-tabs>
        </v-row>

        <!-- 내용 -->
        <v-row class="mr-tp">
          <v-col v-if="viewType == 'list'"><opinion-table /></v-col>
          <v-col v-if="viewType == 'card'"
            ><card-list v-for="item in items" :key="item.tab" />
          </v-col>
        </v-row>

        <!-- paging -->
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  components: {},
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
