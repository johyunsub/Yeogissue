import { createInstance } from '../../api/index.js';

const instance = createInstance();

const opinionStore = {
  namespaced: true,
  state: {
    opinions: null,
  },
  getters: {},
  mutations: {
    SET_OPINIONS(state, opinions) {
      state.opinions = opinions;
    },
  },
  actions: {
    //조회
    opinionList({ commit }) {
      instance
        .get('/articles/articles_list')
        .then((res) => {
          commit('SET_OPINIONS', res.data);
        })
        .catch((err) => console.log(err.response.data));
    },
  },
};

export default opinionStore;
