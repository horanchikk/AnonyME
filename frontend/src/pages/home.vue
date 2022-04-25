<template>
  <div
    class="w-full h-full flex flex-col gap-1 justify-center items-center text-4xl font-semibold text-white helkow"
  >
    <icon />
    <div class="flex flex-col flex-auto items-center justify-center">
      <h1 class="font-medium text-lg text-center">
        Приветствуем вас в
        <a class="font-bold" style="color: #ef313d">AnonyME</a> <br />
        Введите свой ник, чтобы продолжить работу
      </h1>
      <Input placeholder="Введите свой ник" :type="'login'" />
      <Btn :text="'Продолжить'" :type="'lg'" />
    </div>
    <div class="flex w-full h-20 text-xs items-end text-slate-500">
      <a href="https://github.com/horanchikk/hackaton">© AVOCAT 2022</a>
    </div>
  </div>
</template>

<script>
import Icon from "../components/icon.vue";
import Btn from "../components/btn.vue";
import Input from "../components/input.vue";
export default {
  components: {
    Icon,
    Btn,
    Input,
  },
};
</script>

<style></style>
