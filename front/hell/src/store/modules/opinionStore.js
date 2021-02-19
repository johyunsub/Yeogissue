import { createInstance } from "../../api/index.js";
import Swal from "sweetalert2";

const instance = createInstance();

const opinionStore = {
  namespaced: true,
  state: {
    opinions: null,

    //페이징 하게 10개씩 저장
    opinionPaging: {},
    pagingCnt: 0,

    opinionCategory: null,

    // 디테일 변수
    opinionData: {
      agree_count: 0,
      category: "",
      club_pk: 0,
      comment_count: 0,
      comment_set: [],
      comment_type: false,
      content: "",
      created_at: "",
      disagree_count: 0,
      hashtags: [],
      id: 0,
      like_users: [],
      like_users_count: 0,
      read_count: 117,
      scrap_users: [],
      scrap_users_count: 0,
      title: "",
      updated_at: "",
      user: 0,
      username: "",
    },

    //댓글
    opinionComment: null,
    opinionCommentPaging: {},
    opinionCommentPagingCnt: 0,
    opinionCommentSelect: 0,

    //해시태그
    top_hashtags: [],
    hashtags: [],
  },
  getters: {},
  mutations: {
    SET_TOP_HASHTAGS(state, hashtags) {
      state.top_hashtags = hashtags;
    },
    SET_HASHTAGS(state, hashtags) {
      state.hashtags = hashtags;
    },

    SET_OPINIONS(state, opinions) {
      state.opinions = opinions;
    },

    SET_OPINION_PAGING(state, start) {
      state.opinionPaging = {};
      state.pagingCnt = Math.floor(state.opinionCategory.length / 10);
      if (state.opinionCategory.length % 10 != 0) state.pagingCnt++;

      let index = 0;
      for (let i = start; i < start + 10; i++) {
        if (i == state.opinionCategory.length) break;
        state.opinionPaging[index++] = state.opinionCategory[i];
      }
    },

    SET_OPINION_CATEGORY(state, category) {
      state.opinionCategory = [];
      let index = 0;
      //전체 보기이면 그대로 저장
      if (category == "전체") {
        state.opinionCategory = state.opinions;
        return;
      }

      //카테고리 분류
      for (let i = 0; i < state.opinions.length; i++) {
        if (state.opinions[i].category == category) {
          state.opinionCategory[index++] = state.opinions[i];
        }
      }
    },

    SET_OPINION_DETAIL(state, opinion) {
      console.log("디테일 저장됩니다.");
      state.opinionData = opinion;
    },

    SET_OPINION_COMMENT(state, comment) {
      state.opinionComment = comment;
    },

    SET_OPINION_COMMENT_PAGING(state, start) {
      state.opinionCommentPaging = {};
      state.opinionCommentPagingCnt = Math.floor(state.opinionComment.length / 10);
      if (state.opinionComment.length % 10 != 0) state.opinionCommentPagingCnt++;

      let index = 0;
      for (let i = start; i < start + 10; i++) {
        if (i == state.opinionComment.length) break;
        state.opinionCommentPaging[index++] = state.opinionComment[i];
      }
    },

    SET_OPINION_COMMENT_SELECT(state, cur) {
      state.opinionCommentSelect = cur;
    },

    //의견 LIKED 상태로 변경 <<
    // SET_OPINION_LIKED(state, id) {
    //   state.opinionLike.push(id);
    // },
  },
  actions: {
    //조회
    opinionList({ commit }) {
      instance
        .get("/articles/article_list/")
        .then((res) => {
          commit("SET_OPINIONS", res.data);
          commit("SET_OPINION_CATEGORY", "전체");
          commit("SET_OPINION_PAGING", 0);
        })
        .catch((err) => console.log(err.response));
    },
    //클럽 조회
    opinionListClub({ commit }, id) {
      instance
        .get(`/articles/club/${id}/`)
        .then((res) => {
          commit("SET_OPINIONS", res.data);
          commit("SET_OPINION_CATEGORY", "전체");
          commit("SET_OPINION_PAGING", 0);
        })
        .catch((err) => console.log(err.response));
    },
    //해시태그 조회
    hashOpinionList({ commit }, data) {
      instance
        .post("/articles/search_bar/", data)
        .then((res) => {
          commit("SET_OPINIONS", res.data);
          commit("SET_OPINION_CATEGORY", "전체");
          commit("SET_OPINION_PAGING", 0);
        })
        .catch((err) => console.log(err.response));
    },
    // 해시태그 탑 10
    hash_top10({ commit }) {
      instance
        .get("/articles/top_hashtag/")
        .then((res) => {
          commit("SET_TOP_HASHTAGS", res.data);
        })
        .catch((err) => console.log(err.response));
    },
    //생성
    opinionCreate({ dispatch }, data) {
      instance
        .post("/articles/article_create/", data)
        .then(() => {
          dispatch("opinionList");
        })
        .catch((err) => console.log(err.response));
    },

    //수정
    opinionUpdate({ commit }, data) {
      instance
        .put(`/articles/${data.id}/`, data)
        .then(() => {
          commit("SET_OPINION_DETAIL", data);
        })
        .catch((err) => console.log(err.response));
    },

    //삭제
    opinionDelete({ commit }, id) {
      instance
        .delete(`/articles/${id}/`)
        .then(() => {
          commit("SET_OPINION_DETAIL", null);
        })
        .catch((err) => console.log(err.response));
    },

    // 카테고리별로 생성
    opinionCategorySelelct({ commit }, category) {
      commit("SET_OPINION_CATEGORY", category);
      commit("SET_OPINION_PAGING", 0);
    },

    // 디테일
    opinionDetail({ commit, state }, id) {
      instance
        .get(`/articles/${id}/`)
        .then((res) => {
          commit("SET_OPINION_DETAIL", res.data);
          commit("SET_OPINION_COMMENT", res.data.comment_set);
          commit("SET_OPINION_COMMENT_PAGING", state.opinionCommentSelect);
        })
        .catch((err) => console.log(err.response));
    },

    // 해시태그 추천
    getHashtag({ commit }, data) {
      instance
        .post("/articles/make_hashtag/", data)
        .then((res) => {
          console.log(res.data);
          commit("SET_HASHTAGS", res.data);
        })
        .catch((err) => console.log(err.response));
    },

    // 댓글 등록
    opinionCommentCreate({ dispatch, state }, data) {
      instance
        .post(`/articles/${state.opinionData.id}/comments/`, data)
        .then(() => {
          dispatch("opinionDetail", state.opinionData.id);
        })
        .catch((err) => {
          console.log("에러")
          console.log(err.response);
        });
    },

    // 댓글 수정
    opinionCommentUpdate({ dispatch, state }, updateData) {
      instance
        .put(`/articles/comments/${updateData.no}/`, updateData.data)
        .then(() => {
          dispatch("opinionDetail", state.opinionData.id);
        })
        .catch((err) => console.log(err.response));
    },

    // 댓글 삭제
    opinionCommentDelete({ dispatch, state }, commentid) {
      instance
        .delete(`/articles/comments/${commentid}/`)
        .then(() => {
          dispatch("opinionDetail", state.opinionData.id);
        })
        .catch((err) => console.log(err.response));
    },

    // 댓글 신고
    opinionBadComment({ dispatch, state }, commentid) {
      instance
        .put(`/articles/badcomments/${commentid}/`)
        .then(() => {
          dispatch("opinionDetail", state.opinionData.id);
        })
        .catch((err) => console.log(err.response));
    },

    // 댓글 감정
    opinionCommentEmotion({ dispatch }, data) {
      instance
        .post(`/articles/emotion_comment/`, data)
        .then((res) => {
          if (res.data.emotion == "분노" || res.data.emotion == "혐오") {
            Swal.fire({
              title: "화가 많아보이는 댓글입니다. 그대로 저장하시겠습니까?",

              showCancelButton: true,
              confirmButtonText: `Save`,
            }).then((result) => {
              /* Read more about isConfirmed, isDenied below */
              if (result.isConfirmed) {
                Swal.fire("Saved!", "", "success");
                dispatch("opinionCommentCreate", res.data);
              }
            });
          } else {
            console.log(res.data);
            dispatch("opinionCommentCreate", res.data);
          }
        })
        .catch((err) => console.log(err.response));
    },

    //북마크 버튼
    bookmarkUpdate({ state, dispatch }, user) {
      instance
        .post(`/articles/${state.opinionData.id}/scrap/`, { user: user })
        .then(() => {
          dispatch("opinionDetail", state.opinionData.id);
        })
        .catch((err) => console.log(err.response));
    },

    //좋아요 버튼
    thumbUp({ state, dispatch }, data) {
      instance
        .post(`/articles/${data.id}/like/`, { user: data.user })
        .then(() => {
          dispatch("opinionDetail", state.opinionData.id);
        })
        .catch((err) => console.log(err.response));
    },
  },
};

export default opinionStore;
