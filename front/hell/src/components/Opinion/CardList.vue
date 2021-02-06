<template>
  <v-card class="mx-auto mr-tp" max-width="1000" outlined>
    <v-card-text>
      <v-row>
        <v-col cols="auto" class="mr-auto">
          <p class="subtitle-1 text--primary choice_cursor" @click="MovePage('opinionDetail', data.id)">
            {{ data.title }}
          </p>
        </v-col>
        <v-col cols="auto"> <v-icon small>mdi-thumb-up-outline</v-icon> {{ data.like_users_count}} </v-col>
      </v-row>
      <p>작성자 : {{ data.user }}</p>
      <div class="text--primary choice_cursor">
        간단한 내용
      </div>

      <v-divider class="my-2"></v-divider>
      <div class="text--primary">
        #해시태그
        <v-row class="mr-tp">
          <v-chip-group mandatory>
            <v-chip v-for="tag in data.hashtags" :key="tag.name"> 
              {{ tag.name }}
            </v-chip>
          </v-chip-group>
          <v-col cols="4"></v-col>
        </v-row>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  props: {
    data: {type: Object},
    
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
};
</script>

<style scoped></style>
