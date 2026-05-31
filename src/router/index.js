import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/admin',
    name: 'admin',
    component: () => import('@/views/AdminView.vue')
  },
  // We can add other routes if we want to have separate pages, but for now, we'll just have home.
  // However, to support hash scrolling, we can use the hash mode or just rely on the HomeView to handle scrolling.
  // We'll create the router with history mode and let the HomeView handle the scrolling via anchor links.
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
