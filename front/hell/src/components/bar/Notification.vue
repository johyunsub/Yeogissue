<template>
  <v-menu
    v-model="notiMenu"
    :close-on-content-click="false"
    :nudge-right="40"
    offset-y
    left
    open-on-hover
    transition="scale-transition"
    min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn icon medium color="primary" fab v-bind="attrs" v-on="on">
        <v-icon>mdi-bell-outline</v-icon>
      </v-btn>
    </template>
    <div v-if="alarms.length == 0">알람이 없습니다.</div>
    <v-list v-if="alarms.length != 0">
      <div class="pl-4 pb-3 border-bt">VIEW READ</div>
      <v-list-item
        class="alarm"
        v-for="(item, index) in alarms"
        :key="index"
        style="font-size: 13px; width:300px"
      >
        <div
          v-if="item.message_type == '댓글'"
          class="alarm choice_cursor"
          @click="alarmOpinion(item.object_id, 1, item.id)"
        >
          <v-icon small color="blue darken-2" class="mr-1">far fa-comment-alt</v-icon> 내가 쓴 '{{
            item.object_content
          }}'글에 댓글이 추가됨
        </div>
        <div
          v-else-if="item.message_type == '좋아요'"
          class="alarm choice_cursor"
          @click="alarmOpinion(item.object_id, 1, item.id)"
        >
          <v-icon small color="red" class="mr-1">far fa-heart</v-icon> 내가 쓴 '{{
            item.object_content
          }}'글에 좋아요 눌림
        </div>
        <div
          v-else-if="item.message_type == '댓글좋아요'"
          class="alarm choice_cursor"
          @click="alarmOpinion(item.object_id, 1, item.id)"
        >
          <v-icon small class="mr-1">mdi-thumb-up-outline</v-icon>
          내가 쓴 '{{ item.object_content }}'댓글에 좋아요 눌림
        </div>
        <div
          v-else-if="item.message_type == '클럽승인'"
          class="alarm choice_cursor"
          @click="alarmClub(item.object_id, 2, item.id)"
        >
          <v-icon small class="mr-1" color="red accent-3">fas fa-lock</v-icon>
          '{{ item.object_content }}'클럽에 클럽승인 요청
        </div>
        <div
          v-else-if="item.message_type == '클럽승인완료'"
          class="alarm choice_cursor pd-minus"
          @click="alarmClub(item.object_id, 2, item.id)"
        >
          <v-icon class="mr-1" small color="blue">fas fa-user-friends</v-icon>
          '{{ item.object_content }}'클럽에 클럽 승인됨
        </div>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
import { mapActions, mapState } from "vuex";
import { API_BASE_URL } from "../../config";
import axios from "axios";

export default {
  ...mapState(["alarms"]),
  data: () => ({
    notiMenu: false,
    messages: 0,
    items: [],
  }),
  methods: {
    ...mapActions("opinionStore", ["opinionDetail"]),
    ...mapActions("clubStore", ["clubDeatil"]),
    alarmOpinion(id, num, alr) {
      if (num == 1) {
        axios
          .get(`${API_BASE_URL}articles/${id}/`)
          .then((res) => {
            console.log(res.data.content);
            // this.getClubTagName();
            this.$store.commit("opinionStore/SET_OPINION_DETAIL", res.data);
            this.$store.commit("opinionStore/SET_OPINION_COMMENT", res.data.comment_set);
            this.$store.commit("opinionStore/SET_OPINION_COMMENT_PAGING", 0);
          })
          .catch((err) => console.log(err.response));
        this.$router.push(`/opinionDetail?id=${id}`).catch(() => {});
      } else if (num == 2) {
        axios
          .get(`${API_BASE_URL}club/club_detail/${id}/`)
          .then((res) => {
            this.$store.commit("SET_CLUB_DETAIL", res.data);
          })
          .catch((err) => console.log(err.response));
        this.$router.push(`/clubDetail?id=${id}`).catch(() => {});
      }

      axios
        .post(`${API_BASE_URL}accounts/alarm_check/`, { alarm_id: alr })
        .then(() => {
          this.$store.dispatch("alarm");
        })
        .catch((err) => console.log(err.response));
    },
  },
  computed: {
    ...mapState(["alarms"]),
    // this.items = alarms
  },
};
</script>

<style>
.alarm:hover {
  background-color: grey;
}

.pd-minus {
}
</style>
