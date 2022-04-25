<template>
  <input v-if="type === 'chat'" type="text" />
  <input
    v-else-if="type === 'login'"
    class="w-96 my-5 text-center rounded-lg outline-none p-1 bg-slate-200 text-teal-600"
    type="text"
  />
  <h1 v-else type="text">Type of Input is not found</h1>
</template>

<script>
export default {
  props: {
    text: String,
    type: String,
  },
};
</script>

<style lang="scss" scoped></style>
