import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

import opinionStore from './modules/opinionStore';
import clubStore from './modules/clubStore';

export default new Vuex.Store({
  state: {
    //Meun 상태
    drawer: false,
    dialog: false,
    clubDialog: false,
    clubDetailUrlDialog: false,

    //Club 리스트 페이지
  },
  getters: {
    getClubs(state) {
      return state.clubs;
    },
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
  },
  actions: {},
  modules: {
    opinionStore: opinionStore,
    clubStore: clubStore,
  },
});
