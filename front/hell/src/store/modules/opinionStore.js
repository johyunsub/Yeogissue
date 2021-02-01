import { createInstance } from '../../api/index.js';

const instance = createInstance();

const opinionStore = {
  namespaced: true,
  state: {
    opinions: null,

    opinionPaging: {},
    pagingCnt: 0,

    opinionCategory: null,

    // 디테일 변수
    opinionData: null,
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
    SET_OPINIONDETAIL(state, opinion) {
      state.opinionData = opinion;
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

    //수정
    opinionUpdate({ commit }, data) {
      instance
        .put(`/articles/${data.id}/`, data)
        .then(() => {
          commit('SET_OPINIONDETAIL', data);
        })
        .catch((err) => console.log(err.response));
    },

    //삭제
    opinionDelete({ commit }, id) {
      instance
        .delete(`/articles/${id}/`)
        .then(() => {
          commit('SET_OPINIONDETAIL', null);
        })
        .catch((err) => console.log(err.response));
    },

    // 디테일
    opinionDetail({ commit }, id) {
      instance
        .get(`/articles/${id}`)
        .then((res) => {
          commit('SET_OPINIONDETAIL', res.data);
        })
        .catch((err) => console.log(err.response));
    },
  },
};

export default opinionStore;
