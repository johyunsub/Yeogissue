import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //Meun 상태
    drawer: false,
    dialog: false,
  },
  getters: {
    getDrawer(state) {
      return state.drawer;
    },
    getDialog(state) {
      return state.dialog;
    },
  },
  mutations: {
    CHANGE_DRAWER(state, drawer) {
      state.drawer = drawer;
    },
    CHANGE_DIALOG(state, dialog) {
      state.dialog = dialog;
    },
  },
  actions: {
  },
  modules: {
  }
})
