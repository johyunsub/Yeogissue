import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
<<<<<<< HEAD
import Issue from '../views/Issue/IssuePage.vue'
import Opinion from '../views/Opinion/OpinionPage.vue'
import Suggest from '../views/Suggest/SuggestPage.vue'
=======
import Login from '../views/Login.vue'
>>>>>>> a78e6030ef30d1e78791c04fd4fbc81c75a5c125

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
<<<<<<< HEAD
    path: '/issue',
    name: 'Issue',
    component: Issue
  },
  {
    path: '/opinion',
    name: 'Opinion',
    component: Opinion
  },
  {
    path: '/suggest',
    name: 'Suggest',
    component: Suggest
  },
 
=======
    path: '/login',
    name: 'Login',
    component: Login
  },
>>>>>>> a78e6030ef30d1e78791c04fd4fbc81c75a5c125
]

const router = new VueRouter({
  routes
})

export default router
