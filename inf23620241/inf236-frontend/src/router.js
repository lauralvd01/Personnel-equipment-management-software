import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from './components/HelloWorld.vue'
import vistaJefeMotores from './components/vistaJefeMotores.vue'
import vistaMecanico from './components/vistaMecanicos.vue'
import VistaConductores from './components/vistaConductores.vue'


const routes = [
  { path: '/', component: HomeView},
  { path: '/vistaJefeMotores/', component: vistaJefeMotores},
  { path: '/vistaMecanico/:id', component: vistaMecanico}
  { path: '/vistaConductores/:id', component: VistaConductores}
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router