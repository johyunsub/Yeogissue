<template>
  <v-container >
  
      <h1> 이메일 인증 </h1>
      <h2> {{certData.email}}  로 발송된 인증번호를 입력해주세요 </h2>
      <v-row rows="12" sm="3"  class="py-3">
        <v-text-field
          label=""
          single-line
          v-model="certData.token"
        ></v-text-field>
      </v-row>
      <v-row rows="12" sm="3" class="py-3">
          <v-btn tile x-large color="info"  @click="tokenCheck"> 인증확인 </v-btn> 
     </v-row>       
    
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';
import axios from 'axios';
import { API_BASE_URL } from "../../config"; 

export default {
  data:function(){
    return{
      certData:{
        email : '',
        token: '',
      }
    }
  },
  methods: {
    ...mapActions(['userData']),
    tokenCheck() {
      axios
        .post(`${API_BASE_URL}accounts/email_check/`, this.certData)
        .then((res) => {
          console.log(res.data);
          if(res.data == 'success'){
            this.$fire({
              title: "인증되었습니다!",
              text: " 다시 로그인해주세요!",
              type: "success",
            }).then(r => {
              console.log(r.value);
              this.$store.commit("CHANGE_DIALOG", true);
              this.$router.push({ name: 'Home' });
            });
          }
          else{
            this.$fire({
              title: "인증실패",
              text: "인증번호를 확인해주세요",
              type: "error" ,
            }); 
          }

        })
    }
  },
  created(){
    this.certData.email = this.$route.query.email;
  },
}

</script>