import { createInstance } from '../../api/index.js';

const instance = createInstance();

const opinionStore = {
  namespaced: true,
  state: {
    opinions: null,

    opinionPaging: {},
    pagingCnt: 0,

    opinionCategory: null,
  },
  getters: {},
  mutations: {
    SET_OPINIONS(state, opinions) {
      state.opinions = opinions;
    },

    SET_OPINIONPAGING(state, start) {
      state.opinionPaging = {};
      state.pagingCnt = Math.floor(state.opinions.length / 10);
      if (state.opinions.length % 10 != 0) state.pagingCnt++;

      let index = 0;
      for (let i = start; i < start + 10; i++) {
        if (i == state.opinions.length) break;
        state.opinionPaging[index++] = state.opinions[i];
      }
    },
  },
  actions: {
    //조회
    opinionList({ commit }) {
      instance
        .get('/articles/article_list')
        .then((res) => {
          commit('SET_OPINIONS', res.data);
          commit('SET_OPINIONPAGING', 0);
        })
        .catch((err) => console.log(err.response));
    },
    //생성
    opinionCreate({ dispatch }, data) {
      instance
        .post('/articles/article_create/', data)
        .then(() => {
          dispatch('opinionList');
        })
        .catch((err) => console.log(err.response));
    },
  },
};

export default opinionStore;
