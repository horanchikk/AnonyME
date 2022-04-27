<template>
  <div class="flex flex-col w-screen h-screen bg">
    <!-- <header class="flex justify-center h-12 bg-slate-700 text-white">
      <ul class="flex h-full items-center gap-5 theader">
        <router-link to="/home"> Home </router-link>
        <router-link to="/first"> First Page </router-link>
        <router-link to="/second"> Second Page </router-link>
      </ul>
    </header> -->
    <div class="flex-auto text-white bg-wwhite dark:bg-bblack">
      <div class="w-screen h-screen pointer-events-none fixed p-10">
        <div class="flex h-full items-end">
          <img
            v-if="theme == 'dark'"
            src="/white_theme.svg"
            class="h-24 cursor-pointer pointer-events-auto transition ease-in-out hover:scale-120"
            alt="whitetheme"
            @click="changeTheme('light')"
          />
          <img
            v-else-if="theme == 'light'"
            src="/black_theme.svg"
            class="h-24 py-full cursor-pointer pointer-events-auto transition ease-in-out hover:scale-120"
            alt="blacktheme"
            @click="changeTheme('dark')"
          />
        </div>
      </div>
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      theme: "light",
    };
  },
  methods: {
    changeTheme(name) {
      this.theme = name;
      localStorage.theme = name;
      console.log(localStorage.theme);
    },
  },
  mounted() {},
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

.mainappwhite {
  background: #fff;
}
</style>
