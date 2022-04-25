<template>
  <button
    style="background: #ef313d"
    class="rounded-xl font-medium"
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
