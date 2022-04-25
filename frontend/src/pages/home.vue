<template>
  <div
    class="w-full h-full flex flex-col gap-1 justify-center items-center text-4xl font-semibold text-white helkow"
  >
    <icon class="my-5" />
    <div class="flex flex-col flex-auto items-center justify-center">
      <h1 class="font-medium text-lg text-center">
        Приветствуем вас в
        <a class="font-bold" style="color: #ef313d">AnonyME</a> <br />
        Введите свой ник, чтобы продолжить работу
      </h1>
      <Input
        v-model="this.message"
        placeholder="Введите свой ник"
        :type="'login'"
        @username="setUsername"
      />
      <Btn @click="createUser()" :text="'Продолжить'" :type="'lg'" />
      <h3 class="my-3 font-bold text-red-500 text-xs">{{ error }}</h3>
    </div>
    <div class="flex w-full h-20 text-xs items-end text-slate-500">
      <a href="https://github.com/horanchikk/AnonyME"
        >© AVOCAT 2022. All rights reserved</a
      >
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
      username: "",
      error: "",
    };
  },
  components: {
    Icon,
    Btn,
    Input,
  },
  methods: {
    setUsername(name) {
      this.username = name;
    },
    async createUser() {
      const req = await fetch(
        `http://localhost:8000/user/new?name=${this.username}`
      );
      if (req.ok) {
        const res = await req.json();
        console.log(`Token is: ${res["response"]["token"]}`);
        document.cookie = `token=${res["response"]["token"]}`;
        location.href = "http://localhost:3000/#/app";
      } else {
        this.error = "User is created. Try change username";
      }
    },
  },
};
</script>

<style></style>
