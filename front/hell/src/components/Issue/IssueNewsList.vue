<template>
  <v-list-item>
    <v-list-item-content>
      <div class="cover mt-2">
        <v-img
          class="left choice_cursor"
          :src="data.image"
          max-height="130"
          max-width="250"
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
          <div class="text--primary mt-2 choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="color: #6a7e88" v-if="data.site_name !=''">출처 : {{ data.site_name }} | {{ getDate() }}</p>
          </div>
          <div class="text--primary mt-2 choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p class="target_new" style="color: #666">{{ data.description }}</p>
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
    getDate(){
      let a = this.data.image.indexOf('202');
      return this.data.image.substr(a,10);
    }
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
