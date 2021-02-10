<template>
<div>
  <!-- <v-container> -->
    <!-- <h2 class="text-center mr-tp mr-bt display-1">Club</h2> -->
    <v-row>

      <v-col id="">
        <!-- 클럽 정보 -->
        <club-detail-card />

        <!-- <v-divider class="my-10"></v-divider> -->

        <!-- 가입해야지만 보이게-->
        <club-detail-content v-if="clubDetailManegerBtn === false" />

        <!-- 클럽 관리자 -->
        <club-detail-manager-content v-if="clubDetailManegerBtn === true" />
      </v-col>

    </v-row>
  <!-- </v-container> -->
  </div>
</template>

<script>
import ClubDetailContent from '../../components/Club/Detail/ClubDetailContent.vue';
import ClubDetailManagerContent from '../../components/Club/Detail/Manager/ClubDetailManagerContent.vue';
import ClubDetailCard from '../../components/Club/Detail/ClubDetailCard.vue';
import { mapState, mapActions } from 'vuex';

export default {
  components: { ClubDetailContent, ClubDetailCard, ClubDetailManagerContent },
  computed: {
    ...mapState('clubStore', ['clubDetailManegerBtn']),
  },
  data: function() {
    return {};
  },
  methods: {
    ...mapActions('clubStore', ['clubDetail']),
  },
  created() {
    this.clubDetail(this.$route.query.id);
  },
};
</script>

<style lang="scss" scoped>
.category {
  margin-top: 40px;
}
</style>
