<template>
  <div class="flex flex-col w-full h-full justify-center items-center">
    <div v-if="loading" class="flex flex-col justify-center items-center">
      <img src="../../public/loading.svg" />
      <h2>Loading</h2>
    </div>
    <div v-else class="flex w-full h-full">
      <div class="p-3 w-72 h-full">
        <icon />
        <div class="flex w-full py-3 justify-between">
          <h2 class="text-2xl">Test User</h2>
          <h2 class="flex text-lg py-1">
            <button @click="logout()">Выйти</button>
          </h2>
        </div>
        <h3>{{ msg }}</h3>
      </div>
      <div class="flex flex-col flex-auto gap-5 justify-center items-center">
        <h1 class="text-2xl">Начните общение прямо сейчас</h1>
        <div class="w-80 h-40 flex justify-between">
          <div class="flex flex-col justify-center items-center cursor-pointer">
            <img class="w-20 h-20" src="../../public/twogays.svg" alt="" />
            <h2>Общаться вдвоём</h2>
          </div>
          <div class="flex flex-col justify-center items-center cursor-pointer">
            <img class="w-40 h-20" src="../../public/threegays.svg" alt="" />
            <h2>Общаться в группе</h2>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Icon from "../components/icon.vue";
import Btn from "../components/btn.vue";
import Input from "../components/input.vue";

export default {
  data() {
    return {
      msg: "",
      token: "",
      loading: true,
    };
  },
  components: {
    Icon,
    Btn,
    Input,
  },
  methods: {
    logout() {
      location.href = "http://localhost:3000";
    },
    updateToken() {
      this.token = document.cookie;
    },
    getCookie(name) {
      let matches = document.cookie.match(
        new RegExp(
          "(?:^|; )" +
            name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, "\\$1") +
            "=([^;]*)"
        )
      );
      return matches ? decodeURIComponent(matches[1]) : undefined;
    },
    userGet() {
      // http://localhost:8000/room/history.get?token=
      // http://localhost:8000/room/history.get?token=
      // const req = await fetch(`http://localhost:8000/user/get?token=${this.token}`);
      // const res = req.json()
      // console.log(res)
    },
    createConnection() {
      this.loading = true;
      var conn = new WebSocket(
        `ws://localhost:8000/user/poll?token=${this.token}`
      );
      conn.onmessage = function (e) {
        console.log(e.data);
      };
      conn.onopen = () => {
        conn.send("idi nahoy");
        this.loading = false;
      };
    },
  },
  mounted() {
    this.token = this.getCookie("token");
    this.createConnection();
    // this.getHistory();
  },
};
</script>

<style lang="scss" scoped></style>
