import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Issue from '../views/Issue/IssuePage.vue'
import Opinion from '../views/Opinion/OpinionPage.vue'
import OpinionWrite from '../views/Opinion/OpinionWrite.vue'
import Club from '../views/Club/ClubPage.vue'
import OpinionDetail from '../views/Opinion/OpinionDetail.vue'

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
    path: '/club',
    name: 'Club',
    component: Club
  },
  {
    path: '/opinionWrite',
    name: 'OpinionWrite',
    component: OpinionWrite
  },
  {
    path: '/opinionDetail',
    name: 'OpinionDetail',
    component: OpinionDetail
  },
]

const router = new VueRouter({
  routes
})

export default router
