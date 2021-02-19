<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-card
      class="ml-5 my-5 mx-auto elevation-10 rounded-xl { 'on-hover': hover }"
      max-width="300"
      min-width="300"
      max-height="280"
      min-height="280"
      :elevation="hover ? 16 : 2"
      :id="'mainCard' + data.id"
      @mouseover="changeBack('over')"
      @mouseout="changeBack('out')"
    >
      <v-card-title class="headline mt-5 ml-5 pt-7" :id="'cardTitle' + data.id"
        style="font-weight: 600;">{{ data.title }} 
        <i style="color:#29B6F6" class="far fa-comment-dots ml-2" v-if="data.id ==1"></i>
        <i style="color:#D81B60" class="fas fa-users ml-2" v-if="data.id ==2"></i>
        <i style="color:#F9A825" class="fas fa-crown ml-2" v-if="data.id ==3"></i>
        <i style="color:#6D4C41" class="fas fa-book-reader ml-2" v-if="data.id ==4"></i>
      </v-card-title>
      
      <v-card-text>
        <span
          class="subtitle-1 ml-5 pt-3 menu-descText"
          :id="'cardContent' + data.id"
          style="height:100px"
          >{{ data.content }} <br> {{data.content2}}</span
        >
      </v-card-text>
      <v-card-actions>
        <v-btn class=" ml-5 mt-5" color="white" rounded @click="movepage()">
          <span style="color: black;"> 바로가기 > </span></v-btn
        >
      </v-card-actions>
    </v-card>
  </v-hover>
</template>

<script>
import $ from 'jquery';

export default {
  name: 'Home',
  props: {
    data: { Type: Object },
  },
  data: () => ({}),
  methods: {
    changeBack(check) {
      let back = '#mainCard' + this.data.id;
      let title = '#cardTitle' + this.data.id;
      let content = '#cardContent' + this.data.id;
      if (check == 'over') {
        $(back).css('background-color', '#1F5EFF');
        $(title).css('color', 'white');
        $(content).css('color', 'white');
      } else if (check == 'out') {
        $(back).css('background-color', 'white');
        $(title).css('color', 'black');
        $(content).css('color', 'rgba(0, 0, 0, 0.6)');
      }
    },
    movepage(){
      if(this.data.id == 1) this.$router.push(`/opinion`);
      else if(this.data.id ==2) this.$router.push(`/club`);
      else if(this.data.id ==3) this.$router.push(`/issue`);
      else if(this.data.id ==4) this.$router.push(`/magazine`);
    }
  },
};
</script>

<style>

.menu-subject {
  font-size: 21px;
  letter-spacing: -0.05em;
  font-weight: 800;
  margin: 4px 0 21px;
}
.menu-descText {
  display: block;
  text-align: left;
}
</style>
