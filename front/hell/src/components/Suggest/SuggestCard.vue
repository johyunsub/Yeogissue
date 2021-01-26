<template>
    <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <v-img
      height="150"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title>제목</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
      </v-row>

      <div class="my-4 subtitle-1">
        카테고리
      </div>

      <div>내용</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>제안 상태</v-card-title>

    <v-card-text>
        <v-chip>완료</v-chip>
    </v-card-text>
  </v-card>
</template>