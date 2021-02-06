<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-card
      class="mx-auto my-5 elevation-5 choice_cursor { 'on-hover': hover }"
      max-width="250"
      :elevation="hover ? 16 : 2"
      @click="MovePage('detail')"
    >
      <v-img height="150" src="https://cdn.vuetifyjs.com/images/cards/cooking.png"></v-img>

      <!-- 글짜 ... 해주는거 text-truncate -->
      <v-card-title class="headline mb-0 h6">{{ clubInfo.title }}</v-card-title>

      <v-card-text>
        <v-row align="center" class="mx-0"> </v-row>

        <div class="my-2 subtitle-4 text-truncate">
          {{ clubInfo.category }}
        </div>

        <div class="body-1 text-truncate">{{ clubInfo.content }}</div>
      </v-card-text>

      <v-divider class="mx-4"></v-divider>

      <v-card-text>
        <v-chip>모집중</v-chip>
      </v-card-text>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: 'clubCard',
  computed: {},
  data() {
    return {};
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

<style lang="sass" scoped></style>
