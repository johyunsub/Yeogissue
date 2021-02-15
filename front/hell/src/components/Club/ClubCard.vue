<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-col cols="12">
    <v-card
      class="mx-auto my-5 elevation-5 choice_cursor { 'on-hover': hover }"
      max-width="600"
      :elevation="hover ? 16 : 2"
      
    >
    <div class="d-flex flex-no-wrap justify-space-between">
      <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img height="150" src="https://cdn.vuetifyjs.com/images/cards/cooking.png">
      </v-img>

              </v-avatar>
      <div>
        <v-card-title @click="MovePage('detail')" class="headline mb-0 h6">{{ clubInfo.title }}
      </v-card-title>
       <v-card-text>
        <v-row align="center" class="mx-0"> </v-row>

        <div class="my-2 subtitle-4 text-truncate">
        <span style="color:blueviolet">{{ clubInfo.category }} </span>
        </div>
        <div>
          <v-icon small color="">fas fa-lock</v-icon>
          <v-icon class="ml-3" small color="blue">fas fa-user-friends</v-icon> 클럽 멤버 수
        </div>

      </v-card-text>


      </div>
      <!-- <v-img height="150" src="https://cdn.vuetifyjs.com/images/cards/cooking.png">
      </v-img> -->

      <!-- 글짜 ... 해주는거 text-truncate -->
      <!-- <v-card-title @click="MovePage('detail')" class="headline mb-0 h6">{{ clubInfo.title }}
      </v-card-title> -->
<!-- 
      <v-card-text>
        <v-row align="center" class="mx-0"> </v-row>

        <div class="my-2 subtitle-4 text-truncate">
        <span style="color:blueviolet">{{ clubInfo.category }} </span> <v-icon class="ml-3" small color="blue">fas fa-user-friends</v-icon> 클럽 멤버 수
        </div>

      </v-card-text> -->

      <!-- <v-divider class="mx-4"></v-divider> -->
<!-- 
      <v-card-text>
        <v-chip>공개/비공개 표시</v-chip>
         <v-chip>활발/보통/저조</v-chip>
      </v-card-text> -->

    </div>
    
    </v-card>
    </v-col>
  </v-hover>
</template>

<script>
export default {
  name: 'clubCard',
  computed: {},
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
    MovePage: function(check) {
      switch (check) {
        case 'detail':
          console.log(this.clubInfo,'clubinfo')
          this.$router.push(`/clubDetail?id=${this.clubInfo.id}`);
          break;
      }
    },
  },
};
</script>

<style lang="sass"></style>
