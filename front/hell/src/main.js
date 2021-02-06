import Vue from 'vue';
import './plugins/axios';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import store from './store';
import router from './router';

Vue.config.productionTip = false;
window.Kakao.init('ebbcba463d0c5113870c2df8674ac8c7');
// Vue.$cookies.config("1d");

new Vue({
  vuetify,
  store,
  router, 
  // beforeCreate() {
  //   console.log('gdgd')
  //   this.$store.dispatch("userData")
  // },
  render: (h) => h(App),
}).$mount('#app');
