import { createRouter, createWebHashHistory } from "vue-router";
import app from "../pages/app.vue";
import notFound from "../pages/404.vue";
import home from "../pages/home.vue";
import room from "../pages/room.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: home,
  },
  {
    path: "/app",
    name: "app",
    component: app,
  },
  {
    path: "/room",
    name: "room",
    component: room,
  },
  {
    path: "/:catchAll(.*)",
    name: "notFound",
    component: notFound,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
