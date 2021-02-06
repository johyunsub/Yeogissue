import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

import { createInstance } from '../api/index.js';
const instance = createInstance();

import opinionStore from './modules/opinionStore';
import clubStore from './modules/clubStore';

export default new Vuex.Store({
  state: {
    //로그인 정보
    isLoginToken: '',

    // 유저 정보
    userInfo: {
      email : '',
      id : '',
      nickname : '',
    },

    //Meun 상태
    drawer: false,
    dialog: false,
  },
  getters: {},
  mutations: {
    //Login
    SET_LOGIN_TOKEN(state, token) {
      state.isLoginToken = token;
      localStorage.setItem('token', token);
    },

    //userInfo
    SET_USER_INFO(state, data) {
      state.userInfo = data;
    },

    //NavBar Modal
    CHANGE_DRAWER(state, drawer) {
      state.drawer = drawer;
    },
    CHANGE_DIALOG(state, dialog) {
      state.dialog = dialog;
    },
  },
  actions: {
    //유저 정보 받아오기
    userData({ commit }, data) {
      console.log("index userdata "+data)
      instance
        .post('/accounts/get_user/', { email: data })
        .then((res) => {
          commit('SET_USER_INFO', res.data);
          console.log("유저 정보는 " + data + " id는 " + res.data.id)
        })
        .catch((err) => console.log(err.response));
    },

    //로그아웃
    userLogout({ commit }) {
      commit('SET_LOGIN_TOKEN', '');
      commit('SET_USER_INFO', null);
      localStorage.removeItem('token');
      localStorage.removeItem('email');
                                             
    },
  },
  modules: {
    opinionStore: opinionStore,
    clubStore: clubStore,
  },
});
