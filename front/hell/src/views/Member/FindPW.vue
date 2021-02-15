<template>
  <v-container borderd="1px">
        <div class="contentInner1">
            <h2 class="mypagepw_contentsTitle">
                <span class="title_text" >비밀번호 찾기 </span>
            </h2>
            <h3 class="mypagepw_contentsSubTitle">
                <span class="subtitle_text" >가입 시 입력한 이메일을 입력해주세요 </span>
            </h3>
            
            <v-simple-table height="400px">
                <tr height="50">
                    <td>이메일</td>
                    <td><v-text-field
                        required
                        v-model="email"
                    ></v-text-field></td>
                    <td></td>
                </tr>
                
                <tr>
                    <td></td>
                    <td><v-btn class="mr-4"  @click="sendPW"> 임시비밀번호발송</v-btn></td>
                    <td></td>
                </tr>
            </v-simple-table>
        </div>
  </v-container>
</template>

<script>
import axios from 'axios'
import { API_BASE_URL } from "../../config";

export default {
  data: function(){
    return{
      email:'',
      message: '',
    }
  },
  methods: {
      sendPW() {
          axios
              .post(`${API_BASE_URL}accounts/sendPassword/`, {email : this.email})///// 이메일 존재 찾기 , 이메일 전송까지
              .then((res) => {
                  console.log(res.data);
                  if(res.data == '0'){ //성공
                  this.message = '이메일로 임시비밀번호가 전송되었습니다!'
                  this.successPop();
                  }
                  else{ //이메일 잘못 입력된 경우
                  this.message = '존재하지 않는 이메일 입니다.'
                  this.errorPop();
                  }
              })
              .catch((err) => 
              console.log(err.response),
          );
      },
      successPop(){
          this.$fire({
          title: `${this.message}`,
          type: "success",
          })
          .then(() => {
              this.$router.push({ name: 'Home' })
              this.message='';
          })
      },
      errorPop(){
          this.$fire({
          title: `${this.message}`,
          type: "error",
          })
          this.message='';
      },
  }
}
</script>