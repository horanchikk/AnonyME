<template>
  <input v-if="type === 'chat'" type="text" />
  <input
    v-else-if="type === 'login'"
    v-model="username"
    class="w-96 my-5 text-center transition ease-in-out duration-200 rounded-lg outline-none p-1 bg-slate-200 text-teal-600 focus:shadow-xl"
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
    };
  },
  props: {
    text: String,
    type: String,
  },
};
</script>

<style lang="scss" scoped></style>
