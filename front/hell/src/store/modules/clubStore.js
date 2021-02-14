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
    clubDetailManegerBtn: false,  //관리창, 게시글창 컨트롤
    clubDetailIsManager: false,   //관리자인지
    clubDetailIsMember: false,    //멤버인지
    clubDetailIsWaiting: false,   //클럽가입대기중인지

    //클럽 모달 변수
    clubDialog: false,
    clubDetailUrlDialog: false,

    //클럽 멤버 관리 리스트 
    clubManageMemberList: [],
    clubManageJoinList: [],

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
    SET_CLUB_Is_Manager(state, check) {
      state.clubDetailIsManager = check;
    },

    //Club Modal
    CLUB_CREATE_DIALOG(state, dialog) {
      state.clubDialog = dialog;
    },
    CLUB_DETAIL_URL_DIALOG(state, dialog) {
      state.clubDetailUrlDialog = dialog;
    },

    //클럽멤버 관리
    SET_MANAGE_MEMBER_LIST(state, data) {
      state.clubManageMemberList = data;
    },
    SET_MANAGE_JOIN_LIST(state, data) {
      state.clubManageJoinList = data;
    },

    //클럽멤버인지
    SET_IS_MEMBER(state, data){
      state.clubDetailIsMember = data;
    },

    //클럽가입신청대기 중인지
    SET_IS_WAITING(state, data){
      console.log("데이터 변경 " + data)
      state.clubDetailIsWaiting = data;
    }
    
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
    clubDetail({ commit },id) {
      console.log(id,'club_id')
      instance
        .get(`club/club_detail/${id}/`)
        .then((res) => {
          console.log(res)
          commit('SET_CLUB_DETAIL', res.data);
          
        })
        .catch((err) => console.log(err.response));
    },

    // Url 조회
    // clubDetailUrlList({ state, commit }) {
    clubDetailUrlListNews({ state, commit }) {
      console.log(state.clubData.id)
      instance
        .get(`club/club_article_list/${state.clubData.id}/news/`)
        .then((res) => {
          commit('SET_CLUB_DETAIL_URL', res.data);
        })
        .catch((err) => console.log(err.response));
    },
    clubDetailUrlListYoutube({ state, commit }) {
      console.log(state.clubData.id)
      instance
        .get(`club/club_article_list/${state.clubData.id}/youtube/`)
        .then((res) => {
          commit('SET_CLUB_DETAIL_URL', res.data);
        })
        .catch((err) => console.log(err.response));
    },
    clubDetailUrlListetc({ state, commit }) {
      console.log(state.clubData.id)
      instance
        .get(`club/club_article_list/${state.clubData.id}/etc/`)
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


    // 클럽 멤버 관리
    clubMangeList({ state, commit }, data) {
      instance
        .post(`club/member_check/${state.clubData.id}/`, data)
        .then((res) => {
          if(data.type == ''){
            commit('SET_MANAGE_JOIN_LIST', res.data);
          }
          else{
            commit('SET_MANAGE_MEMBER_LIST', res.data);
          }
        })
        .catch((err) => console.log(err.response));
    },
    
    //클럽 가입신청
    clubJoin({ state,commit }, data) {
      instance
        .post(`club/club_signup/${state.clubData.id}/`, data )
        .then(() => {
          commit('SET_IS_WAITING', true);
        })
    },

    //클럽 가입요청 승인
    clubManageJoinApprove({ state, dispatch }, data){
      instance
        .post(`club/member_approve/${state.clubData.id}/`, data)
        .then(() => {
          dispatch('clubMangeList', {type: ''});
        })
        .catch((err) => console.log(err.response));
    },

    //클럽 가입요청 거부
    clubManageJoinDisApprove({ state, dispatch }, data){
      console.log(data)
      instance
        .delete(`club/member_delete/${state.clubData.id}/${data.member}/`)
        .then(() => {
          dispatch('clubMangeList', {type: ''});
        })
        .catch((err) => console.log(err.response));
    },

    //클럽 탈퇴
    clubLeave({state, dispatch }, data){
      instance
        .post(`club/club_member_delete/${state.clubData.id}/`, data)
        .then(()=>{
          dispatch('isClubMember', {type: '승인'});
        })
    },

    //클럽멤버인지
    isClubMember({ state, commit }, data) {
      instance
      .post(`club/member_check/${state.clubData.id}/`, {type: '승인'})
      .then((res) => {
        commit('SET_MANAGE_MEMBER_LIST', res.data);
        for(var i=0; i<res.data.length; i++){
          if(res.data[i].user === data.user){
            commit('SET_IS_MEMBER', true);
            return;
          }
        }
        commit('SET_IS_MEMBER', false);
        instance
          .post(`club/member_check/${state.clubData.id}/`, {type: ''})
          .then((res1) => {
            for(var j=0; j<res1.data.length; j++){
              if(res1.data[j].user === data.user){
                commit('SET_IS_WAITING', true);
                return;
              }
            }
              commit('SET_IS_WAITING', false);
              return;
            })
        })
        .catch((err) => console.log(err.response));
    },
  },
};

export default clubStore;
