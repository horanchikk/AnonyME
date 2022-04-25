<template>
  <div class="flex flex-col w-screen h-screen bg">
    <!-- <header class="flex justify-center h-12 bg-slate-700 text-white">
      <ul class="flex h-full items-center gap-5 theader">
        <router-link to="/home"> Home </router-link>
        <router-link to="/first"> First Page </router-link>
        <router-link to="/second"> Second Page </router-link>
      </ul>
    </header> -->
    <div class="flex-auto mainapp">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  data() {},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300&display=swap");
body {
  font-family: "Nunito Sans", sans-serif;
}
.mainapp {
  background: #222429;
}
</style>
