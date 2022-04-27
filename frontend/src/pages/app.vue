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
          <img class="w-20 max-h-16" src="/twopersons.svg" alt="" />
          <h2>Общаться вдвоём</h2>
        </div>
        <div
          @click="enter_in_room(4)"
          class="flex flex-col justify-center items-center cursor-pointer transition ease-in-out duration-200 hover:scale-125"
        >
          <img class="w-40 max-h-16" src="/three_persons.svg" alt="" />
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
      await fetch(`http://localhost:8000/user/remove?token=${this.token}`);
      console.log(`Token ${this.token} has been deleted from the server`);
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
    async create_empty_room(limit) {
      const req = await fetch(
        `http://localhost:8000/room/new?user_token=${this.token}&name=asd123&users_limit=${limit}`
      );
      const ans = await req.json();
      document.cookie = `room=${ans["response"]["token"]}`;
    },
    async enter_in_room(limit) {
      const req = await fetch("http://localhost:8000/room/getall");
      const ans = await req.json();
      const available_rooms = ans["response"].filter(
        (x) => x["users_limit"] == limit && !x["is_full"]
      );
      console.log(available_rooms);
      console.log(ans["response"]);
      if (available_rooms.length === 0) {
        // Если нет доступных комнат - создаем новую.
        await this.create_empty_room(limit);
      } else {
        const index = Math.floor(Math.random() * available_rooms.length);
        document.cookie = `room=${available_rooms[index]["token"]}`;
        // пробуем войти в комнату ...
        const req = await fetch(
          `http://localhost:8000/user/room.enter?token=${this.token}&room_token=${available_rooms[index]["token"]}`
        );
        const res = await req.json();
        // если комната достигла лимита - создаем новую.
        if ("detail" in res && res["detail"]["code"] == 6) {
          await this.this.create_empty_room(limit);
        }
      }
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

<style />
