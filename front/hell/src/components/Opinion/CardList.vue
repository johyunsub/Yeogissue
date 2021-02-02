<template>
  <v-card class="mx-auto mr-tp" max-width="1000" outlined>
    <v-card-text>
      <v-row>
        <v-col cols="auto" class="mr-auto">
          <p class="subtitle-1 text--primary choice_cursor" @click="MovePage('opinionDetail', id)">
            {{ title }}
          </p>
        </v-col>
        <v-col cols="auto"> <v-icon small>mdi-thumb-up-outline</v-icon> 100 </v-col>
      </v-row>
      <p>{{ user }}</p>
      <div class="text--primary choice_cursor">
        간단한 내용
      </div>

      <v-divider class="my-2"></v-divider>
      <div class="text--primary">
        #해시태그
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  props: {
    id: { type: Number },
    title: { type: String },
    user: { type: Number },
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
