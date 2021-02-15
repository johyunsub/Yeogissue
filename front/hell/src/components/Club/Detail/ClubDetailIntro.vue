<template>
  <v-container>  <div>
            <v-row class="mt-1 mr-auto mb-2">
              <v-col cols="2" class="mr-auto" md="10">
                <!-- <v-sheet width="90%"> -->
                  <!-- 클럽정보 (맴버수, 카테고리, 개설일, 마스터) -->

                  <div class="mt-3">카테고리 - {{ clubData.category }}</div>
                  <div class="mt-3">멤버수 - {{ clubData.member_cnt }}</div>
                  <div class="mt-3">클럽장 - {{ clubData.mastername }}</div>
                  <div class="mt-3">개설일 - {{ clubData.created_at }}</div>
                <!-- </v-sheet> -->
              </v-col>
             
              <v-col cols="auto"></v-col>
            </v-row>
          </div></v-container>
</template>

<script>

import { mapState } from 'vuex';
export default {
  components: {
  },
  computed: {
    ...mapState('clubStore', ['clubData', 'clubDetailManegerBtn', 'clubDetailIsMember', 'clubDetailIsWaiting', 'clubManageMemberList']),
    ...mapState( ['userInfo' ]),
  },
  data() {
    return {
      content: '',
    }
    
  },
  props: {
    clubInfo: { type: Object},
  },
}

</script>