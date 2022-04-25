<template>
  <div class="flex flex-col bg-slate-500 w-screen h-screen font-sans">
    <header class="flex justify-center h-12 bg-slate-700 text-white">
      <ul class="flex h-full items-center gap-5 theader">
        <router-link to="/home"> Home </router-link>
        <router-link to="/first"> First Page </router-link>
        <router-link to="/second"> Second Page </router-link>
      </ul>
    </header>
    <div class="flex-auto">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  data() {},
};
</script>

<style />
