<template>
  <div
    class="w-full h-full flex flex-col gap-1 justify-center items-center text-4xl font-semibold text-white helkow"
  >
    <icon class="my-5 icon-animate" />
    <div
      class="flex flex-col flex-auto items-center justify-center body-animate"
    >
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

    <div class="flex w-full h-20 text-xs items-end text-slate-500">
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
      const req = await fetch(
        `http://localhost:8000/user/new?name=${this.username}`
      );
      if (req.ok) {
        const res = await req.json();
        console.log(`Token is: ${res["response"]["token"]}`);
        document.cookie = `token=${res["response"]["token"]}`;
        document.cookie = `username=${this.username}`;
        this.$router.push("/app");
      } else {
        this.error = "User is created. Try change username";
      }
    },
  },
};
</script>

<style>
@keyframes fadein-icon {
  0% {
    transform: translateY(-50px);
    opacity: 0%;
  }
  100% {
    transform: translateY(0px);
    opacity: 100%;
  }
}

.icon-animate {
  animation: fadein-icon 1000ms ease-in-out;
}

@keyframes fadein-body {
  0% {
    transform: translateY(50px);
    opacity: 0%;
  }
  100% {
    transform: translateY(0px);
    opacity: 100%;
  }
}

.body-animate {
  animation: fadein-body 1000ms ease-in-out;
}
</style>
