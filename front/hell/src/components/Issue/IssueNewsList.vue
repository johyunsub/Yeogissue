<template>
  <v-list-item>
    <v-list-item-content>
      <div class="cover mt-1">
        <v-img
          class="left choice_cursor"
          :src="data.image"
          max-height="100"
          max-width="200"
          @click="MovePage"
        >
        </v-img>
        <div class="right mt-1">
          <p
            class="text--primary choice_cursor"
            style=" fontSize: 18px; font-weight: bold "
            @click="MovePage"
          >
            {{ data.title }}
          </p>
          <div class="text--primary mt-5 choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="color: #666">{{ data.description }}</p>
          </div>
        </div>
      </div>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  props: {
    data: { type: Object },
  },
  data: () => ({
    dialog: false,
  }),
  methods: {
    MovePage() {
      // this.dialog = true;
      window.open(`${this.data.link}`);
    },
  },
};
</script>

<style>
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
