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
      <v-list-item class="alarm" v-for="(item, index) in items" :key="index">
        <v-list-item-title class="alarm choice_cursor" @click="alarm()">{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  data: () => ({
    notiMenu: false,
    messages: 0,
    items: [
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me 2" },
    ],
  }),
  methods:{
    alarm(){
      console.log("찍힘");
    }
  }
};
</script>

<style>
.alarm:hover {
  background-color: grey;
}
</style>
