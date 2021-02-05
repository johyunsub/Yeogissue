import { createInstance } from '../../api/index.js';

const instance = createInstance();

const clubStore = {
  namespaced: true,
  state: {
    //클럽 전체
    clubs: '',

    //클럽 디테일 정보
    clubData: '',

    //Url 정보
    clubDetailUrl: null,

    //MamagerOnOff
    clubDetailManegerBtn: false,

    //클럽 모달 변수
    clubDialog: false,
    clubDetailUrlDialog: false,
  },
  getters: {},
  mutations: {
    SET_CLUBS(state, club) {
      state.clubs = club;
    },
    SET_CLUB_DETAIL(state, club) {
      state.clubData = club;
    },
    SET_CLUB_DETAIL_URL(state, url) {
      state.clubDetailUrl = url;
    },

    SET_CLUB_MANAGER_BTN(state, check) {
      state.clubDetailManegerBtn = check;
    },

    //Club Modal
    CLUB_CREATE_DIALOG(state, dialog) {
      state.clubDialog = dialog;
    },
    CLUB_DETAIL_URL_DIALOG(state, dialog) {
      state.clubDetailUrlDialog = dialog;
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

    // 수정
    clubUpdate({ state, dispatch }, data) {
      instance
        .put(`/club/club_detail/${state.clubData.id}/`, data)
        .then(() => {
          dispatch('clubDetail', state.clubData.id);
        })
        .catch((err) => console.log(err.response));
    },

    // 디테일
    clubDetail({ commit }, id) {
      instance
        .get(`club/club_detail/${id}`)
        .then((res) => {
          commit('SET_CLUB_DETAIL', res.data);
        })
        .catch((err) => console.log(err.response));
    },

    // Url 조회
    clubDetailUrlList({ state, commit }) {
      instance
        .get(`club/club_article_list/${state.clubData.id}`)
        .then((res) => {
          commit('SET_CLUB_DETAIL_URL', res.data);
        })
        .catch((err) => console.log(err.response));
    },

    // Url 등록
    clubDetailUrlCreate({ dispatch }, data) {
      instance
        .post(`club/club_article/`, data)
        .then(() => {
          dispatch('clubDetailUrlList');
        })
        .catch((err) => console.log(err.response));
    },

    // Url 수정
    clubDetailUrlUpdate({ dispatch }, data) {
      instance
        .put(`club/club_article_detail/2/`, data)
        .then(() => {
          dispatch('clubDetailUrlList');
        })
        .catch((err) => console.log(err.response));
    },
  },
};

export default clubStore;
