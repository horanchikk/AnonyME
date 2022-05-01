<template>
  <div class="w-full h-full flex flex-col">
    <div class="flex flex-col p-3 w-72 h-auto">
      <a href="http://localhost:3000/#/app"
        ><icon class="animate__animated animate__fadeInLeft"
      /></a>
      <div class="flex w-full py-3 justify-between">
        <h2
          class="text-3xl text-slate-700 dark:text-slate-100 animate__animated animate__fadeInLeft"
        >
          {{ username }}
        </h2>
        <button
          class="flex text-lg p-1 text-slate-700 dark:text-slate-100 animate__animated animate__fadeInLeft"
          @click="logout()"
        >
          Выйти
        </button>
      </div>
    </div>

    <div class="flex flex-col p-3 w-72 h-32" v-if="loading">
      <div
        class="flex flex-col w-screen h-screen justify-center items-center overflow-hidden"
      >
        <div class="flex flex-col w-full h-full">
          <div class="p-3 w-72 h-32">
            <a @click="exit_from_room()"><icon /></a>
            <div class="flex w-full py-3 justify-between">
              <h2 class="text-2xl">
                {{ username }}
              </h2>
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
                  <img src="/loading.svg" />
                  <h2>Loading</h2>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="flex flex-col items-center h-full">
      <div class="flex flex-auto justify-center items-end w-5/6 shadow-md">
        <div class="w-4/6">
          <div class="overflow-y-auto scroller" id="mainChat">
            <TransitionGroup
              id="transition"
              name="msg"
              tag="div"
              @transitionstart="scrollDown()"
            >
              <div v-for="msg in dialog" :key="msg">
                <!-- Обработка статусов (вход в чат и выход из чата) -->
                <div
                  v-if="[2,3,4].filter(x => msg.action_code == x).length > 0"
                  class="flex justify-center font-semibold text-xl text-slate-700 dark:text-slate-200"
                >
                  {{ msg.author }} {{ msg.action }}
                </div>
                <div
                  v-else-if="msg.author === this.username"
                  class="flex justify-end"
                >
                  <div :class="msg.class">
                    <p class="mx-5 font-semibold">
                      {{ msg.author }}
                    </p>
                    <p
                      v-if="msg.sticker.length == 0"
                      v-html="msg.text"
                      class="font-normal"
                    ></p>
                    <img
                      v-else
                      class="h-48"
                      :src="'/stickers/' + msg.sticker[0]['file']"
                    />
                    <div
                      class="flex mx-4 items-end justify-end text-slate-200 msgtime"
                    >
                      {{ msg.time }}
                    </div>
                  </div>
                </div>

                <!-- а вы гей? мы да. че пиздишь ты наурал. нет сам ты наурал. ну на урал так ну урал мне пох. -->

                <div v-else>
                  <div :class="msg.class">
                    <p class="mx-5 font-semibold">
                      {{ msg.author }}
                    </p>
                    <p class="p-3" v-html="msg.text"></p>
                    <p
                      v-if="msg.sticker.length == 0"
                      v-html="msg.text"
                      class="font-normal"
                    ></p>
                    <img
                      v-else
                      class="h-48"
                      :src="'/stickers/' + msg.sticker[0]['file']"
                    />
                    <div class="flex mx-4 items-end justify-end msgtime">
                      {{ msg.time }}
                    </div>
                  </div>
                </div>
              </div>
            </TransitionGroup>
          </div>
          <div>
            <stickerPanel @choise="sendSticker" />
            <div class="flex h-14">
              <Input
                @chatmessage="setMessage"
                v-on:keyup.enter="sendMessage(this.chatmessage, 0)"
                id="chatInput"
                class="w-full"
                :type="'chat'"
              />
              <img
                @click="sendMessage(this.chatmessage, 0)"
                class="h-full ml-4 px-4 cursor-pointer transition ease-in-out duration-200 hover:scale-125"
                src="/send.svg"
                alt="send"
              />
            </div>

            <!-- bottom icons -->
            <div class="flex w-full justify-center">
              <div class="flex w-4/6 p-5 justify-between">
                <div
                  class="flex flex-col overflow-hidden cursor-pointer transition ease-in-out duration-200 hover:scale-125 animate__animated animate__fadeInUp"
                >
                  <img
                    @click="change_room()"
                    class="h-10 cursor-pointer"
                    src="/search.svg"
                    alt="search"
                  />
                  <h1 class="text-slate-700 dark:text-slate-500">
                    Найти другого
                  </h1>
                </div>
                <div
                  class="flex flex-col cursor-pointer transition ease-in-out duration-200 hover:scale-125 animate__animated animate__fadeInUp"
                >
                  <img
                    @click="exit_from_room()"
                    class="h-10"
                    src="/quit.svg"
                    alt="quit"
                  />
                  <h1 class="text-slate-700 dark:text-slate-500">
                    Прекратить общение
                  </h1>
                </div>
                <div
                  class="flex flex-col cursor-pointer transition ease-in-out duration-200 hover:scale-125 animate__animated animate__fadeInUp"
                >
                  <img
                    @click="console.log('asd')"
                    class="h-10"
                    src="/complaint.svg"
                    alt="complaint"
                  />
                  <h1 class="text-slate-700 dark:text-slate-500">Жалоба</h1>
                </div>
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
import emoji_list from "../../public/emojilist.json";
import stickers_list from "../../public/stickers/stickers.json";
import stickerPanel from "../components/stickerPanel.vue";
import showNewMessage from "../components/showNewMessage.vue";

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
      emoji_list: emoji_list,
    };
  },
  components: {
    Icon,
    Btn,
    Input,
    stickerPanel,
    showNewMessage,
  },
  methods: {
    /**
     * Очистка всех куки и удаление пользователя.
     */

    async logout() {
      await fetch(`http://109.248.133.17:8000/users/remove?token=${this.token}`);
      document.cookie = 'token=""';
      document.cookie = 'username=""';
      document.cookie = 'room=""';
      location.href = "http://localhost:3000";
    },
    async exit_from_room() {
      await fetch(`http://109.248.133.17:8000/users/room.leave?token=${this.token}`);
      document.cookie = 'room=""';
      location.href = "http://localhost:3000/#/app";
    },
    updateToken() {
      this.token = document.cookie;
    },
    setMessage(value) {
      this.chatmessage = value;
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
    /**
     * Отправка сообщения (через вебсокеты).
     */
    async sendMessage(text, sticker) {
      if (text != "" || sticker != 0) {
        this.connection.send(
          JSON.stringify({
            text: text,
            sticker_id: sticker,
          })
        );
        document.getElementById("chatInput").value = "";
        this.chatmessage = "";
      }
    },
    /**
     * Обработка сообщений
     */
    processMessage(msg) {
      msg.text = this.emojify(marked(msg.text));
      msg.sticker = stickers_list.filter((x) => x["id"] == msg.sticker_id);
      // msg.background =
      //   msg.sticker.length == 0
      //     ? msg.author == this.username
      //       ? "background:  #515861"
      //       : "background: #33373d"
      //     : "background: none";
      // m-5 p-3 px-5 rounded-3xl max-w-md
      msg.class =
        msg.sticker.length == 0
          ? msg.author == this.username
            ? "m-5 p-3 px-5 rounded-3xl max-w-md bg-msg-100 text-slate-200"
            : "m-5 p-3 px-5 rounded-3xl max-w-md bg-msg-200 text-slate-200"
          : "m-5 p-3 px-5 rounded-3xl max-w-md text-slate-700 dark:text-slate-100";

      msg.time = new Date(msg.time * 1000).toLocaleTimeString();
      return msg;
    },
    /**
     * Подключение к вебсокетам.
     */
    async createConnection() {
      this.connection.onopen = () => {
        console.log("connected");
      };
      this.connection.onmessage = async (e) => {
        let msg = JSON.parse(e.data).response;
        if (msg.author !== undefined && msg.text !== undefined) {
          this.dialog.push(this.processMessage(msg));
        }
      };
    },
    /**
     * Получение истории чата и запись в dialog.
     */
    async getDialog() {
      const req = await fetch(
        `http://109.248.133.17:8000/rooms/history.get?token=${this.roomtoken}`
      );
      const res = await req.json();
      this.dialog = res["response"]["history"];
      this.dialog.forEach((msg) => {
        msg = this.processMessage(msg);
      });
    },
    async create_empty_room(limit) {
      const req = await fetch(
        `http://109.248.133.17:8000/rooms/new?user_token=${this.token}&name=asd123&users_limit=${limit}`
      );
      const ans = await req.json();
      document.cookie = `room=${ans["response"]["token"]}`;
    },
    /**
     *  Смена комнаты на другую
     */
    async change_room() {
      const req = await fetch("http://109.248.133.17:8000/rooms/getall");
      const ans = await req.json();
      const available_rooms = ans["response"].filter(
        (x) =>
          x["users_limit"] == this.limit &&
          !x["is_full"] &&
          x["token"] != this.roomtoken
      );
      console.log(available_rooms);
      console.log(ans["response"]);
      if (available_rooms.length === 0) {
        // Если нет доступных комнат - создаем новую.
        await this.create_empty_room(this.limit);
      } else {
        const index = Math.floor(Math.random() * available_rooms.length);
        document.cookie = `room=${available_rooms[index]["token"]}`;
        // пробуем войти в комнату ...
        const req = await fetch(
          `http://109.248.133.17:8000/users/room.enter?token=${this.token}&room_token=${available_rooms[index]["token"]}`
        );
        const res = await req.json();
        // если комната достигла лимита - создаем новую.
        if ("detail" in res && res["detail"]["code"] == 6) {
          await this.create_empty_room(this.limit);
        }
      }
      location.href = "http://localhost:3000/#/room";
      window.history.go();
    },
    /**
     * Перемотка в самый низ диалога.
     */
    scrollDown() {
      let chat = document.getElementById("mainChat");
      chat.scrollIntoView({ behavior: "smooth" });
      chat.scrollTop = 100000;
    },
    /**
     * Переводит все :название_смайлика: в смайлики, если это возможно.
     */
    emojify(str) {
      let matches = str.matchAll(/:([\w\d_]+):/g);
      [...matches].forEach((emoji_name) => {
        if (emoji_name[1] in emoji_list) {
          str = str.replace(emoji_name[0], emoji_list[emoji_name[1]]);
        }
      });
      return str;
    },
    /**
     *  Просто отправляет стикер :)
     */
    async sendSticker(sticker) {
      await this.sendMessage("", sticker);
    },
  },
  mounted() {
    this.token = this.getCookie("token");
    this.username = this.getCookie("username");
    this.limit = this.getCookie("limit");
    this.roomtoken = this.getCookie("room");
    this.connection = new WebSocket(
      `ws://109.248.133.17:8000/users/poll?token=${this.token}`
    );
    this.getDialog();
    this.createConnection();
  },
};
</script>

<style>
.scroller {
  max-height: 64vh;
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.scroller::-webkit-scrollbar {
  display: none;
}

.msgtime {
  transform: translate(10px, 5px);
  color: rgba(255, 255, 255, 0.5);
}

a {
  text-decoration: overline;
  color: red;
}

a:visited {
  color: green;
}

.msg-move,
.msg-enter-active,
.msg-leave-active {
  transition: all 0.5s ease;
}

.msg-enter-from {
  opacity: 0;
  transform: translateX(20px);
}

.msg-leave-to {
  opacity: 1;
  transform: translateX(0px);
}

.msg-leave-active {
  position: absolute;
}
</style>
