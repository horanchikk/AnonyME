<template>
  <div
    class="w-full h-full flex flex-col gap-1 justify-center items-center text-white helkow"
  >
    <icon class="my-5" />
    <div class="flex flex-col flex-auto items-center justify-center">
      <h1 class="font-medium text-lg text-center">
        {{ username }}, начните общение прямо сейчас!
      </h1>
      <div class="flex gap-7 my-7">
        <div
          @click="enter_in_room(2)"
          class="flex flex-col justify-center items-center cursor-pointer transition ease-in-out duration-200 hover:scale-125"
        >
          <img class="w-20 max-h-16" src="../../public/twopersons.svg" alt="" />
          <h2>Общаться вдвоём</h2>
        </div>
        <div
          @click="enter_in_room(4)"
          class="flex flex-col justify-center items-center cursor-pointer transition ease-in-out duration-200 hover:scale-125"
        >
          <img
            class="w-40 max-h-16"
            src="../../public/three_persons.svg"
            alt=""
          />
          <h2>Общаться в группе</h2>
        </div>
      </div>
      <h3 class="my-3 font-bold text-red-500 text-xs">{{ error }}</h3>
    </div>
    <div
      class="flex w-full h-20 text-xs justify-between items-end text-slate-500"
    >
      <a href="https://github.com/horanchikk/AnonyME"
        >© AVOCAT 2022. All rights reserved</a
      >
      <button
        class="p-10 text-2xl text-white transition ease-in-out duration-200 hover:text-slate-400"
        @click="logout()"
      >
        Выйти
      </button>
    </div>
  </div>

  <!-- <div class="flex justify-center items-center">
    <div class="flex w-screen h-screen">
      <div class="p-3 w-72">
        <icon />
        <div class="flex w-full py-3 justify-between">
          <h2 class="text-2xl">{{ username }}</h2>
          <h2 class="flex text-lg py-1">
            <button @click="logout()">Выйти</button>
          </h2>
        </div>
        <h3>{{ msg }}</h3>
      </div>
      <div class="flex flex-col flex-auto gap-5 justify-center items-center">
        <h1 class="text-2xl">{{ username }}, начните общение прямо сейчас!</h1>
        <div class="w-80 h-40 flex justify-between">
          <div
            @click="enter_in_room()"
            class="flex flex-col justify-center items-center cursor-pointer"
          >
            <img class="w-20 h-20" src="../../public/twogays.svg" alt="" />
            <h2>Общаться вдвоём</h2>
          </div>
          <div
            @click="enter_in_room()"
            class="flex flex-col justify-center items-center cursor-pointer"
          >
            <img class="w-40 h-20" src="../../public/threegays.svg" alt="" />
            <h2>Общаться в группе</h2>
          </div>
        </div>
      </div>
    </div>
  </div> -->
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
      username: "",
    };
  },
  components: {
    Icon,
    Btn,
    Input,
  },
  methods: {
    async logout() {
      // 500 status code + CORS ERROR => FastAPI error
      const req = await fetch(
        `http://localhost:8000/user/remove?token=${this.token}`
      );
      document.cookie = 'token=""';
      document.cookie = 'username=""';
      document.cookie = 'limit=""';
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
    async enter_in_room(limit) {
      const req = await fetch(
        `http://localhost:8000/room/new?users_limit=${limit}&name=123123&user_token=${this.token}`
      );
      const ans = await req.json();
      document.cookie = `room=${ans["response"]["token"]}`;
      document.cookie = `limit=${limit}`;
      location.href = "http://localhost:3000/#/room";
    },
  },
  mounted() {
    this.token = this.getCookie("token");
    this.username = this.getCookie("username");
  },
};
</script>

<style lang="scss" scoped></style>
