<template>
  <v-list-item>

    <v-list-item-content>
      <v-row>
        <v-col cols="auto" class="mr-auto ml-6">
          <p
            class="text--primary choice_cursor"
            @click="MovePage('opinionDetail', data.id)"
            style=" fontSize: 25px; font-weight: bold "
          >
            {{ data.title }}
          </p>
        </v-col>

        <v-col cols="auto">
          <v-icon small>far fa-eye</v-icon> {{ data.read_count }}
          <v-icon small color="red">far fa-heart</v-icon>
          {{ data.like_users_count }}
        </v-col>
      </v-row>

      <!-- 해시태그 -->
      <div class="text--primary ml-8 mb-2 mt-5" v-if="data.hashtags.length != 0">
        <v-row>
          <v-chip-group>
            <v-chip outlined v-for="tag in data.hashtags" :key="tag.name">
              <span style="color: black; font-weight: 600">
                <v-icon small color="pink ">fas fa-hashtag</v-icon>
                {{ tag.name }}</span
              >
            </v-chip>
          </v-chip-group>
          <v-col cols="4"></v-col>
        </v-row>
      </div>
      <div class="ma-6" style="fontSize: 14px;">
        <span style="color:blueviolet;"> #{{ data.category }} </span>  | by
        {{ data.username }} | {{ data.created_at.substr(0, 10) }} |
        <span v-if="!data.comment_type"><v-icon small class="mr-1" color="pink">far fa-comments</v-icon>찬반 토론 중</span>
        <span v-if="data.comment_type"><v-icon small class="mr-1" color="green">far fa-comment</v-icon>토의 중</span> |
        <v-icon small color="blue darken-2">far fa-comment-alt</v-icon>
        댓글 수:{{ data.comment_count }} 
      </div>
      <v-divider class="my-2"></v-divider>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  props: {
    data: { type: Object },
  },
  methods: {
    ...mapActions('opinionStore', ['opinionDetail']),
    MovePage: function(check, value) {
      switch (check) {
        case 'opinionDetail':
          this.$router.push(`/opinionDetail?id=${value}`);
          break;
      }
    },
  },
  created() {
  },
};
</script>

<style></style>
