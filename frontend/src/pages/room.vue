<template>
  <div class="flex flex-col w-full h-full justify-center items-center">
    <div class="flex w-full h-full">
      <div class="p-3 w-72 h-full">
        <a href="http://localhost:3000/#/app"><icon /></a>

        <div class="flex w-full py-3 justify-between">
          <h2 class="text-2xl">{{ username }}</h2>
          <h2 class="flex text-lg py-1">
            <button @click="logout()">Выйти</button>
          </h2>
        </div>
        <h3>{{ msg }}</h3>
      </div>
      <div class="flex flex-col flex-auto gap-5 justify-center items-center">
        <div class="w-80 h-40 flex justify-between">
          <div class="flex flex-col w-full h-full justify-center items-center">
            <div
              v-if="loading"
              class="flex flex-col justify-center items-center"
            >
              <img src="../../public/loading.svg" />
              <h2>Loading</h2>
            </div>
            <div v-else>OK</div>
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
      token: "",
      loading: true,
      username: "",
      messages: [],
      dialog: [],
    };
  },
  components: {
    Icon,
    Btn,
    Input,
  },
  methods: {
    logout() {
      document.cookie = 'token=""';
      document.cookie = 'username=""';
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
    async createConnection() {
      var conn = new WebSocket(
        `ws://localhost:8000/user/poll?token=${this.token}`
      );
      conn.onmessage = (e) => {
        console.log(e.data);
      };
      conn.onopen = () => {
        conn.send("hello world");
        this.loading = false;
      };
    },
  },
  mounted() {
    this.token = this.getCookie("token");
    this.username = this.getCookie("username");
    this.createConnection();
  },
};
</script>

<style lang="scss" scoped></style>
