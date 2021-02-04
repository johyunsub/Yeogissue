<template>
  <v-sheet height="12vh">
    <head>
      <title>The Rock (1996)</title>
      <meta property="og:title" content="The Rock" />
      <meta property="og:type" content="video.movie" />
      <meta property="og:url" content="https://www.imdb.com/title/tt0117500/" />
      <meta property="og:image" content="https://ia.media-imdb.com/images/rock.jpg" />
    </head>
    <div class="title mt-5 ml-2">기사제목ㅇㅇ</div>
    <div class="body-2 mt-3 ml-2">기사내용</div>
    <div class="body-2 mt-8 ml-2" v-if="type === 'club'">코멘트</div>
    <meta
      property="og:url"
      content="https://m.blog.naver.com/PostView.nhn?blogId=chrisphotography&logNo=221285447090&proxyReferer=https:%2F%2Fwww.google.com%2F"
    />
    <v-divider class="my-3"></v-divider>
  </v-sheet>
</template>

<script>
export default {
  props: {
    type: { Type: String },
  },
};
</script>
