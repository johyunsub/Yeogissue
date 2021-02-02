<template>
  <v-menu bottom left>
    <template v-slot:activator="{ on, attrs }">
      <v-btn icon v-bind="attrs" v-on="on">
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </template>

    <v-list>
      <!-- user 정보 알아서 items 조절 -->
      <v-list-item v-for="(item, i) in items" :key="i">
        <v-list-item-title class="choice_cursor back-gray">{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  data: () => ({
    items: [{ title: '수정' }, { title: '삭제' }, { title: '신고' }],
    items2: [{ title: '신고' }],
  }),
};
</script>
