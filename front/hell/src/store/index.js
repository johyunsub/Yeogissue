import Vue from 'vue';
import Vuex from 'vuex';
import axios from "axios";

Vue.use(Vuex);

import opinionStore from './modules/opinionStore';

export default new Vuex.Store({
  state: {
    //Meun 상태
    drawer: false,
    dialog: false,
    clubDialog: false,
    clubDetailUrlDialog: false,

    //Club 리스트 페이지
    clubs: "",
  },
  getters: {
    getClubs(state) {
      return state.clubs;
    }
  },
  mutations: {
    CHANGE_DRAWER(state, drawer) {
      state.drawer = drawer;
    },
    CHANGE_DIALOG(state, dialog) {
      state.dialog = dialog;
    },

    CLUB_CREATE_DIALOG(state, dialog) {
      state.clubDialog = dialog;
    },

    CLUB_DETAIL_URL_DIALOG(state, dialog) {
      state.clubDetailUrlDialog = dialog;
    },
    GET_CLUBS(state, payload) {
      state.clubs = payload;
    },
  },
  actions: {
    GET_CLUBS(context) {
      return axios
      .get("http://127.0.0.1:8000/club/")
      .then((response) => {
        context.commit("GET_CLUBS", response);
        console.log("ok")
      })
    },
  },
  modules: {
    opinionStore: opinionStore,
  },
});
