<template>
<v-hover 
        v-slot="{ hover }"
        open-delay="200">
    <v-card
    :loading="loading"
    class="mx-auto my-5 elevation-5 choice_cursor { 'on-hover': hover }"
    max-width="250"
    :elevation="hover ? 16 : 2"
    
  >
    <v-img
      height="150"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title class="headline mb-0">제목</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
      </v-row>

      <div class="my-2 subtitle-4">
        카테고리
      </div>

      <div class="body-1">내용</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-text>
        <v-chip>모집중</v-chip>
    </v-card-text>
  </v-card>
</v-hover>
</template>

<style lang="sass" scoped>

</style>