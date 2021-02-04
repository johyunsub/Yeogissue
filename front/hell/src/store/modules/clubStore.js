import { createInstance } from '../../api/index.js';

const instance = createInstance();

const clubStore = {
  namespaced: true,
  state: {
    clubs: '',
  },
  getters: {},
  mutations: {
    SET_CLUBS(state, club) {
      state.clubs = club;
    },
  },
  actions: {
    // 조회
    clubList({ commit }) {
      instance
        .get('/club/')
        .then((res) => {
          commit('SET_CLUBS', res.data);
        })
        .catch((err) => console.log(err.response));
    },

    // 생성
    clubCreate({ dispatch }, data) {
      instance
        .post('/club/create/', data)
        .then(() => {
          dispatch('clubList');
        })
        .catch((err) => console.log(err.response));
    },
  },
};

export default clubStore;
