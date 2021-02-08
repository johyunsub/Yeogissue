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
          <div>감정{{emotion}}</div>
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
// import axios from 'axios';
// import { API_BASE_URL } from "../../config";

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
    }
  },
  methods: {
    thumbUp() {
      console.log(this.id +" <<<<<값이 왜 안받아와지냐 진짜;")
      this.$emit('take')
      // axios.post(`${API_BASE_URL}articles/${this.id}/comment_like/`, {user: this.$store.state.userInfo.id})
      if(this.getLike) {
        // this.opinionData.like_users_count--;
      }else{
        // this.opinionData.like_users_count++;
      }
      console.log(this.id)
      this.opinionDetail(this.id);
      // if(this.like_users.includes(this.$store.state.userInfo.id))
      
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
