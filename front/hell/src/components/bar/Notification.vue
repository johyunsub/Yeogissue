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
      <v-list-item class="alarm" v-for="(item, index) in alarms" :key="index">
        <div
          v-if="item.message_type == '댓글'"
          class="alarm choice_cursor"
          @click="alarmOpinion(item.object_id)"
        >
          내가 쓴 '{{ item.object_content }}'글에 댓글이 추가됨
        </div>
        <div
          v-else-if="item.message_type == '좋아요'"
          class="alarm choice_cursor"
          @click="alarmOpinion(item.object_id)"
        >
          내가 쓴 '{{ item.object_content }}'글에 좋아요 눌림
        </div>
        <div
          v-else-if="item.message_type == '댓글좋아요'"
          class="alarm choice_cursor"
          @click="alarmOpinion(item.object_id)"
        >
          내가 쓴 '{{ item.object_content }}'댓글에 좋아요 눌림
        </div>
        <div
          v-else-if="item.message_type == '클럽승인'"
          class="alarm choice_cursor"
          @click="alarmClub(item.object_id)"
        >
          '{{ item.object_content }}'클럽에 클럽승인 요청
        </div>
        <div
          v-else-if="item.message_type == '클럽승인완료'"
          class="alarm choice_cursor"
          @click="alarmClub(item.object_id)"
        >
          '{{ item.object_content }}'클럽에 클럽 승인됨
        </div>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
import { mapState } from 'vuex';

export default {
  ...mapState(['alarms']),
  data: () => ({
    notiMenu: false,
    messages: 0,
    items: [],
  }),
  methods: {
    alarmOpinion() {},
  },
  computed: {
    ...mapState(['alarms']),
    // this.items = alarms
  },
};
</script>

<style>
.alarm:hover {
  background-color: grey;
}
</style>
