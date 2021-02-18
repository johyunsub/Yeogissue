import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import { createInstance } from "../api/index.js";
const instance = createInstance();

import opinionStore from "./modules/opinionStore";
import clubStore from "./modules/clubStore";
import issueStore from "./modules/issueStore";

export default new Vuex.Store({
  state: {
    //로그인 정보
    isLoginToken: "",

    // 유저 정보
    userInfo: {
      email: "",
      id: 0,
      nickname: "",
      introduce_text: "",
      image: "",
    },

    //프로필 유저 정보
    profileData: {},
    myEmotion: [],

    // 알림
    alarms: [],

    //Meun 상태
    drawer: false,
    dialog: false,

    profile: false,
  },
  getters: {},
  mutations: {
    //Login
    SET_LOGIN_TOKEN(state, token) {
      state.isLoginToken = token;
      localStorage.setItem("token", token);
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

    CHANGE_PROFILE(state, profile) {
      state.profile = profile;
    },

    SET_PROFILE_DATA(state, data) {
      state.profileData = data;
    },

    //나의 감정분석
    SET_MY_EMOTION(state, data) {
      let result_map = Object.keys(data).map(function(key) {
        return [String(key), data[key]];
      });
      state.myEmotion = result_map;
    },

    //d알람
    SET_USER_ALARM(state, data) {
      state.alarms = data;
    },
  },
  actions: {
    // 알림
    alarm({ state, commit }) {
      instance
        .post(`/accounts/alarm/`, { user: state.userInfo.id })
        .then((res) => {
          console.log(res.data, "12211212");
          commit("SET_USER_ALARM", res.data);
        })
        .catch((err) => console.log(err.response));
    },
    //유저 정보 받아오기
    userData({ dispatch, commit }, data) {
      console.log("index usderdata " + data);
      instance
        .post("/accounts/get_user/", { email: data })
        .then((res) => {
          commit("SET_USER_INFO", res.data);
          dispatch("alarm");
        })
        .catch((err) => console.log(err.response));
    },
    //유저 프로필 정보
    getProfile({ commit }, id) {
      console.log("index profile " + id);
      instance
        .post("/accounts/get_user_id/", { id: id })
        .then((res) => {
          commit("SET_PROFILE_DATA", res.data);
        })
        .catch((err) => console.log(err.response));
    },

    userUpdate({ dispatch }, data) {
      instance
        .post(`/accounts/user_update/`, data)
        .then(() => {
          dispatch("userData", data.email);
        })
        .catch((err) => console.log(err.response));
    },

    getEmotion({ commit, state }) {
      instance
        .post(`/articles/my_emotion/`, { user: state.userInfo.id })
        .then((res) => {
          console.log(this.emotionData);
          commit("SET_MY_EMOTION", res.data);
        })
        .catch((err) => console.log(err.response));
    },

    //로그아웃
    userLogout({ commit }) {
      commit("SET_LOGIN_TOKEN", "");
      commit("SET_USER_INFO", {});
      localStorage.removeItem("token");
      localStorage.removeItem("email");
    },
  },
  modules: {
    opinionStore: opinionStore,
    clubStore: clubStore,
    issueStore: issueStore,
  },
});
