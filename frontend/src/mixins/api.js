const api_domen = "localhost:8000";
const api_url = `http://${api_domen}/`;

/**
 * Отправляет запрос на url
 * @param {String} url
 */
async function sendReqJson(url) {
  const req = await fetch(url);
  return await req.json();
}

export default {
  /** Хранит ссылку для подключения к вебсокетам. */
  ws_url: `ws://${api_domen}/`,

  /**
   * Создает нового пользователя с указанным именем.
   * @param {String} username имя создаваемого пользователя.
   * @returns объект пользователя или объект ошибки.
   */
  async newUser(username) {
    return await sendReqJson(`${api_url}users/new?name=${username}`);
  },
  /**
   * Возвращает пользователя по токену.
   * @param {String} token токен пользователя.
   * @returns объект пользователя или объект ошибки.
   */
  async getUser(token) {
    return await sendReqJson(`${api_url}users/get?token=${token}`);
  },
  /**
   * Удаляет пользователя по токену.
   * @param {String} username имя создаваемого пользователя.
   */
  async removeUser(token) {
    return await sendReqJson(`${api_url}users/remove?token=${token}`);
  },
  /**
   * Отправляет сообщение в комнату пользователя по его токену
   * @param {String} token токен пользователя.
   * @param {String} text текст сообщения.
   * @param {Int} sticker_id ID стикера.
   */
  async sendMessageUser(token, text, sticker_id) {
    return await sendReqJson(
      `${api_url}users/messages.send?token=${token}&sticker_id=${sticker_id}&text=${text}`
    );
  },
  /**
   * Возвращает список всех активных пользователей.
   */
  async getAllUsers() {
    return await sendReqJson(`${api_url}users/getall`);
  },
  /**
   * Входит в комнату с room_token через токен пользователя.
   * При этом выходит из текущей комнаты.
   * @param {String} token токен пользователя.
   * @param {String} roomtoken токен комнаты.
   */
  async enterInRoom(token, roomtoken) {
    return await sendReqJson(
      `${api_url}users/room.enter?token=${token}&room_token=${roomtoken}`
    );
  },
  /**
   * Выходит из текущей комнаты пользователя по токену пользователя.
   * @param {String} token токен пользователя.
   */
  async leaveFromRoom(token) {
    return await sendReqJson(`${api_url}users/room.leave?token=${token}`);
  },

  /**
   * Создает новую комнату, используя токен пользователя
   * @param {String} token токен пользователя.
   * @param {Int} limit лимит создаваемой комнаты.
   * @param {String} name имя создаваемой комнаты.
   */
  async newRoom(token, limit, name = "asd12") {
    return await sendReqJson(
      `${api_url}rooms/new?user_token=${token}&name=${name}&users_limit=${limit}`
    );
  },
  /**
   * Возвращает комнату по ее токену, если это возможно.
   * @param {String} token токен комнаты
   * @returns Объект комнаты или объект ошибки
   */
  async getRoom(token) {
    return await sendReqJson(`${api_url}rooms/get?token=${token}`);
  },
  /**
   * Удаляет комнату по ее токену, если это возможно.
   * @param {String} token токен комнаты
   */
  async removeRoom(token) {
    return await sendReqJson(`${api_url}rooms/remove?token=${token}`);
  },
  /**
   *Возвращает список всех комнат.
   */
  async getAllRooms() {
    return await sendReqJson(`${api_url}rooms/getall`);
  },
  /**
   * Возвращает историю сообщений комнаты по ее токену.
   * @param {String} roomtoken токен комнаты
   */
  async getRoomHistory(roomtoken) {
    return await sendReqJson(`${api_url}rooms/history.get?token=${roomtoken}`);
  },
};
