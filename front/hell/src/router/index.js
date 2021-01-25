import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Issue from '../views/Issue/IssuePage.vue'
import Opinion from '../views/Opinion/OpinionPage.vue'
import Suggest from '../views/Suggest/SuggestPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
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
<<<<<<< HEAD
 
=======
>>>>>>> 385e493305b4af3bb65f6a1129b9fb2fa9456e45
]

const router = new VueRouter({
  routes
})

export default router
