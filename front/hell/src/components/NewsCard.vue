<template>
  <!-- <v-sheet height="12vh">
    <div class="title mt-10 ml-2">기사제목ㅇㅇ</div>
    <div class="body-2 mt-3 ml-2">Url : {{ urlData.url }}</div>
    <div class="body-2 mt-8 ml-2" v-if="type === 'club'">코멘트 : {{ urlData.comment }}</div>
    <v-divider class="my-3"></v-divider>
  </v-sheet> -->
  <v-list-item>
    <v-list-item-content>
      <div>내용 : {{urlData.comment}}</div>
      <div>작성일 : {{urlData.created_at}}</div>
      <div>사이트 이름 :{{urlData.site_name}}</div>
      <div>작성자 : {{urlData.user}}</div>
      <!-- <div>{{urlData.title}}</div>
      <div>{{urlData.description}}</div>
      <div>{{urlData.image}}</div> -->
      <div class="cover">
        <v-img
          class="left choice_cursor"
          :src="urlData.image"
          max-height="100"
          max-width="200"
          @click="MovePage"
        >
        </v-img>
        <div class="right mt-2">
          <p
            class="text--primary choice_cursor"
            style=" fontSize: 18px; font-weight: bold "
            @click="MovePage"
          >
            {{ urlData.title }}
          </p>
          <div class="text--primary mt-5 choice_cursor" style="fontSize: 13px;" @click="MovePage">
            <p>{{ urlData.description }}</p>
          </div>
        </div>
      </div>
      <v-divider class="my-4"></v-divider>
      <v-dialog v-model="dialog" max-width="700">
        <iframe src="urlData.video" height="400"></iframe>
      </v-dialog>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  props: {
    type: String,
    urlData: Object,
  },
  methods: {
    data() {
      return { 
        qqqq: this.urlData,
        dialog: false, 
      };
    },
    MovePage() {
      // this.dialog = true;
      const data = this.data();

      console.log(data.qqqq.url,'21313');
      window.open(`${data.qqqq.url}`);
    },
  },
  
  
  created() {
    console.log(this.data());
  },
};
</script>
