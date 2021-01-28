import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Issue from '../views/Issue/IssuePage.vue'
import Opinion from '../views/Opinion/OpinionPage.vue'
import Suggest from '../views/Suggest/SuggestPage.vue'
import Join from '../views/Join.vue'

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
  {
    path: '/join',
    name: 'Join',
    component: Join
  },
 
]

const router = new VueRouter({
  routes
})

export default router
