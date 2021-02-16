<template>
  <v-list-item>
    <v-list-item-content>
      <div class="cover">
        <v-img
          class="left choice_cursor"
          :src="urlData.image"
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
            {{ urlData.title }}
          </p>
          <div class="text--primary choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="color: #666">{{ urlData.description }}</p>
          </div>

          <div class="text--primary choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="color: #64B5F6">{{ urlData.comment }}</p>
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

      console.log(data.qqqq.url, '21313');
      window.open(`${data.qqqq.url}`);
    },
  },

  created() {
    console.log(this.data());
  },
};
</script>
