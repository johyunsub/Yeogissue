<template>
  <div>
    <!-- 카테고리 if문 처리-->
    <div class="category mt-15">
      <v-col cols="4"></v-col>
      <v-col>
        <v-tabs>
          <v-tab @click="SelectCategory('member')">멤버관리</v-tab>
          <v-tab @click="SelectCategory('board')">게시물 관리</v-tab>
          <v-tab @click="SelectCategory('join')">가입요청</v-tab>
        </v-tabs>
      </v-col>
      <v-col cols="3"></v-col>
    </div>

    <!-- 내용 -->
    <div class="mr-tp">
      <v-col v-if="categoryType == 'member'">
        <manage-member />
      </v-col>
      <v-col v-if="categoryType == 'board'"><manage-article /> </v-col>
      <v-col v-if="categoryType == 'join'"><manage-join /></v-col>
    </div>

    <!-- paging -->

    <!-- 수정 -->
    <v-btn @click="OnOff"></v-btn>
    <club-create :type="'update'" />
  </div>
</template>

<script>
import ManageJoin from './ManageJoin.vue';
import ManageArticle from './ManageArticle.vue';
import ManageMember from './ManageMember.vue';
import ClubCreate from '../../ClubCreate.vue';
import { mapState, mapActions } from 'vuex';

export default {
  computed: {
    ...mapState('clubStore', ['clubManageMemberList']),
  },
  components: {
    ManageJoin,
    ManageArticle,
    ManageMember,
    ClubCreate,
  },

  data() {
    return {
      categoryType: 'member',
    };
  },
  methods: {
    ...mapActions('clubStore', ['clubMangeList']),
    SelectCategory: function(category) {
      this.categoryType = category;
      switch (category) {
        case 'member':
          // this.getList();
          break;
      }
    },
    OnOff: function() {
      this.$store.commit('clubStore/CLUB_CREATE_DIALOG', true);
    },
  },
  created() {
    //멤버 정보와 게시물 정보 가입 정보
  },
};
</script>
