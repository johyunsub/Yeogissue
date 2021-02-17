<template>
  <div class="text-center">
    <v-dialog v-model="getDialog" max-width="1000px" persistent>
     
        <v-card>
          <v-card-title>
            <span class="headline font-weight-bold"> {{profileData.nickname}} 님의 프로필</span>
          </v-card-title>

         <v-container class="grey lighten-5">
            <v-row rows="8" >
                <!-- <figure class="profile_area" id="preview">
                    <img src="https://static.some.co.kr/sometrend/images/mypage/profile/w_01.png" id="picture" class="profileImg">
                </figure> -->
                <v-avatar
                  class="profile ma-4"
                  size="164"
                  tile
                >
                 <img :src="url+this.profileData.image.substr(1)" alt="">
                </v-avatar>
              <v-col cols="1"></v-col>
              <v-col
                  cols="2"
                  class="mt-4"
              >   
                <v-row class="mt-1  text-h6">
                  닉네임 :
                </v-row>
                <v-row class="mt-9  text-h6">
                  아이디 :
                </v-row>
                <v-row class="mt-9  text-h6">
                  나의 소개 :
                  
                </v-row>
              </v-col>    
              <v-col
                  cols="2"
                  sm="4"
                  class="my-4"
              >  
                <v-row class="mt-1 font-weight-bold text-h6">
                  {{profileData.nickname}} 
                </v-row> 
                <v-row class="mt-9 font-weight-bold text-h6">
                  {{profileData.email}} 
                </v-row> 
                <v-row class="mt-9 font-weight-bold text-h6">
                  <!-- <Viewer v-if="profileData.introduce_text != null" :initialValue="profileData.introduce_text" />  -->
                  {{profileData.introduce_text}} 
                </v-row>
              </v-col>    
              
            </v-row>

            <v-row rows="4" >
                
            </v-row>
            

        </v-container>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="OnOffProfile()">Close</v-btn>
          </v-card-actions>
        </v-card>
     
    </v-dialog>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

import "codemirror/lib/codemirror.css"; 
import "@toast-ui/editor/dist/toastui-editor.css"; 
// import { Viewer } from "@toast-ui/vue-editor";
import { API_BASE_URL } from '../../config';

// import axios from "axios";

export default {
  components: {  },
  data: function() {
    return {
      profile: false,
      image: '',
      nickname: '',
      introduce_text: '',
      email:'',
      url:'',
      newimage:'',
    }
  },
  created(){
    this.url = API_BASE_URL;
    console.log("aDADAD"+this.profileData.introduce_text)
  
  },
  computed: {
    ...mapState(['profileData']),
    getDialog: {
      get: function() { 
        return this.$store.state.profile;
      },
      set: function() {
        
   
      },
    },
  },

  methods: {
    ...mapActions(['userData']),
    OnOffProfile: function() {
      this.$store.commit('CHANGE_PROFILE', false);
    },
   
  },
};
</script>
