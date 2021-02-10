//type에 따라 찬반, 의견으로 버튼이 보이고 안보이고 성질에 따라
<template>
  <v-card class="mt-2" max-width="1000" outlined>
    <v-card-text>
      <v-row>
        <v-col>
          <div class="text--primary ">
            {{ username }} | {{ updated_at }}
          </div>
        </v-col>
        <v-col v-if="!getLike" cols="auto" class="choice_cursor" @click="thumbUp"> 
          <v-icon small>mdi-thumb-up-outline</v-icon> {{ like_users_count }} 
        </v-col>
        <v-col v-if="getLike" cols="auto" class="choice_cursor" @click="thumbUp"> 
          <v-icon small>mdi-thumb-up</v-icon> {{ like_users_count }} 
        </v-col>
        <v-col cols="auto"> <comment-menu /></v-col>
      </v-row>

      <v-row>
        <v-col cols="2">
        
        <div v-if="emotion=='기쁨'">
        <i class="far fa-grin-squint"></i></div>
        
        <div v-else-if="emotion=='신뢰'">
        <i class="far fa-grin-stars"></i></div>

        <div v-else-if="emotion=='놀라움'">
        <i class="far fa-fa-surprise"></i></div>

        <div v-else-if="emotion=='슬픔'">
        <i class="far fa-fa-sad-tear"></i></div>

        <div v-else-if="emotion=='공포'">
        <i class="far fa-fa-grimace"></i></div>

        <div v-else-if="emotion=='기대'">
        <i class="far fa-kiss-beam"></i></div>

        <div v-else-if="emotion=='혐오'">
        <i class="far fa-dizzy"></i></div>

        <div v-else>
        <i class="far fa-angry"></i></div>

          
        
          <!-- <v-avatar class="profile ml-10" color="grey" size="80">
            <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
          </v-avatar> -->
          
        </v-col>

        <v-col cols="9">
          <span class="ml-5">{{ content }}</span>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import CommentMenu from './CommentMenu.vue';
import { mapState } from 'vuex';
import axios from 'axios';
import { API_BASE_URL } from "../../config";

export default {
  components: { CommentMenu },
  computed: {
    ...mapState('opinionStore', ['opinionComment']),
    getLike: {
      get: function(){
        if(this.like_users.includes(this.$store.state.userInfo.id)){
            return true;
          }
        return false;
      }
    }
  },
  props: {
    id: { type: Number },
    opinion_type: { type: Boolean },
    content: { type: String },
    created_at: { type: String },
    updated_at: { type: String },
    user: { type: Number },
    article: { type: Number },
    emotion: { type: String},
    like_users_count: { type: Number },
    like_users: { type: Array },
    username: {type: String},
  },
  data: () =>{
    return {
      isLike: false,
      // likeCnt: this.like_users_count,
      articleno: '',
      // article_id: this.article,
      // like_count: this.like_users_count,
    }
  },
  methods: {

    thumbUp() {
      axios.post(`${API_BASE_URL}articles/${this.id}/comment_like/`, {user: this.$store.state.userInfo.id})
        .then((res)=>{
          console.log(res);
          if(this.getLike) {
            this.like_users_count--;
            console.log(this.like_users_count)
          }else{
            this.like_users_count++;
            console.log(this.like_users_count)
          }
          this.$store.dispatch('opinionStore/opinionDetail',this.article)
        })
        .catch((err) =>{
          console.log(err.response);
        })

    }
  },
  created() {

  }
};
</script>

<style scoped>
.mr-le {
  margin-left: 15px;
}
</style>
