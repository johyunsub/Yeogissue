<template>
  <v-list-item>
    <v-list-item-content>
      <div class="cover">
        <v-img class="left" :src="data.image" max-height="100" max-width="200"> </v-img>
        <div class="right mt-2">
          <p
            class="text--primary choice_cursor"
            style=" fontSize: 18px; font-weight: bold "
            @click="MovePage"
          >
            {{ data.title }}
          </p>
          <div class="text--primary mt-5 choice_cursor" style="fontSize: 13px;" @click="MovePage">
            {{ data.description }}
          </div>
        </div>
      </div>
      <v-divider class="my-4"></v-divider>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  props: {
    data: { type: Object },
  },
  data: () => ({}),
  methods: {
    MovePage() {
      window.open(`${this.data.link}`);
    },
  },
};
</script>

<style scoped>
.cover {
  display: inline-block;
  margin-top: -10px;
}
.left {
  float: left;
  margin-right: 20px;
  border-radius: 7px;
}
</style>
