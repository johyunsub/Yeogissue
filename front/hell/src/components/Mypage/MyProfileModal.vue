<template>
  <div class="text-center">
    <v-dialog v-model="getDialog" max-width="1000px" persistent>
     
        <v-card>
          <v-card-title>
            <span class="headline"> {{profileData.nickname}} 님의 프로필</span>
          </v-card-title>

         <v-container class="grey lighten-5">
            <v-row rows="8" >
                <figure class="profile_area" id="preview">
                    <img src="https://static.some.co.kr/sometrend/images/mypage/profile/w_01.png" id="picture" class="profileImg">
                </figure>
                <Viewer v-if="profileData.introduce_text != null" :initialValue="profileData.introduce_text" /> 
            <v-col
                cols="12"
                sm="4"
            >   
            
            </v-col>

            <v-col
                cols="12"
                sm="4"
            >   
            </v-col>    

            </v-row>

            <v-row rows="4" >
                {{profileData.email}} 
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
import { Viewer } from "@toast-ui/vue-editor";

export default {
  components: { Viewer },
  data: () => ({
    profile: false,
    //image: '',
    nickname: '',
    introduce_text: '',
    email:'',
   
  }),
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
    }
  },
};
</script>
