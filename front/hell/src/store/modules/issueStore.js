import { createInstance } from "../../api/index.js";

const instance = createInstance();

const issueStore = {
  namespaced: true,
  state: {
    // 카테고리별 이슈
    issueEntertainment: null,
    issueITScience: null,
    issueWorld: null,
    issueEconomy: null,
    issueSports: null,
    issuePolitics: null,
    issueSociety: null,

    issueDetailYoutubeDialog: false,
    issueDetailVideoUrl: '',

  },
  getters: {},
  mutations: {
    SET_ISSUE_DETAIL_YOUTUBE_DIALOG(state, dialog){
      state.issueDetailYoutubeDialog= dialog;
    },
    SET_ISSUE_DETAIL_VIDEO_URL(state, url){
      state.issueDetailVideoUrl= url;
    },
    SET_ISSUE_ENTERTAINMENT(state, issue) {
      state.issueEntertainment = issue;
    },
    SET_ISSUE_ITSCIENCE(state, issue) {
      state.issueITScience = issue;
    },
    SET_ISSUE_WORLD(state, issue) {
      state.issueWorld = issue;
    },
    SET_ISSUE_ECONOMY(state, issue) {
      state.issueEconomy = issue;
    },
    SET_ISSUE_SPORTS(state, issue) {
      state.issueSports = issue;
    },
    SET_ISSUE_POLITICS(state, issue) {
      state.issuePolitics = issue;
    },
    SET_ISSUE_LIVING(state, issue) {
      state.issueSociety = issue;
    },


  },
  actions: {
    issueCategory({ commit }, data) {
      instance
        .post(`/issue/`, data)
        .then((res) => {
          switch (res.data[0].category) {
            case "ENTERTAINMENT":
              commit("SET_ISSUE_ENTERTAINMENT", res.data);
              break;
            case "IT_SCIENCE":
              commit("SET_ISSUE_ITSCIENCE", res.data);
              break;
            case "WORLD":
              commit("SET_ISSUE_WORLD", res.data);
              break;
            case "ECONOMY":
              commit("SET_ISSUE_ECONOMY", res.data);
              break;
            case "SPORTS":
              commit("SET_ISSUE_SPORTS", res.data);
              break;
            case "POLITICS":
              commit("SET_ISSUE_POLITICS", res.data);
              break;
            case "SOCIETY/LIVING":
              commit("SET_ISSUE_LIVING", res.data);
              break;
          }
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
  },
};

export default issueStore;
