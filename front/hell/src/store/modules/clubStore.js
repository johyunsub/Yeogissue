import { createInstance } from '../../api/index.js';

const instance = createInstance();

const clubStore = {
  namespaced: true,
  state: {
    //클럽 전체
    clubs: '',
    clubsPaging: {},
    clubsPaginCnt: 0,
    clubsCategory: null,

    //클럽 디테일 정보
    clubData: '',

    //Url 정보
    clubDetailUrl: null,

    //MamagerOnOff
    clubDetailManegerBtn: false, //관리창, 게시글창 컨트롤
    clubDetailIsManager: false, //관리자인지
    clubDetailIsMember: false, //멤버인지
    clubDetailIsWaiting: false, //클럽가입대기중인지

    //클럽 모달 변수
    clubDialog: false,
    clubDetailUrlDialog: false,

    //클럽 멤버 관리 리스트
    clubManageMemberList: [],
    clubManageJoinList: [],
    clubManageArticleList: [],

    //쓰레기 값 저장
    demo: '',
  },
  getters: {},
  mutations: {
    SET_CLUBS(state, club) {
      state.clubs = club;
    },
    SET_CLUBS_PAGING(state, start) {
      state.clubsPaging = {};
      state.clubsPaginCnt = Math.floor(state.clubsCategory.length / 10);
      if (state.clubsCategory.length % 10 != 0) state.clubsPaginCnt++;

      let index = 0;
      for (let i = start; i < start + 10; i++) {
        if (i == state.clubsCategory.length) break;
        state.clubsPaging[index++] = state.clubsCategory[i];
      }
    },
    SET_CLUBS_CATEGORY(state, category) {
      state.clubsCategory = [];
      let index = 0;
      //전체 보기이면 그대로 저장
      if (category == '전체') {
        state.clubsCategory = state.clubs;
        return;
      }

      //카테고리 분류
      for (let i = 0; i < state.clubs.length; i++) {
        if (state.clubs[i].category == category) {
          state.clubsCategory[index++] = state.clubs[i];
        }
      }
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
    SET_IS_MEMBER(state, data) {
      state.clubDetailIsMember = data;
    },

    //클럽가입신청대기 중인지
    SET_IS_WAITING(state, data) {
      console.log('데이터 변경 ' + data);
      state.clubDetailIsWaiting = data;
    },

    SET_DD(state, str){
      state.demo = str;
    }
  },
  actions: {
    // 조회
    clubList({ commit }) {
      instance
        .get('/club/')
        .then((res) => {
          commit('SET_CLUBS', res.data);
          commit('SET_CLUBS_CATEGORY', '전체');
          commit('SET_CLUBS_PAGING', 0);
        })
        .catch((err) => console.log(err.response));
    },

    // 생성
    clubCreate({ commit }, data) {
      instance
        .post('/club/create/', data)
        .then(() => {
          commit('SET_DD','dd');
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
      console.log(id, 'club_id');
      instance
        .get(`club/club_detail/${id}/`)
        .then((res) => {
          commit("SET_CLUB_DETAIL", res.data);
        })
        .catch((err) => console.log(err.response));
    },

    // Url 조회
    clubDetailUrlListNews({ state, commit }) {
      console.log(state.clubData.id);
      instance
        .get(`club/club_article_list/${state.clubData.id}/news/`)
        .then((res) => {
          console.log(res.data);
          commit('SET_CLUB_DETAIL_URL', res.data);
        })
        .catch((err) => console.log(err.response));
    },
    clubDetailUrlListYoutube({ state, commit }) {
      console.log(state.clubData.id);
      instance
        .get(`club/club_article_list/${state.clubData.id}/youtube/`)
        .then((res) => {
          commit('SET_CLUB_DETAIL_URL', res.data);
        })
        .catch((err) => console.log(err.response));
    },
    clubDetailUrlListetc({ state, commit }) {
      console.log(state.clubData.id);
      instance
        .get(`club/club_article_list/${state.clubData.id}/etc/`)
        .then((res) => {
          commit('SET_CLUB_DETAIL_URL', res.data);
        })
        .catch((err) => console.log(err.response));
    },

    // Url 등록
    clubDetailUrlCreate({ dispatch }, data) {
      let dd =data.category;
      instance
        .post(`club/club_article/`, data)
        .then(() => {
          console.log("카테고리 -"+dd)
          if(dd == 'News'){
            console.log("URL 등록 뉴스 잘 됨")
            dispatch('clubDetailUrlListNews');
          }
          else if(dd == 'Youtube')dispatch('clubDetailUrlListYoutube');
          else dispatch('clubDetailUrlListetc');
        })
        .catch((err) => console.log(err.response));
    },

    // Url 수정
    clubDetailUrlUpdate({ dispatch }, data) {
      instance
        .put(`club/club_article_detail/2/`, data)
        .then(() => {
          if(data.category == 'News')dispatch('clubDetailUrlListNews');
          else if(data.category == 'Youtube')dispatch('clubDetailUrlListYoutube');
          else dispatch('clubDetailUrlListetc');
        })
        .catch((err) => console.log(err.response));
    },

    //url삭제
    clubDetailUrlDelete({ state }, data) {
      instance.delete(`club/club_article_detail/${data}/`).then(() => {
        for (var i = 0; i < state.clubManageArticleList.length; i++) {
          if (state.clubManageArticleList[i].id == data) {
            state.clubManageArticleList.splice(i, 1);
            break;
          }
        }
        // dispatch('clubManageArticle');
      });
    },

    // 클럽 멤버 관리
    clubMangeList({ state, commit }, data) {
      instance
        .post(`club/member_check/${state.clubData.id}/`, data)
        .then((res) => {
          if (data.type == '') {
            commit('SET_MANAGE_JOIN_LIST', res.data);
          } else {
            commit('SET_MANAGE_MEMBER_LIST', res.data);
          }
        })
        .catch((err) => console.log(err.response));
    },

    //클럽 가입신청
    clubJoin({ state, commit }, data) {
      instance.post(`club/club_signup/${state.clubData.id}/`, data).then(() => {
        if(state.clubData.is_private){
          commit('SET_IS_WAITING', true);
        }else{
          commit('SET_IS_MEMBER', true)
        }
      });
    },

    //클럽 가입요청 승인
    clubManageJoinApprove({ state, dispatch }, data) {
      instance
        .post(`club/member_approve/${state.clubData.id}/`, data)
        .then(() => {
          dispatch('clubMangeList', { type: '' });
        })
        .catch((err) => console.log(err.response));
    },

    //클럽 가입요청 거부
    clubManageJoinDisApprove({ state, dispatch }, data) {
      console.log(data);
      instance
        .delete(`club/member_delete/${state.clubData.id}/${data.member}/`)
        .then(() => {
          dispatch('clubMangeList', { type: '' });
        })
        .catch((err) => console.log(err.response));
    },

    //클럽 탈퇴
    clubLeave({ state, commit }, data) {
      instance
        .post(`club/club_member_delete/${state.clubData.id}/`, data)
        .then(() => {
          commit("SET_IS_MEMBER", false);
        });
    },

    //클럽멤버인지
    isClubMember({ state, commit }, data) {
      instance
        .get(`club/club_detail/${data.id}/`)
        .then((result) => {
          console.log(data.user + " 여기유저");
          commit("SET_CLUB_DETAIL", result.data);
          instance
          .post(`club/member_check/${state.clubData.id}/`, { type: "승인" })
          .then((res) => {
            commit("SET_MANAGE_MEMBER_LIST", res.data);
            var b = false;
            for (var i = 0; i < res.data.length; i++) {
              if (res.data[i].user === data.user) {
                b = true;
                commit("SET_IS_MEMBER", true);
                break;
              }
            }
            if(!b){
              commit("SET_IS_MEMBER", false);
            }
            instance
            .post(`club/member_check/${state.clubData.id}/`, { type: "" })
            .then((res1) => {
              for (var j = 0; j < res1.data.length; j++) {
                if (res1.data[j].user === data.user) {
                  commit("SET_IS_WAITING", true);
                  return;
                }
              }
              commit("SET_IS_WAITING", false);
              console.log("여기2222 " + data.id)
                  return;
                });
            })
            .catch((err) => console.log(err.response));
        })
    },

    //클럽 게시판 관리 조회
    clubManageArticle({ state }) {
      state.clubManageArticleList = [];
      instance.get(`club/club_article_list/${state.clubData.id}/news/`).then((res) => {
        if (res.data.length > 0) {
          for (var i = 0; i < res.data.length; i++) {
            if (res.data[i] == '') {
              break;
            }
            state.clubManageArticleList.push(res.data[i]);
          }
        }
        instance.get(`club/club_article_list/${state.clubData.id}/youtube/`).then((res1) => {
          for (var i = 0; i < res1.data.length; i++) {
            if (res1.data[i] == '') {
              break;
            }
            state.clubManageArticleList.push(res1.data[i]);
          }
          instance.get(`club/club_article_list/${state.clubData.id}/etc/`).then((res2) => {
            for (var i = 0; i < res2.data.length; i++) {
              if (res2.data[i] == '') {
                break;
              }
              state.clubManageArticleList.push(res2.data[i]);
            }
          });
        });
      });
    },

    //클럽추방
    clubMemberRemove({ state, dispatch }, data) {
      instance.post(`club/club_member_delete/${state.clubData.id}/`, data).then(() => {
        dispatch('clubMangeList', { type: '승인' });
      });
    },
  },
};

export default clubStore;
