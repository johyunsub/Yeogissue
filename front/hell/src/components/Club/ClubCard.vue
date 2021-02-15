<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-col cols="12">
      <v-card
        class="mx-auto my-5 elevation-5 choice_cursor { 'on-hover': hover }"
        max-width="500"
        min-width="500"
        :elevation="hover ? 16 : 2"
      >
        <div class="d-flex flex-no-wrap">
            <img
            style="width: 150px; height:150px"
              src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            >
          <div>
            <v-card-title @click="MovePage('detail')" class="headline mb-0 h6"
              >{{ clubInfo.title }}
            </v-card-title>
            <v-card-text>
              <v-row align="center" class="mx-0"> </v-row>

              <div class="my-2 subtitle-4 text-truncate">
                <span style="color: blueviolet">{{ clubInfo.category }} </span>
              </div>
              <div>
                <v-icon v-if="clubInfo.is_private" small color="">fas fa-lock</v-icon>
                <v-icon v-if="!clubInfo.is_private" small color=""></v-icon>
                <v-icon class="ml-3" small color="blue"
                  >fas fa-user-friends</v-icon
                >
                 {{ clubInfo.member_cnt }} 
              </div>
            </v-card-text>
          </div>
         
        </div>
      </v-card>
    </v-col>
  </v-hover>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "clubCard",
  computed: {
    ...mapState("clubStore", ["clubManageMemberList"]),
    ...mapState(["userInfo"]),
  },
  data() {
    return {
      show: false,
    };
  },
  props: {
    clubInfo: Object,
  },
  created() {},
  methods: {
    MovePage: function (check) {
      switch (check) {
        case "detail":
          this.isLogin();
          break;
      }
    },
    isLogin() {
      if (this.userInfo != null) {
        this.$router.push(`/clubDetail?id=${this.clubInfo.id}`);
      } else {
        this.$fire({
          title: "로그인후 이용하실 수 있습니다.",
          type: "error",
        });
      }
    },
  },
};
</script>

<style lang="sass"></style>
