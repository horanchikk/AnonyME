<template>
  <input
    v-if="type === 'chat'"
    v-model="chatmessage"
    style="background: #575e63"
    placeholder="Введите сообщение.."
    class="w-96 p-4 text-left font-semibold text-xl transition ease-in-out duration-200 rounded-lg outline-none bg-slate-200 text-teal-400 focus:shadow-2xl"
    type="text"
    @input="this.$emit('chatmessage', this.chatmessage)"
  />
  <input
    v-else-if="type === 'login'"
    v-model="username"
    class="w-96 my-5 text-center transition ease-in-out duration-200 rounded-lg outline-none p-1 text-wwhite bg-slate-700 shadow-black focus:shadow-2xl dark:bg-slate-700 inputlogin"
    type="text"
    @input="this.$emit('username', this.username)"
  />
  <h1 v-else type="text">Type of Input is not found</h1>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      chatmessage: "",
    };
  },
  props: {
    text: String,
    type: String,
  },
};
</script>

<style>
.inputlogin:focus {
  box-shadow: 0 0 8px 1px white;
}
</style>
