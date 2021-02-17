<template>
  <v-container>
    <v-row>
      <v-col cols="3" class="mr-auto"></v-col>
      <v-col>
        <v-sheet height="5vh" />
        <v-sheet width="600" height="80vh" rounded elevation="2">
          <div class="headline text-center pt-7 pb-10">
            회원가입
          </div>
          <form style="text-align: center;">
            <v-row>
              <v-col cols="8">
                <v-text-field
                  v-model="email"
                  :error-messages="emailErrors"
                  label=" E-mail "
                  required
                  @input="$v.email.$touch()"
                  @blur="$v.email.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn class="mt-4" @click="emailCheck" v-bind:disabled="email.length < 1"
                  >이메일 중복확인</v-btn
                >
              </v-col>
            </v-row>

            <v-text-field
              v-model="name"
              :error-messages="nameErrors"
              label=" 이름 "
              required
              @input="$v.name.$touch()"
              @blur="$v.name.$touch()"
            ></v-text-field>

            <v-row>
              <v-col cols="8">
                <v-text-field
                  v-model="nickname"
                  :error-messages="nicknameErrors"
                  :counter="10"
                  label=" 닉네임 ( 10자 이하로 입력해주세요 ) "
                  required
                  @input="$v.nickname.$touch()"
                  @blur="$v.nickname.$touch()"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <v-btn class="mt-4" @click="nicknameCheck" v-bind:disabled="nickname.length < 1"
                  >닉네임 중복확인</v-btn
                >
              </v-col>
            </v-row>

            <v-text-field
              v-model="password"
              :error-messages="passwordErrors"
              :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show4 ? 'text' : 'password'"
              label=" 비밀번호 "
              @click:append="show4 = !show4"
              @input="$v.password.$touch()"
              @blur="$v.password.$touch()"
            ></v-text-field>

            <v-text-field
              v-model="passwordCheck"
              :error-messages="passwordCheckErrors"
              :append-icon="show5 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show5 ? 'text' : 'password'"
              label=" 비밀번호확인 "
              @click:append="show5 = !show5"
              @input="$v.passwordCheck.$touch()"
              @blur="$v.passwordCheck.$touch()"
            ></v-text-field>

            <v-checkbox
              off-icon="$checkboxOff"
              v-model="checkbox"
              :error-messages="checkboxErrors"
              label="여기issue 사이트에 가입하시겠습니까?"
              required
              @change="$v.checkbox.$touch()"
              @blur="$v.checkbox.$touch()"
            ></v-checkbox>

            <v-btn class="mr-4" :disabled="!valid" @click="submit">가입하기</v-btn>
            <v-btn @click="clear">초기화</v-btn>
          </form>
        </v-sheet>
      </v-col>
      <v-col cols="1" class="mr-auto"></v-col>
    </v-row>
  </v-container>
</template>

<script>
import { validationMixin } from 'vuelidate';
import { required, minLength, maxLength, email, sameAs } from 'vuelidate/lib/validators';
import axios from 'axios';
import { API_BASE_URL } from '../../config';

