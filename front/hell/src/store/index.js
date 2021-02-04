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
    userInfo: null,

    //Meun 상태
    drawer: false,
    dialog: false,

    //클럽 모달 변수
    clubDialog: false,
    clubDetailUrlDialog: false,
  },
  getters: {
    getClubs(state) {
      return state.clubs;
    },
  },
  mutations: {
    //Login
    SET_LOGIN_TOKEN(state, token) {
      state.isLoginToken = token;
      // localStorage.setItem('token', token);
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

    //Club Modal
    CLUB_CREATE_DIALOG(state, dialog) {
      state.clubDialog = dialog;
    },
    CLUB_DETAIL_URL_DIALOG(state, dialog) {
      state.clubDetailUrlDialog = dialog;
    },
  },
  actions: {
    //유저 정보 받아오기
    userData({ commit }, data) {
      instance
        .post('/accounts/get_user/', { email: data })
        .then((res) => {
          commit('SET_USER_INFO', res.data);
        })
        .catch((err) => console.log(err.response));
    },

    //로그아웃
    userLogout({ commit }) {
      console.log('되나?');
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
