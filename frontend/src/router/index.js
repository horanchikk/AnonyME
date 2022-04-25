import { createRouter, createWebHashHistory } from "vue-router";
import first from "../pages/first.vue";
import second from "../pages/second.vue";
import notFound from "../pages/404.vue";
import home from "../pages/home.vue";

const routes = [
  {
    path: "/home",
    name: "home",
    component: home,
  },
  {
    path: "/first",
    name: "first",
    component: first,
  },
  {
    path: "/second",
    name: "second",
    component: second,
  },
  {
    path: "/",
    name: "notFound",
    component: notFound,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
