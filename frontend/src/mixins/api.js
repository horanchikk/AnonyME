const api_domen = "109.248.133.17:8000";
const api_url = `http://${api_domen}/`;

export default {
  ws_url: `ws://${api_domen}/`,

  /**
   * Создает нового пользователя с указанным именем.
   */
  async newUser(username) {
    const req = await fetch(`${api_url}users/new?name=${username}`);
    return await req.json();
  },
  /**
   * Возвращает пользователя по токену
   */
  async getUser(token) {
    const req = await fetch(`${api_url}users/get?token=${token}`);
    return await req.json();
  },
  /**
   * Удаляет пользователя по токену
   */
  async removeUser(token) {
    const req = await fetch(`${api_url}users/remove?token=${token}`);
    return await req.json();
  },
  /**
   * Отправляет сообщение в комнату пользователя по его токену
   * text и sticker_id - текст сообщения и ID стикера соответственно.
   */
  async sendMessageUser(token, text, sticker_id) {
    const req = await fetch(
      `${api_url}users/messages.send?token=${token}&sticker_id=${sticker_id}&text=${text}`
    );
    return await req.json();
  },
  /**
   * Возвращает список всех активных пользователей.
   */
  async getAllUsers() {
    const req = await fetch(`${api_url}users/getall`);
    return await req.json();
  },
  /**
   * Входит в комнату с room_token через токен пользователя.
   * При этом выходит из текущей комнаты.
   */
  async enterInRoom(token, room_token) {
    const req = await fetch(
      `${api_url}users/room.enter?token=${token}&room_token=${room_token}`
    );
    return await req.json();
  },
  /**
   * Выходит из текущей комнаты пользователя по токену пользователя.
   * @param {*} token токен пользователя
   */
  async leaveFromRoom(token) {
    const req = await fetch(`${api_url}users/room.leave?token=${token}`);
    return await req.json();
  },

  /**
   * Создает новую комнату, используя токен пользователя
   * @param {*} token токен пользователя
   * @param {*} limit лимит создаваемой комнаты
   * @param {*} name имя создаваемой комнаты
   */
  async newRoom(token, limit, name = "asd12") {
    const req = await fetch(
      `${api_url}rooms/new?user_token=${token}&name=${name}&users_limit=${limit}`
    );
    return await req.json();
  },
  /**
   *Возвращает список всех комнат.
   */
  async getAllRooms() {
    const req = await fetch(`${api_url}rooms/getall`);
    return await req.json();
  },
  /**
   * Возвращает историю сообщений комнаты по ее токену.
   * @param {*} room_token токен комнаты
   */
  async getRoomHistory(room_token) {
    const req = await fetch(`${api_url}rooms/history.get?token=${room_token}`);
    return await req.json();
  },
};
