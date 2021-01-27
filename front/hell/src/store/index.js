import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //Meun 상태
    drawer: false,
    dialog: false,
    clubDialog: false,
  },
  getters: {
    
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
  },
  actions: {
  },
  modules: {
  }
})
