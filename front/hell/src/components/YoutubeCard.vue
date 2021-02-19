<template>
  <v-list-item>
    <v-list-item-content>
      <div class="cover">
        <v-img
          class="left choice_cursor"
          :src="data.image"
          max-height="180"
          max-width="320"
          @click="MovePage"
        >
        </v-img>
        <div class="right mt-2">
          <div class="text--primary choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="fontSize: 18px; color: #64B5F6">> {{ data.comment }}</p>
          </div>
          <p
            class="text--primary choice_cursor"
            style=" fontSize: 18px; font-weight: bold "
            @click="MovePage"
          >
            {{ data.title }}
          </p>
          <div class="text--primary mt-5 choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="color: #666;">{{ data.description }}</p>
          </div>
          <div class="text--primary mt-5 choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p style="color: #6a7e88">생성일 : {{ data.updated_at.substr(0, 10) }}</p>
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
  data: () => ({
    dialog: false,
    videoUrl: "",
  }),

  methods: {
    MovePage() {
      this.$store.commit("issueStore/SET_ISSUE_DETAIL_YOUTUBE_DIALOG", true);
      let url = this.data.url.replace('watch?v=', 'embed/');
      let position = url.indexOf('&');
      
      if(position != -1) url = url.substr(0,position);
      
      this.$store.commit(
        "issueStore/SET_ISSUE_DETAIL_VIDEO_URL",
        `<iframe
            src="${url}"
            style="width:800px; height:500px"
          ></iframe>`
      );
    },
  },
};
</script>
