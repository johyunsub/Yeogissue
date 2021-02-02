//type에 따라 찬반, 의견으로 버튼이 보이고 안보이고 성질에 따라
<template>
  <v-card class="mt-2" max-width="1000" outlined>
    <v-card-text>
      <v-row>
        <v-col>
          <div class="text--primary ">
            {{ updated_at }}
          </div>
        </v-col>
        <v-col cols="auto"> <v-icon small>mdi-thumb-up-outline</v-icon> 100 </v-col>
        <v-col cols="auto"> <comment-menu /></v-col>
      </v-row>

      <v-row>
        <v-col cols="2">
          <v-avatar class="profile ml-10" color="grey" size="80">
            <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
          </v-avatar>
          <div class="title ml-10 mt-1">
            {{ user }}
          </div>
        </v-col>

        <v-col cols="9">
          <span class="ml-5">{{ content }}</span>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import CommentMenu from './CommentMenu.vue';
export default {
  components: { CommentMenu },
  props: {
    id: { type: Number },
    opinion_type: { type: Boolean },
    content: { type: String },
    created_at: { type: String },
    updated_at: { type: String },
    user: { type: Number },
    article: { type: Number },
  },
};
</script>

<style scoped>
.mr-le {
  margin-left: 15px;
}
</style>
