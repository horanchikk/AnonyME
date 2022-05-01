<template>
  <div
    class="w-full h-full flex flex-col gap-1 overflow-hidden justify-center items-center text-4xl font-semibold text-white helkow"
  >
    <icon class="my-5 animate__animated animate__fadeInDown" />
    <div
      class="flex flex-col flex-auto items-center justify-center animate__animated animate__fadeInUp"
    >
      <h1 class="font-medium text-lg text-center text-bblack dark:text-white">
        Приветствуем вас в
        <a class="font-bold" style="color: #ef313d">AnonyME</a> <br />
        Введите свой ник, чтобы продолжить работу
      </h1>
      <Input
        v-model="this.message"
        placeholder="Введите свой ник"
        :type="'login'"
        @username="setUsername"
        v-on:keyup.enter="createUser()"
      />
      <Btn
        id="btnnext"
        @click="createUser()"
        :text="'Продолжить'"
        :type="'lg'"
      />
      <h3
        v-if="error != ''"
        class="my-3 font-bold text-red-500 text-base animate-pulse"
        @animationend="error = ''"
      >
        {{ error }}
      </h3>
    </div>

    <div
      class="flex w-full h-20 text-xs items-end text-slate-700 dark:text-slate-500"
    >
      <div class="flex flex-col">
        <a href="https://github.com/horanchikk/AnonyME"
          >© AVOCAT 2022. All rights reserved
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import Icon from "../components/icon.vue";
import Btn from "../components/btn.vue";
import Input from "../components/input.vue";
import API from "../mixins/api";
import cookies from "../mixins/cookies";

export default {
  data() {
    return {
      username: "",
      error: "",
      errorAnimation: false,
    };
  },
  components: {
    Icon,
    Btn,
    Input,
  },
  mixins: [API, cookies],
  methods: {
    setUsername(name) {
      this.username = name;
    },
    async createUser() {
      this.error = "";
      if (this.username == "") {
        this.error = "Username is empty. Try again.";
        return;
      }
      const res = await API.newUser(this.username);
      if ("response" in res) {
        console.log(`Token is: ${res["response"]["token"]}`);
        document.cookie = `token=${res["response"]["token"]}`;
        document.cookie = `username=${this.username}`;
        this.$router.push("/app");
      } else {
        this.error = res["detail"]["message"];
      }
    },
  },
};
</script>

<style />
