<template>
  <v-dialog v-model="getDialog" max-width="800px">
    <div ref="cont"></div>
    <button style="display:none" id="chageYoutubeDialog" @click="OnOffMenu">ddd</button>
  </v-dialog>
</template>

<script>
import $ from "jquery";
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState("issueStore", ["issueDetailYoutubeDialog", "issueDetailVideoUrl"]),
    getDialog: {
      get: function() {
        return this.issueDetailYoutubeDialog;
      },
      set: function() {},
    },
  },
  updated() {
    console.log("들어옴");
    this.$refs.cont.innerHTML = this.issueDetailVideoUrl;
    $(document).ready(function() {
      $('.v-overlay').on('click', function() {
        $('#chageYoutubeDialog').trigger('click');
      });
    });

  },
  methods:{
      OnOffMenu(){
        this.$store.commit("issueStore/SET_ISSUE_DETAIL_YOUTUBE_DIALOG", false);
        this.$refs.cont.innerHTML = "";
      }
  }
};
</script>
