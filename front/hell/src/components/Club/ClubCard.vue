<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-card
      class="mx-auto my-5 elevation-5 choice_cursor { 'on-hover': hover }"
      max-width="600"
      :elevation="hover ? 16 : 2"
      
    >
      <v-img height="150" src="https://cdn.vuetifyjs.com/images/cards/cooking.png">
      </v-img>

      <!-- 글짜 ... 해주는거 text-truncate -->
      <v-card-title @click="MovePage('detail')" class="headline mb-0 h6">{{ clubInfo.title }}
      </v-card-title>

      <v-card-text>
        <v-row align="center" class="mx-0"> </v-row>

        <div class="my-2 subtitle-4 text-truncate">
          {{ clubInfo.category }} | 클럽 멤버 수
        </div>

      </v-card-text>

      <v-divider class="mx-4"></v-divider>

      <v-card-text>
        <v-chip>공개/비공개 표시</v-chip>
         <v-chip>활발/보통/저조</v-chip>
      </v-card-text>

     
    </v-card>
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
          this.$router.push(`/clubDetail?id=${this.clubInfo.id}`);
          break;
      }
    },
  },
};
</script>

<style lang="sass"></style>
