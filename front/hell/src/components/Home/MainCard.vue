<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-card
      class="ml-5 my-5 elevation-10 choice_cursor { 'on-hover': hover }"
      max-width="300"
      min-width="300"
      max-height="260"
      min-height="260"
      rounded
      :elevation="hover ? 16 : 1"
    >
      <v-card-title class="headline mt-5 ml-5 h6">{{data.title}} </v-card-title>
      <v-card-text>
        <span class="subtitle-1 ml-5" style="height:100px">{{data.content}}</span>
      </v-card-text>
      <v-card-actions>
        <v-btn class="btnLC ml-3" color="blue" rounded>
            <span style="color: white;"> 바로가기 </span></v-btn
          >
      </v-card-actions>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: "Home",
  props:{
    data : {Type : Object}
  },
  data: () => ({
    
  }),
  methods: {

  },
};
</script>

<style>
.issue-span:hover {
  background-color: #FAEAD4;
  border-radius: 20px 20px 20px 20px;
  padding: 4px;
}
</style>