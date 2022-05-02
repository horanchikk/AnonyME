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
                  v-if="
                    [2, 3, 4].filter((x) => msg.action_code == x).length > 0
                  "
                  class="flex justify-center font-semibold text-xl text-slate-700 dark:text-slate-200"
                >
                  {{ msg.author }} {{ msg.action }}
                </div>

                <!-- Сообщение пользователя -->
                <div
                  v-else-if="msg.author === this.username"
                  class="flex justify-end"
                >
                  <div :class="msg.class">
                    <!-- Автор сообщения, в своем сообщении не стоит его отображать
                    <p class="mx-5 font-semibold">
                      {{ msg.author }}
                    </p> -->
                    <!-- Текст сообщения -->
                    <p
                      v-if="msg.sticker.length == 0"
                      v-html="msg.text"
                      class="font-normal"
                    ></p>
                    <!-- Стикер при наличии -->
                    <img
                      v-else
                      class="h-48"
                      :src="'/stickers/' + msg.sticker[0]['file']"
                    />
                    <!-- Время сообщения -->
                    <div
                      class="flex mx-4 items-end justify-end text-slate-200 msgtime"
                    >
                      {{ msg.time }}
                    </div>
                  </div>
                </div>

                <!-- Сообщение собеседника -->
                <div v-else>
                  <div :class="msg.class">
                    <!-- Автор -->
                    <p class="mx-5 font-semibold">
                      {{ msg.author }}
                    </p>
                    <!-- Текст -->
                    <div v-if="msg.sticker.length == 0">
                      <p class="py-3" v-html="msg.text"></p>
                      <div class="flex mx-4 items-end justify-end msgtime">
                        {{ msg.time }}
                      </div>
                    </div>
                    <!-- Стикер -->
                    <div v-else>
                      <img
                        class="h-48"
                        :src="'/stickers/' + msg.sticker[0]['file']"
                      />
                      <div class="flex mx-4 items-end justify-start msgtime">
                        {{ msg.time }}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </TransitionGroup>
          </div>
          <div>
            <!-- Панель со стикерами -->
            <stickerPanel @choise="sendSticker" />
            <div class="flex h-14">
              <!-- Поле ввода для сообщений -->
              <Input
                @chatmessage="setMessage"
                v-on:keyup.enter="sendMessage(this.chatmessage, 0)"
                id="chatInput"
                class="w-full"
                :type="'chat'"
              />
              <!-- Кнопка отправки сообщений -->
              <img
                @click="sendMessage(this.chatmessage, 0)"
                class="h-full ml-4 px-4 cursor-pointer transition ease-in-out duration-200 hover:scale-125"
                src="/send.svg"
                alt="send"
              />
            </div>

            <!-- Нижние кнопки -->
            <div class="flex w-full justify-center">
              <div class="flex w-4/6 p-5 justify-between">
                <!-- Найти другого (Сменить комнату) -->
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

                <!-- Прекратить общение (Выйти из комнаты) -->
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

                <!-- Жалоба (Здесь должно появляться окно голосования) -->
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
import API from "../mixins/api";
import cookies from "../mixins/cookies";

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
  mixins: [API, cookies],
  methods: {
    /**
     * Очистка всех куки и удаление пользователя.
     */
    updateToken() {
      this.token = document.cookie;
    },
    setMessage(value) {
      this.chatmessage = value;
    },
    /**
     * Выход из аккаунта с последующим удалением аккаунта.
     */
    async logout() {
      // 500 status code + CORS ERROR => FastAPI error
      await API.removeUser(this.token);
      document.cookie = 'token=""';
      document.cookie = 'username=""';
      document.cookie = 'limit=""';
      location.href = "http://localhost:3000";
    },
    /**
     * Отправка сообщения (через вебсокеты).
     * Для отправки текста следует указать `0` для `sticker`.
     * Для отправки стикера следует указать `""` для `text`.
     * @param {String} text текст сообщения
     * @param {Int} sticker ID стикера.
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
     *  Просто отправляет стикер.
     */
    async sendSticker(sticker) {
      await this.sendMessage("", sticker);
    },
    /**
     *  Просто отправляет сообщение.
     */
    async sendText(text) {
      await this.sendMessage(text, 0);
    },
    /**
     * Обработка сообщения:
     *   - обработка md-текста
     *   - обработка эмоджи
     * @param {String} msg текст сообщения.
     * @returns обработанное сообщение
     */
    processMessage(msg) {
      msg.text = this.emojify(marked(msg.text));
      msg.sticker = stickers_list.filter((x) => x["id"] == msg.sticker_id);
      msg.class =
        msg.sticker.length == 0
          ? msg.author == this.username
            ? "m-5 p-3 px-5 rounded-3xl max-w-xs bg-msg-100 text-slate-200"
            : "m-5 p-3 px-5 rounded-3xl max-w-xs w-fit bg-msg-200 text-slate-200"
          : "m-5 p-3 px-5 rounded-3xl max-w-xs text-slate-700 dark:text-slate-100";

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
      const res = await API.getRoomHistory(this.roomtoken);
      this.dialog = res["response"]["history"];
      this.dialog.forEach((msg) => {
        msg = this.processMessage(msg);
      });
    },
    /**
     * Создание пустой комнаты с указанным лимитом.
     * @param {int} limit лимит комнаты.
     */
    async create_empty_room(limit) {
      const ans = await API.newRoom(this.token, limit);
      document.cookie = `room=${ans["response"]["token"]}`;
    },
    /**
     *  Смена комнаты на другую
     */
    async change_room() {
      const ans = await API.getAllRooms();
      const available_rooms = ans["response"].filter(
        (x) =>
          x["users_limit"] == this.limit &&
          !x["is_full"] &&
          x["token"] != this.roomtoken
      );
      if (available_rooms.length === 0) {
        // Если нет доступных комнат - создаем новую.
        await this.create_empty_room(this.limit);
      } else {
        const index = Math.floor(Math.random() * available_rooms.length);
        document.cookie = `room=${available_rooms[index]["token"]}`;
        // пробуем войти в комнату ...
        const res = await API.enterInRoom(
          this.token,
          available_rooms[index]["token"]
        );
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
     * @param {string} str строка, содержащая в себе :SMILENAME:
     * @returns обработанная строка
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
  },
  mounted() {
    this.token = cookies.getCookie("token");
    this.username = cookies.getCookie("username");
    this.limit = cookies.getCookie("limit");
    this.roomtoken = cookies.getCookie("room");
    this.connection = new WebSocket(
      `${API.ws_url}users/poll?token=${this.token}`
    );
    this.getDialog();
    this.createConnection();
  },
};
</script>

<style />
