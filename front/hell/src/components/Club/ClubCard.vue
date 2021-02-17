<template>
  <v-hover v-slot="{ hover }" open-delay="200">
    <v-col cols="12">
      <v-card
        class="mx-auto my-5 elevation-5 choice_cursor { 'on-hover': hover }"
        max-width="500"
        min-width="500"
        :elevation="hover ? 16 : 2"
        @click="MovePage('detail')"
      >
        <div class="d-flex flex-no-wrap">
          <img 
            style="width: 150px; height:150px"
            :src="image"
          />
          <div class="ml-4 mt-2">
            <v-card-title @click="MovePage('detail')" class="headline mb-0 h6"
              >{{ clubInfo.title }}
            </v-card-title>
            <v-card-text>
              <v-row align="center" class="mx-0"> </v-row>

              <div class="my-2 subtitle-4 text-truncate">
                <span style="color: blueviolet">{{ clubInfo.category }} </span>
              </div>
              <div>
                <v-icon v-if="clubInfo.is_private" small class="mb-1" color="red accent-3">fas fa-lock</v-icon>
                <v-icon v-if="!clubInfo.is_private" small color=""></v-icon>
                <v-icon class="ml-3 mr-1 mb-1" small color="blue">fas fa-user-friends</v-icon>
                <span style="color: blue">{{ clubInfo.member_cnt }}</span>
              </div>
            </v-card-text>
          </div>
        </div>
      </v-card>
    </v-col>
  </v-hover>
</template>

<script>
import { mapState } from 'vuex';
import { API_BASE_URL } from "../../config";

export default {
  name: 'clubCard',
  computed: {
    ...mapState('clubStore', ['clubManageMemberList','clubData']),
    ...mapState(['userInfo']),
  },
  data() {
    return {
      show: false,
      image: 'https://cdn.vuetifyjs.com/images/cards/cooking.png',
    };
  },
  props: {
    clubInfo: Object,
  },
  created() {
    this.setImage();
 
  },
  methods: {
    setImage: function() {
      if (this.clubInfo.image) 
      { this.image = API_BASE_URL + this.clubInfo.image.substr(1);}
      else if (this.clubInfo.category == "IT/과학") {this.image = `${API_BASE_URL}media/images/%EA%B3%BC%ED%95%99.JPG` }
      else if (this.clubInfo.category == "경제") {this.image = `${API_BASE_URL}media/images/%EA%B2%BD%EC%A0%9C.JPG`}
      else if (this.clubInfo.category == "사회") {this.image = `${API_BASE_URL}media/images/%EC%82%AC%ED%9A%8C.JPG`}
      else if (this.clubInfo.category == "생활") {this.image = `${API_BASE_URL}media/images/%EC%83%9D%ED%99%9C.JPG`}
      else if (this.clubInfo.category == "스포츠") {this.image = `${API_BASE_URL}media/images/%EC%8A%A4%ED%8F%AC%EC%B8%A0.JPG`}
      else if (this.clubInfo.category == "연예") {this.image = `${API_BASE_URL}media/images/%EC%97%B0%EC%98%88.JPG`}
      else if (this.clubInfo.category == "정치") {this.image = `${API_BASE_URL}media/images/%EC%A0%95%EC%B9%98.JPG`}
      else if (this.clubInfo.category == "해외") {this.image = `${API_BASE_URL}media/images/%ED%95%B4%EC%99%B8.JPG`}
    //   this.image = 'http://i4d108.p.ssafy.io:8000' + this.userInfo.image;
    },
    MovePage: function(check) {
      switch (check) {
        case 'detail':
          this.isLogin();
          break;
      }
    },
    isLogin() {
      if (this.userInfo != null) {
        this.$router.push(`/clubDetail?id=${this.clubInfo.id}`);
      } else {
        this.$fire({
          title: '로그인후 이용하실 수 있습니다.',
          type: 'error',
        });
      }
    },
  },
};
</script>

<style lang="sass"></style>
