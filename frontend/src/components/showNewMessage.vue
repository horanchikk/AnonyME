<template>
  <div class="rounded-t-md flex">
    <h1>{{ text }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      can_show: true,
    };
  },
  props: {
    text: String,
  },
};
</script>

<style scoped></style>
