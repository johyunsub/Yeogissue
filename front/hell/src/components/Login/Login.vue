<template>
  <v-dialog v-model="getDialog" max-width="450px" persistent>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-card>
        <div class="headline text-center pt-10">
          로그인
        </div>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Email*"
                  required
                  :rules="emailRules"
                  v-model="logindata.email"
                  @keypress.enter="certCheck"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Password*"
                  type="password"
                  v-model="logindata.password"
                  hint="영문,숫자 포함 8자리 이상 적어주세요."
                  required
                  @keypress.enter="certCheck"
                ></v-text-field>
              </v-col>

              <v-col v-if="accounts_valid" cols="12" sm="12">
                <v-alert dense border="left" type="warning" small>
                  <strong>아이디</strong> 또는 <strong>비밀번호</strong>가 틀렸습니다
                </v-alert>
              </v-col>

              <v-col cols="12" sm="12">
                <v-btn tile block large color="info" :disabled="!valid" @click="certCheck"
                  >로그인</v-btn
                >
              </v-col>

              <v-col cols="12" sm="6" class="mt-3 ml-2">
                <span>비밀번호를 잊으셨습니까?</span>
              </v-col>
              <v-col cols="12" sm="5" class="mt-3">
                <span class="choice_cursor" style="color:#2196f3" @click="forgotpw"
                  >비밀번호 찾기</span
                >
              </v-col>
              <v-col cols="12" sm="6" class="ml-2">
                <span> 회원가입을 하시겠습니까</span>
              </v-col>
              <v-col cols="12" sm="5">
                <span class="choice_cursor" style="color:#2196f3" @click="gojoin">회원가입</span>
              </v-col>

              <v-col cols="12" sm="9"></v-col>
              <v-col cols="12" sm="3"
                ><v-btn color="blue darken-1" text @click="OnOffLoign()">Close</v-btn></v-col
              >
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-form>
  </v-dialog>
</template>

<script>
import { mapActions } from 'vuex';
import axios from 'axios';
import { API_BASE_URL } from '../../config';

export default {
  data: () => ({
    valid: false,
    accounts_valid: false,
    logindata: {
      email: '',
      password: '',
    },
    certdata: '',
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
  }),
  computed: {
    getDialog: {
      get: function() {
        return this.$store.state.dialog;
      },
      set: function() {},
    },
  },

  methods: {
    ...mapActions(['userData']),
    OnOffLoign: function() {
      this.$store.commit('CHANGE_DIALOG', false);
      this.logindata.email = '';
      this.logindata.password = '';
    },
    validate() {
      axios
        .post(`${API_BASE_URL}accounts/api-token-auth/`, this.logindata)
        .then((res) => {
          console.log(res.data);
          this.$store.commit('SET_LOGIN_TOKEN', res.data.token);
          this.$store.commit('SET_USER_INFO', this.logindata);
          this.$store.dispatch('userData', this.logindata.email);
          localStorage.setItem('token', res.data.token);
          localStorage.setItem('email', this.logindata.email);
          this.OnOffLoign();
          // this.$router.push({ name: 'Home' });
          this.accounts_valid = false;
        })
        .catch((err) => {
          console.log(err.response);
          this.accounts_valid = true; //에러일때 노출
        });
    },
    certCheck() {
      axios
        .post(`${API_BASE_URL}accounts/login/`, {
          email: this.logindata.email,
          password: this.logindata.password,
        })
        .then((res) => {
          console.log('인증값' + res.data);

          if (res.data == '1') {
            //인증되있으면
            console.log('인증값 : ' + res.data);
            this.validate();
          } else {
            this.$fire({
              title: '이메일인증이 필요합니다',
              text: '인증페이지로 이동합니다',
              type: 'error',
            }).then((r) => {
              console.log(r.value);
              this.$store.commit('CHANGE_DIALOG', false);
              this.$router.push(`/mypage/cert?email=${this.logindata.email}`);
            });
          }
        });
    },
    loginWithKakao() {
      const params = {
        redirectUri: 'http://localhost:8080/auth',
      };
      window.Kakao.Auth.authorize(params);
    },
    forgotpw() {
      this.$store.commit('CHANGE_DIALOG', false);
      this.$router.push({ name: 'FindPW' });
    },
    gojoin() {
      this.$store.commit('CHANGE_DIALOG', false);
      this.$router.push({ name: 'Join' });
    },
  },
};
</script>
