<template>
  <v-menu bottom left>
    <template v-slot:activator="{ on, attrs }">
      <v-btn icon v-bind="attrs" v-on="on">
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </template>

    <div v-if="!isLoginToken == ''">
      <v-list>
        <v-list-item
          class="choice_cursor back-gray"
          v-for="(item, i) in items"
          :key="i"
          @click="updateComment(item.title, id)"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </div>

    <div v-if="isLoginToken == ''">
      <v-list>
        <v-list-item
          class="choice_cursor back-gray"
          v-for="(item, i) in items2"
          :key="i"
          @click="updateComment(item.title, id)"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </div>
  </v-menu>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  props: {
    id: { Type: String },
  },
  computed: {
    ...mapState(['isLoginToken', 'userInfo']),
  },
  data: () => ({
    items: [{ title: '수정' }, { title: '삭제' }, { title: '신고' }],
    items2: [{ title: '신고' }],
  }),
  methods: {
    ...mapActions('opinionStore', ['opinionCommentDelete', 'opinionBadComment']),
    updateComment(content, id) {
      if (this.isLoginToken == '') {
        this.$store.commit('CHANGE_DIALOG', true);
        return;
      }

      if (content == '수정') {
        this.$emit('CommentUp');
      } else if (content == '삭제') {
        this.opinionCommentDelete(id);
        this.$toasted.show('댓글이 삭제되었습니다.', {
          theme: 'outline',
          position: 'bottom-center',
          duration: 1000,
        });
      } else if (content == '신고') {
        this.opinionBadComment(id);
        this.$toasted.show('신고 되었습니다. 감사합니다.', {
          theme: 'outline',
          position: 'bottom-center',
          duration: 1000,
        });
      }
    },
  },
};
</script>
