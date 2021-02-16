<template>
  <v-list-item>
    <v-list-item-content>
      <div class="cover">
        <v-img
          class="left choice_cursor"
          :src="urlData.image"
          max-height="130"
          max-width="250"
          @click="MovePage"
        >
        </v-img>
        <div class="right mt-1">
          <div class="text--primary choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="fontSize: 18px; color: #64B5F6"> > {{ urlData.comment }}</p>
          </div>
          <p
            class="text--primary choice_cursor"
            style=" fontSize: 18px; font-weight: bold "
            @click="MovePage"
          >
            {{ urlData.title }}
          </p>
          <div class="text--primary choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="color: #666">{{ urlData.description }}</p>
          </div>
        </div>
      </div>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  props: {
    type: String,
    urlData: Object,
  },
  methods: {
    data() {
      return {
        qqqq: this.urlData,
        dialog: false,
      };
    },
    MovePage() {
      // this.dialog = true;
      const data = this.data();

      console.log(data.qqqq.url, "21313");
      window.open(`${data.qqqq.url}`);
    },
    getDate() {
      let a = this.data.image.indexOf("202");
      return this.data.image.substr(a, 10);
    },
  },

  created() {
    console.log(this.data());
  },
};
</script>
