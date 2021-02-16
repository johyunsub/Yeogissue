<template>
  <v-container>
    <v-card class="mt-10" min-height="300">
      <div class="text-center pt-5">
        <!-- <v-sheet width="90%"> -->
        <!-- 클럽정보 (맴버수, 카테고리, 개설일, 마스터) -->
        <div class="mt-3">카테고리 - {{ clubData.category }}</div>
        <div class="mt-3">멤버수 - {{ clubData.member_cnt }}</div>
        <div class="mt-3">클럽장 - {{ clubData.mastername }}</div>
        <div class="mt-3">개설일 - {{ clubData.created_at.substr(0, 10) }}</div>
        <div class="mt-3">소개글</div>
        <div class="mt-3">{{ clubData.content }}</div>
        <!-- </v-sheet> -->
      </div>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
export default {
  components: {},
  computed: {
    ...mapState('clubStore', [
      'clubData',
      'clubDetailManegerBtn',
      'clubDetailIsMember',
      'clubDetailIsWaiting',
      'clubManageMemberList',
    ]),
    ...mapState(['userInfo']),
  },
  data() {
    return {
      content: '',
    };
  },
  props: {
    clubInfo: { type: Object },
  },
};
</script>
