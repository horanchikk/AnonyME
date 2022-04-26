<template>
  <div class="w-full h-full flex flex-col">
    <div class="flex flex-col p-3 w-72 h-auto">
      <a href="http://localhost:3000/#/app"><icon /></a>
      <div class="flex w-full py-3 justify-between">
        <h2 class="text-3xl">{{ username }}</h2>
        <button class="flex text-lg p-1" @click="logout()">Выйти</button>
      </div>
    </div>

    <div class="flex flex-col p-3 w-72 h-32" v-if="loading">
      <div class="flex flex-col w-screen h-screen justify-center items-center">
        <div class="flex flex-col w-full h-full">
          <div class="p-3 w-72 h-32">
            <a href="http://localhost:3000/#/app"><icon /></a>
            <div class="flex w-full py-3 justify-between">
              <h2 class="text-2xl">{{ username }}</h2>
              <button class="flex text-2xl py-1" @click="logout()">
                Выйти
              </button>
            </div>
            <h3>{{ msg }}</h3>
          </div>
          <div
            class="flex flex-col justify-center items-center flex-auto gap-5"
          >
            <div class="w-80 h-40 flex justify-between">
              <div
                class="flex flex-col w-full h-full justify-center items-center"
              >
                <div class="flex flex-col justify-center items-center">
                  <img src="../../public/loading.svg" />
                  <h2>Loading</h2>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="flex flex-col items-center justify-center">
      <div class="w-4/6">
        <div class="overflow-y-scroll scroller">
          <div v-for="msg in dialog" :key="msg">
            <div v-if="msg.author === this.username" class="flex justify-end">
              <div
                style="background: #33373d"
                class="m-5 p-3 px-5 rounded-3xl w-1/2"
              >
                <p class="mx-5 font-semibold">{{ msg.author }}</p>
                <p class="my-1" v-html="msg.text"></p>
                <div class="flex justify-end mx-3 msgtime">{{ msg.time }}</div>
              </div>
            </div>

            <div v-else>
              <div
                style="background: #33373d"
                class="m-5 p-3 px-5 rounded-3xl w-1/2"
              >
                <p class="mx-5 font-semibold">{{ msg.author }}</p>
                <p class="my-1" v-html="msg.text"></p>
                <div class="flex justify-end mx-3 msgtime">{{ msg.time }}</div>
              </div>
            </div>
          </div>
        </div>
        <div>
          <div class="flex h-14">
            <Input @chatmessage="setMessage" class="w-full" :type="'chat'" />
            <img
              class="h-full px-4 cursor-pointer hover"
              src="../../public/send.svg"
              alt="send"
            />
          </div>

          <!-- icons   -->
          <div class="flex w-full justify-center">
            <div class="flex w-4/6 p-5 justify-between">
              <div
                class="flex flex-col cursor-pointer transition ease-in-out duration-200 hover:scale-125"
              >
                <img
                  @click="console.log('asd')"
                  class="h-10 cursor-pointer"
                  src="../../public/search.svg"
                  alt=""
                />
                Найти другого
              </div>
              <div
                class="flex flex-col cursor-pointer transition ease-in-out duration-200 hover:scale-125"
              >
                <img
                  @click="console.log('asd')"
                  class="h-10"
                  src="../../public/quit.svg"
                  alt=""
                />
                Прекратить общение
              </div>
              <div
                class="flex flex-col cursor-pointer transition ease-in-out duration-200 hover:scale-125"
              >
                <img
                  @click="console.log('asd')"
                  class="h-10"
                  src="../../public/complaint.svg"
                  alt=""
                />
                Жалоба
              </div>
            </div>
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
import { marked } from "marked";

export default {
  data() {
    return {
      token: "",
      loading: false,
      limit: "",
      username: "",
      roomtoken: "",
      dialog: [],
      chatmessage: "",
    };
  },
  components: {
    Icon,
    Btn,
    Input,
  },
  methods: {
    async logout() {
      // Clear all cookies and delete user
      await fetch(`http://localhost:8000/user/remove?token=${this.token}`);
      document.cookie = 'token=""';
      document.cookie = 'username=""';
      document.cookie = 'limit=""';
      document.cookie = 'room=""';
      location.href = "http://localhost:3000";
    },
    updateToken() {
      this.token = document.cookie;
    },
    setMessage(value) {
      this.chatmessage = value;
    },
    sendMessage() {
      this.chatmessage;
      // здесьнадо будет this.connection.send(текст с инпута);
    },
    getCookie(name) {
      // какой-то костыль, js пофиксите твари :cry:
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
      this.connection.onopen = () => {
        console.log("connected");
      };
      this.connection.onmessage = async (e) => {
        this.connection.onopen = () => {
          console.log("connected");
        };
        let msg = JSON.parse(e.data).response;
        if (msg.author !== undefined && msg.text !== undefined) {
          console.log(msg);
          msg.text = marked(msg.text);
          msg.time = new Date(parseInt(msg.time).toLocaleTimeString());
          this.dialog.push(msg);
        }
      };
    },
    async getDialog() {
      const req = await fetch(
        `http://localhost:8000/room/history.get?token=${this.roomtoken}`
      );
      const res = await req.json();
      this.dialog = res["response"]["history"];
      this.dialog.forEach((msg) => {
        msg.text = marked(msg.text);
        msg.time = new Date(parseInt(msg.time).toLocaleTimeString());
      });
    },
  },
  mounted() {
    this.token = this.getCookie("token");
    this.username = this.getCookie("username");
    this.limit = this.getCookie("limit");
    this.roomtoken = this.getCookie("room");
    this.connection = new WebSocket(
      `ws://localhost:8000/user/poll?token=${this.token}`
    );
    this.getDialog();
    this.createConnection();
  },
};
</script>

<style>
.scroller {
  height: 600px;
  -ms-overflow-style: none;
  scrollbar-width: none;
  overflow-y: scroll;
}

.scroller::-webkit-scrollbar {
  display: none;
}

.msgtime {
  transform: translate(10px, 5px);
  color: rgba(255, 255, 255, 0.5);
}
</style>
