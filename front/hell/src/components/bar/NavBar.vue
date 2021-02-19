<template>
  <v-app-bar app color="white" flat id="navbar" height="80vh">
    <v-col class="ml-16">
      <v-btn dark text height="10vh">
        <img
          :src="require('../../assets/logo2.png')"
          @click="MovePage('home')"
          style="height:80px;"
        />
      </v-btn>
      <v-btn text @click="MovePage('opinion')">의견이슈</v-btn>
      <v-btn text @click="MovePage('club')">모여이슈</v-btn>
      <v-btn text @click="MovePage('issue')">이슈랭킹</v-btn>
      <v-btn text @click="MovePage('data')">매거진</v-btn>
    </v-col>

    <v-col cols="auto" v-if="isLoginToken == ''">
      <v-btn text @click="OnOff('login')">로그인</v-btn>
      <v-btn text @click="MovePage('join')">회원가입</v-btn>
    </v-col>
    <v-col cols="auto" v-if="isLoginToken != ''">
      <span class="mr-2" style="font-Size:18px"> 안녕하세요 </span><span  style="font-Size:20px;color:#DF01D7">{{ userInfo.nickname }}</span> <span style="font-Size:18px">님 </span>
      <span class="mr-1 ml-1"><notification /></span>
      <v-btn text @click="MovePage('myPage')">마이페이지</v-btn>
      <v-btn text color="red" @click="Out">로그아웃</v-btn>
    </v-col>
    <login />

    <youtube-dialog />
    <my-profile-modal />
  </v-app-bar>
</template>

<script>
import Login from "../Login/Login.vue";
import youtubeDialog from "../Issue/IssueYoutubeDialog.vue";
import MyProfileModal from "../../components/Mypage/MyProfileModal.vue";
import Notification from "./Notification.vue";
import { mapState } from "vuex";
import $ from "jquery";

export default {
  components: { Notification, Login, youtubeDialog, MyProfileModal },
  computed: {
    ...mapState(["userInfo", "isLoginToken"]),
  },
  data() {
    return {};
  },
  created() {},
  methods: {
    OnOff: function(message) {
      switch (message) {
        case "menu":
          this.$store.commit("CHANGE_DRAWER", true);
          break;
        case "login":
          this.$store.commit("CHANGE_DIALOG", true);
          break;
      }
    },
    MovePage: function(check) {
      $("div").remove(".tooltip");
      switch (check) {
        case "opinion":
          this.$router.push({ name: "Opinion" });
          break;
        case "home":
          this.$router.push({ name: "Home" });
          break;
        case "club":
          this.$router.push({ name: "Club" });
          break;
        case "issue":
          this.$router.push({ name: "Issue" });
          break;
        case "data":
          this.$router.push({ name: "Magazine" });
          break;
        case "join":
          this.$router.push({ name: "Join" });
          break;
        case "myPage":
          this.$router.push({ name: "MyPage" });
          break;
      }
    },
    Out: function() {
      this.$store.dispatch("userLogout");
      this.$store.commit("CHANGE_DRAWER", false);
      this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style lang="scss">
#navbar {
  outline: 1px solid rgb(225, 225, 225);
}
</style>
