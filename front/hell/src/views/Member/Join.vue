<template>
  <form>
    <v-text-field
      v-model="email"
      :error-messages="emailErrors"
      label=" E-mail "
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>

    <v-text-field
      v-model="name"
      :error-messages="nameErrors"
      :counter="10"
      label=" 이름 "
      required
      @input="$v.name.$touch()"
      @blur="$v.name.$touch()"
    ></v-text-field>

    <v-text-field
      v-model="nickname"
      :error-messages="nicknameErrors"
      :counter="10"
      label=" 닉네임 ( 10자 이하로 입력해주세요 ) "
      required
      @input="$v.nickname.$touch()"
      @blur="$v.nickname.$touch()"
    ></v-text-field>

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
      v-model="checkbox"
      :error-messages="checkboxErrors"
      label="여기issue 사이트에 가입하시겠습니까?"
      required
      @change="$v.checkbox.$touch()"
      @blur="$v.checkbox.$touch()"
    ></v-checkbox>

    <v-btn class="mr-4" @click="submit">submit</v-btn>
    <v-btn @click="clear">clear</v-btn>
  </form>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, minLength, maxLength, email, sameAs } from 'vuelidate/lib/validators'
  import axios from 'axios'
  import { API_BASE_URL } from "../../config";

  export default {
    mixins: [validationMixin],

    validations: {
      name: { required },
      nickname: { required, maxLength: maxLength(10) },
      email: { required, email },
      password: { required, minLength: minLength(8) },
      passwordCheck: { required, minLength: minLength(8), sameAsPassword: sameAs('password') },
      checkbox: {
        checked (val) {
          return val
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
        show5: false
    }),

    computed: {
      checkboxErrors () {
        const errors = []
        if (!this.$v.checkbox.$dirty) return errors
        !this.$v.checkbox.checked && errors.push(' 동의해주세요')
        return errors
      },
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.required && errors.push('ID를 입력해주세요.')
        return errors
      },
      nicknameErrors () {
        const errors = []
        if (!this.$v.nickname.$dirty) return errors
        !this.$v.nickname.maxLength && errors.push('닉네임은 10자이하여야 합니다')
        !this.$v.nickname.required && errors.push('닉네임을 입력해주세요.')
        return errors
      },
      passwordErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.minLength && errors.push('비밀번호는 최소8자 입니다.')
        !this.$v.password.required && errors.push('비밀번호를 입력해주세요.')
        return errors
      },
      passwordCheckErrors () {
        const errors = []
        if (!this.$v.passwordCheck.$dirty) return errors
        !this.$v.passwordCheck.minLength && errors.push('비밀번호는 최소8자 입니다.')
        !this.$v.passwordCheck.required && errors.push('비밀번호를 입력해주세요.')
        !this.$v.passwordCheck.sameAsPassword && errors.push('패스워드가 일치하지않습니다.')
        return errors
      },
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('이메일 형식으로 입력해주세요.')
        !this.$v.email.required && errors.push('이메일을 입력해주세요.')
        return errors
      },
    },

    methods: {
      submit () {
        this.joinData.name = this.name;
        this.joinData.nickname = this.nickname;
        this.joinData.password = this.password;
        this.joinData.passwordConfirmation = this.passwordCheck;
        this.joinData.email = this.email;
        console.log(this.joinData)
        this.signup();
        this.$v.$touch()
      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.nickname = ''
        this.password = ''
        this.passwordCheck = ''
        this.email = ''
        this.checkbox = false
      },
      signup: function () {
        console.log(this.joinData.name + "<<<")
        axios.post(`${API_BASE_URL}accounts/signup/`, this.joinData)
        .then(() => {
          this.$store.commit("CHANGE_DRAWER", false);
          this.$router.push({ name: 'Home' })
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
  }
</script>