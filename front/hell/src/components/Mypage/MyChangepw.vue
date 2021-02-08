<template>
    <v-container borederd="1px">
        <div class="contentInner">
            <h3 class="mypagepw_contentsTitle">
                <span class="title_text">비밀번호 변경</span>
            </h3>
            <v-simple-table height="300px">
                <tr height="50">
                    <td>현재비밀번호</td>
                    <td><v-text-field
                        label="Password*"
                        type="password"
                        required
                    ></v-text-field></td>
                    <td>뭉뭉뭉</td>
                </tr>
                <tr >
                    <td>변경할 비밀번호</td>
                    <td><v-text-field
                        label="Password*"
                        type="password"
                        v-model="logindata.password"
                        required
                    ></v-text-field></td>
                    <td>뭉뭉뭉</td>
                </tr>
                <tr>
                    <td>변경할 비밀번호 확인</td>
                    <td><v-text-field
                    label="Password*"
                    type="password"
                    required
                  ></v-text-field></td>
                    <td>뭉뭉뭉</td>
                </tr>
                <tr>
                    <td>뭉뭉뭉</td>
                    <td><v-btn class="mr-4"  @click="submit">가입하기</v-btn></td>
                    <td>뭉뭉뭉</td>
                </tr>
            </v-simple-table>
        </div>
    </v-container>
</template>
<script>
// import axios from 'axios'
// import { API_BASE_URL } from "../../config";

export default {
    components: {
      //  Editor
    },
    computed: {
        //...mapState(['userInfo']),
    },
    data: function() {
        return {
            email:'',
            oldpwd:'',
            newpwd:'',
            newpwdcheck:'',

        };
    },
    created() {
        this.modData.email = this.userInfo.email;
    },
    methods: {
        modify() {
           // this.modData.introduce = this.$refs.toastuiEditor.invoke("getMarkdown");
            //this.$store.dispatch('userUpdate', this.modData);
            console.log("지금"+this.modData);
            this.$fire({
              title: "회원 정보가 수정되었습니다.",
              type: "success",
            }).then(r => {
              console.log(r.value);      
              this.$router.push({ name: 'Home' });
            });
        }
    }
}
</script>