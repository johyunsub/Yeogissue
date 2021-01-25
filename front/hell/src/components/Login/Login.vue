<template>
  <v-row justify="center">
    <v-dialog v-model="getDialog" persistent max-width="600px">
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
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Password*"
                    type="password"
                    hint="영문,숫자 포함 8자리 이상 적어주세요."
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-btn
                    tile
                    x-large
                    color="info"
                    :disabled="!valid"
                    @click="validate"
                    >로그인</v-btn
                  >
                </v-col>
                <v-col cols="12" sm="12">
                  <v-btn
                    tile
                    x-large
                    color="yellow darken-2"
                    @click="loginWithKakao"
                    >카카오</v-btn
                  >
                </v-col>
                
                <v-col cols="12" sm="6">
                  비밀번호를 잊으셨습니까?
                </v-col>
                <v-col cols="12" sm="6">
                  <v-btn
                    text
                    color="info"
                    >비밀번호 찾기</v-btn
                  >
                </v-col>
                <v-col cols="12" sm="6">
                  회원가입을 하시겠습니까
                </v-col>
                <v-col cols="12" sm="6">
                  <v-btn
                    text
                    color="info"
                    >회원가입</v-btn
                  >
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="OnOffLoign()"
              >Close</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    valid: true,
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
  }),
  computed: {
    getDialog: {
      get: function () {
        return this.$store.state.dialog
      },
      set: function () {
        }
      }
  },

  methods: {
    OnOffLoign: function() {
      this.$store.commit('CHANGE_DIALOG', false);
    },
    validate() {
      this.$refs.form.validate();
    },
    loginWithKakao() {
      const params = {
          redirectUri: "http://localhost:8080/auth",
      };
      window.Kakao.Auth.authorize(params);
    },
  },
};
</script>
