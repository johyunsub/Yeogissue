import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //Meun 상태
    drawer: false,
  },
  getters: {
    getDrawer(state) {
      return state.drawer;
    },
  },
  mutations: {
    CHANGE_DRAWER(state, drawer) {
      state.drawer = drawer;
    },
  },
  actions: {
  },
  modules: {
  }
})