export default {
  mixins: [validationMixin],

  validations: {
    name: { required },
    nickname: { required, maxLength: maxLength(10) },
    email: { required, email },
    password: { required, minLength: minLength(8) },
    passwordCheck: { required, minLength: minLength(8), sameAsPassword: sameAs('password') },
    checkbox: {
      checked(val) {
        this.valid = val;
        return val;
      },
    },
  },

  data: () => ({
    joinData: {
      nickname: '',
      name: '',
      password: '',
      passwordConfirmation: '',
      email: '',
    },
    name: '',
    nickname: '',
    password: '',
    passwordCheck: '',
    email: '',
    checkbox: false,
    show4: false,
    show5: false,
    timer: '',
    valid: false,

    overlapNick: false,
    overlapEmail: false,

    message: '',
  }),

  computed: {
    checkboxErrors() {
      const errors = [];
      if (!this.$v.checkbox.$dirty) return errors;
      !this.$v.checkbox.checked && errors.push('동의해주세요');
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.required && errors.push('ID를 입력해주세요.');
      return errors;
    },
    nicknameErrors() {
      const errors = [];
      if (!this.$v.nickname.$dirty) return errors;
      !this.$v.nickname.maxLength && errors.push('닉네임은 10자이하여야 합니다');
      !this.$v.nickname.required && errors.push('닉네임을 입력해주세요.');
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.minLength && errors.push('비밀번호는 최소8자 입니다.');
      !this.$v.password.required && errors.push('비밀번호를 입력해주세요.');
      return errors;
    },
    passwordCheckErrors() {
      const errors = [];
      if (!this.$v.passwordCheck.$dirty) return errors;
      !this.$v.passwordCheck.minLength && errors.push('비밀번호는 최소8자 입니다.');
      !this.$v.passwordCheck.required && errors.push('비밀번호를 입력해주세요.');
      !this.$v.passwordCheck.sameAsPassword && errors.push('패스워드가 일치하지않습니다.');
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push('이메일 형식으로 입력해주세요.');
      !this.$v.email.required && errors.push('이메일을 입력해주세요.');
      return errors;
    },
  },

  methods: {
    //이메일중복체크
    emailCheck() {
      axios
        .post(`${API_BASE_URL}accounts/userid_check/`, { email: this.email })
        .then((res) => {
          console.log(res.data);
          if (res.data == 'success') {
            this.message = '사용할 수 있는 이메일입니다.';
            this.successPop();
            this.overlapEmail = true;
          } else {
            this.message = '이미 존재하는 이메일입니다';
            this.errorPop();
            this.email = '';
          }
        })
        .catch((err) => console.log(err.response));
    },
    //닉네임중복체크
    nicknameCheck() {
      console.log(this.nickname);
      axios
        .post(`${API_BASE_URL}accounts/nickname_check/`, { nickname: this.nickname })
        .then((res) => {
          console.log(res.data);
          if (res.data == 'success') {
            this.message = '사용할 수 있는 닉네임입니다.';
            this.successPop();
            this.overlapNick = true;
          } else {
            this.message = '이미 존재하는 닉네임입니다';
            this.errorPop();
            this.nickname = '';
          }
        })
        .catch((err) => console.log(err.response));
    },
    checkForm() {
      let check = true;

      if (this.password.length > 10 || this.password.length == 0) {
        check = false;
        this.message = '비밀번호를 정확히 입력해주세요';
      }

      if (this.nickname.length > 10 || this.nickname.length == 0) {
        check = false;
        this.message = '닉네임을 정확히 입력해주세요';
      }

      if (this.password != this.passwordCheck) {
        check = false;
        this.message = '비밀번호가 일치하지 않습니다';
      }
      if (this.overlapNick == false) {
        check = false;
        this.message = '닉네임 중복체크를 해주세요';
      }

      if (this.overlapEmail == false) {
        check = false;
        this.message = '이메일 중복체크를 해주세요';
      }

      return check;
    },
    successPop() {
      this.$fire({
        title: `${this.message}`,
        type: 'success',
      });
      this.message = '';
    },
    errorPop() {
      this.$fire({
        title: `${this.message}`,
        type: 'error',
      });
      this.message = '';
    },
    errorDialog() {
      this.$fire({
        //에러창
        position: 'center',
        //icon: 'success',
        title: `${this.message}`,
        showConfirmButton: false,
        timer: 1000,
      });
    },
    submit() {
      if (!this.checkForm()) {
        this.errorDialog();
        return;
      }
      this.joinData.name = this.name;
      this.joinData.nickname = this.nickname;
      this.joinData.password = this.password;
      this.joinData.passwordConfirmation = this.passwordCheck;
      this.joinData.email = this.email;
      console.log(this.joinData);
      this.loading();
      this.signup();
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.name = '';
      this.nickname = '';
      this.password = '';
      this.passwordCheck = '';
      this.email = '';
      this.checkbox = false;
    },
    signup: function() {
      console.log(this.joinData.name + '<<<');
      axios
        .post(`${API_BASE_URL}accounts/signup/`, this.joinData)
        .then(() => {
          this.$fire({
            //에러창
            position: 'center',
            //icon: 'success',
            title: '가입 완료 되었습니다',
            showConfirmButton: false,
            timer: 500,
          });
          this.$router.push(`/mypage/cert?email=${this.email}`);
        })
        .catch((err) => {
          console.log(err);
          this.$fire({
            //에러창
            position: 'center',
            //icon: 'success',
            title: '형식에 맞게 입력해주세요!',
            showConfirmButton: false,
            timer: 1000,
          });
        });
    },
    loading() {
      this.$fire({
        //회원가입 로딩창
        position: 'center',
        //icon: 'success',
        title: '회원 가입 중입니다..',
        showConfirmButton: false,
        timer: 3200,
      });
    },
  },
};
</script>

<style scoped>
.v-text-field {
  width: 400px;
}
form {
  margin: 0 auto;

  width: 500px;
}
</style>
