<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-card
      class="ml-5 my-5 mx-auto elevation-10 { 'on-hover': hover }"
      max-width="300"
      min-width="300"
      max-height="260"
      min-height="260"
      rounded
      :elevation="hover ? 16 : 2"
      :id="'mainCard' + data.id"
      @mouseover="changeBack('over')"
      @mouseout="changeBack('out')"
    >
      <v-card-title class="headline mt-5 ml-5 menu-subject " :id="'cardTitle' + data.id"
        >{{ data.title }}
      </v-card-title>
      <v-card-text>
        <span
          class="subtitle-1 ml-5 menu-descText"
          :id="'cardContent' + data.id"
          style="height:100px"
          >{{ data.content }}</span
        >
      </v-card-text>
      <v-card-actions>
        <v-btn class=" ml-5" color="white" rounded>
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
  },
};
</script>

<style>
.menu-descText {
  display: block;
  font-size: 15px;
  line-height: 23px;
  letter-spacing: -0.05em;
  opacity: 0.4;
  font-weight: 400;
  text-align: left;
}

.menu-subject {
  font-size: 21px;
  letter-spacing: -0.05em;
  font-weight: 600;
  margin: 4px 0 21px;
}
</style>
