<template>
  <v-card outlined max-width="1000" class="ml-10 mt-5">
    <h3 class="ml-10 mt-3">
      <span class="title_text">비밀번호 변경</span>
    </h3>
    <v-simple-table height="300px" class="ml-10 mt-5">
      <tr height="50">
        <td>현재비밀번호</td>
        <td><v-text-field type="password" v-model="modData.currentPW" required></v-text-field></td>
      </tr>
      <tr>
        <td width="20%">변경할 비밀번호</td>
        <td width="70%">
          <v-text-field
            type="password"
            v-model="modData.newPW"
            required
            @input="$v.modData.newPW.$touch()"
            @blur="$v.modData.newPW.$touch()"
            :error-messages="passwordErrors"
          ></v-text-field>
        </td>
      </tr>
      <tr>
        <td>변경할 비밀번호 확인</td>
        <td>
          <v-text-field
            type="password"
            v-model="modData.newPW2"
            required
            @input="$v.modData.newPW2.$touch()"
            @blur="$v.modData.newPW2.$touch()"
            :error-messages="passwordCheckErrors"
          ></v-text-field>
        </td>
      </tr>
      <tr>
        <td></td>
        <td><v-btn class="mr-4" @click="modifyPassword"> 비밀번호 변경</v-btn></td>
        <td></td>
      </tr>
    </v-simple-table>
  </v-card>
</template>
<script>
import { validationMixin } from 'vuelidate';
import { required, minLength, sameAs } from 'vuelidate/lib/validators';

import axios from 'axios';
import { API_BASE_URL } from '../../config';
import { mapState } from 'vuex';

export default {
  mixins: [validationMixin],

  validations: {
    modData: {
      newPW: { required, minLength: minLength(8) },
      newPW2: { required, minLength: minLength(8), sameAsPassword: sameAs('newPW') },
    },
  },
  components: {},
  computed: {
    ...mapState(['userInfo']),
    passwordErrors() {
      const errors = [];
      if (!this.$v.modData.newPW.$dirty) return errors;
      !this.$v.modData.newPW.minLength && errors.push('비밀번호는 최소8자 입니다.');
      !this.$v.modData.newPW.required && errors.push('비밀번호를 입력해주세요.');
      return errors;
    },
    passwordCheckErrors() {
      const errors = [];
      if (!this.$v.modData.newPW2.$dirty) return errors;
      !this.$v.modData.newPW2.minLength && errors.push('비밀번호는 최소8자 입니다.');
      !this.$v.modData.newPW2.required && errors.push('비밀번호를 입력해주세요.');
      !this.$v.modData.newPW2.sameAsPassword && errors.push('패스워드가 일치하지않습니다.');
      return errors;
    },
  },
  data: function() {
    return {
      modData: {
        email: '',
        currentPW: '',
        newPW: '',
        newPW2: '',
      },
      message: '',
    };
  },
  created() {
    this.modData.email = this.userInfo.email;
  },
  methods: {
    modifyPassword() {
      axios
        .post(`${API_BASE_URL}accounts/passwordChange/`, this.modData)
        .then((res) => {
          console.log(res.data);
          if (res.data == '0') {
            //성공
            this.message = '비밀번호가 성공적으로 변경되었습니다!';
            this.successPop();
          } else if (res.data == '1') {
            //비밀번호불일치
            this.message = '비밀번호가 일치하지 않습니다!';
            this.errorPop();
          } else {
            //현재비밀번호 틀림
            this.message = '현재 비밀번호가 틀렸습니다';
            this.errorPop();
          }
        })
        .catch((err) => console.log(err.response));
    },
    successPop() {
      this.$fire({
        title: `${this.message}`,
        type: 'success',
      }).then(() => {
        this.$router.push({ name: 'Home' });
        this.message = '';
      });
    },
    errorPop() {
      this.$fire({
        title: `${this.message}`,
        type: 'error',
      });
      this.message = '';
    },
  },
};
</script>
