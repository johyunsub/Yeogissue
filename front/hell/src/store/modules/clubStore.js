import { createInstance } from '../../api/index.js';

const instance = createInstance();

const clubStore = {
  namespaced: true,
  state: {
    clubs: '',
  },
  getters: {},
  mutations: {
    SET_CLUBS(state, payload) {
      state.clubs = payload;
    },
  },
  actions: {
    clubList({ commit }) {
      instance
        .get('/club/')
        .then((res) => {
          commit('SET_CLUBS', res.data);
        })
        .catch((err) => console.log(err.response));
    },
  },
};

export default clubStore;
