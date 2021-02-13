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
    <v-list>
      <v-list-item class="alarm" v-for="(item, index) in alarms" :key="index">
        <v-list-item-title v-if="item.message_type=='댓글'" class="alarm choice_cursor" @click="alarm()">{{ item.object_id }}글에 {{ item.object_content}} 댓글이 추가됨</v-list-item-title>
        <v-list-item-title v-else-if="item.message_type=='좋아요'" class="alarm choice_cursor" @click="alarm()">{{ item.object_content }}글에 좋아요 눌림</v-list-item-title>
        <v-list-item-title v-else-if="item.message_type=='댓글좋아요'" class="alarm choice_cursor" @click="alarm()">{{ item.object_content }}댓글에 좋아요 눌림</v-list-item-title>
        <v-list-item-title v-else-if="item.message_type=='클럽승인'" class="alarm choice_cursor" @click="alarm()">{{ item.object_content }}에 클럽승인 요청</v-list-item-title>
        <v-list-item-title v-else-if="item.message_type=='클럽승인완료'" class="alarm choice_cursor" @click="alarm()">{{ item.object_content }}에 클럽 승인됨</v-list-item-title>
        
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
    // alarm(){
    //   console.log("찍힘");
      
    // }
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
