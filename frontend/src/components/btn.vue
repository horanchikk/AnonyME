<template>
  <button
    class="bg-rred-200 transition ease-in-out duration-200 rounded-xl font-medium hover:bg-rred-100 hover:shadow-lg"
    :class="{
      'text-xl py-2 px-4': type === 'sm',
      'text-xl py-2 px-24': type === 'lg',
      'text-2xl py-4 px-8': type === 'md',
    }"
  >
    {{ text }}
  </button>
</template>

<script>
export default {
  props: {
    type: String,
    text: String,
  },
};
</script>

<style />
