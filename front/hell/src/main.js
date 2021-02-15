import Vue from 'vue';
import './plugins/axios';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import store from './store';
import router from './router';
import VueSimpleAlert from 'vue-simple-alert';
import Toasted from 'vue-toasted';

Vue.config.productionTip = false;
// window.Kakao.init('ebbcba463d0c5113870c2df8674ac8c7');
Vue.use(VueSimpleAlert);
Vue.use(Toasted);

new Vue({
  vuetify,
  store,
  router,

  render: (h) => h(App),
}).$mount('#app');
