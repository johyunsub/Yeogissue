<template>
  <v-list-item>
    <v-list-item-content>
      <v-row>
        <v-col cols="auto" class="mr-auto">
          <p
            class="subtitle-1 text--primary choice_cursor"
            @click="MovePage('opinionDetail', data.id)"
          >
            {{ data.title }}
          </p>
        </v-col>

        <v-col cols="auto">
          <v-icon small>mdi-thumb-up</v-icon> {{ data.like_users_count }}
        </v-col>
        <v-col cols="auto">
          <v-icon small>far fa-eye</v-icon> {{ data.read_count }}
          <v-icon small color="red">far fa-heart</v-icon>
          {{ data.like_users_count }}
        </v-col>
      </v-row>

      <v-col>
        <div class="text--primary choice_cursor">간단한 내용</div>
      </v-col>

      <!-- 해시태그 -->
      <div class="text--primary ma-6" v-if="data.hashtags.length!=0">
        <v-row class="mr-tp">
            <v-chip-group>
              <v-chip
                color="gray darken-4"
                outlined
                v-for="tag in data.hashtags"
                :key="tag.name"
              >
                <span style="color: black; font-weight: 600">
                  <v-icon small color="pink darken-2">fab fa-slack-hash</v-icon>
                  {{ tag.name }}</span
                >
              </v-chip>
            </v-chip-group>
          <v-col cols="4"></v-col>
        </v-row>
      </div>
      <div class="ma-6">
         <span style="color: purple;"> #{{ data.category }} </span> | 작성자 : {{ data.username }} | 작성일 :
        {{ data.created_at }} |
        <v-icon small color="blue darken-2">far fa-comments</v-icon>
        {{ data.comment_count }} | 댓글종류도 아이콘으로 넣고싶당
      </div>
      <v-divider class="my-2"></v-divider>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: {
    data: { type: Object },
  },
  methods: {
    ...mapActions("opinionStore", ["opinionDetail"]),
    MovePage: function (check, value) {
      switch (check) {
        case "opinionDetail":
          this.$router.push(`/opinionDetail?id=${value}`);
          break;
      }
    },
  },
};
</script>

<style scoped></style>
