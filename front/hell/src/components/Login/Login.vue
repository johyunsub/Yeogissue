<template>
  <div class="text-center">
    <v-dialog v-model="getDialog" max-width="600px">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-card>
          <v-card-title>
            <span class="headline">로그인</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    label="Email*"
                    required
                    :rules="emailRules"
                    v-model="logindata.email"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Password*"
                    type="password"
                    v-model="logindata.password"
                    hint="영문,숫자 포함 8자리 이상 적어주세요."
                    required
                  ></v-text-field>
                </v-col>

                <v-col v-if="accounts_valid" cols="12" sm="12">
                  <v-alert dense border="left" type="warning" small>
                    <strong>아이디</strong> 또는 <strong>비밀번호</strong>가 틀렸습니다
                  </v-alert>
                </v-col>

                <v-col cols="12" sm="12">
                  <v-btn tile x-large color="info" :disabled="!valid" @click="validate"
                    >로그인</v-btn
                  >
                </v-col>

                <v-divider></v-divider>
                <v-col cols="12" sm="12">
                  <v-btn tile x-large color="yellow darken-2" @click="loginWithKakao">카카오</v-btn>
                </v-col>

                <v-col cols="12" sm="6">
                  비밀번호를 잊으셨습니까?
                </v-col>
                <v-col cols="12" sm="6">
                  <v-btn text color="info" @click="forgotpw">비밀번호 찾기</v-btn>
                </v-col>
                <v-col cols="12" sm="6">
                  회원가입을 하시겠습니까
                </v-col>
                <v-col cols="12" sm="6">
                  <v-btn text color="info" @click="gojoin">회원가입</v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="OnOffLoign()">Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import axios from 'axios';
import { API_BASE_URL } from "../../config";

export default {
  data: () => ({
    dialog: false,
    valid: false,
    accounts_valid: false,
    logindata: {
      email: '',
      password: '',
    },
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
      set: function() {
      },
    },
  },

  methods: {
    ...mapActions(['userData']),
    OnOffLoign: function() {
      this.$store.commit('CHANGE_DIALOG', false);
    },
    validate() {
      axios
        .post(`${API_BASE_URL}accounts/api-token-auth/`, this.logindata)
        .then((res) => {
          console.log(res);
          this.$store.commit('SET_LOGIN_TOKEN', res.data.token);
          this.userData(this.logindata.email);
          localStorage.setItem('token', res.data.token);
          localStorage.setItem('email', this.logindata.email);
          this.OnOffLoign();
          this.accounts_valid = false;
        })
        .catch((err) => {
          console.log(err.response);
          this.accounts_valid = true;
        });
    },
    loginWithKakao() {
      const params = {
        redirectUri: 'http://localhost:8080/auth',
      };
      window.Kakao.Auth.authorize(params);
    },
    forgotpw() {
      this.$router.push({ name: 'Home' });
    },
    gojoin() {
      this.$router.push({ name: 'Home' });
    },
  },
};
</script>
