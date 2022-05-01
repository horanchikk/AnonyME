<template>
  <div v-if="opened">
    <div
      v-for="line in stickers_grid"
      :key="line"
      class="flex justify-center gap-5 my-2 animate__animated animate__fadeInDown"
    >
      <div class="inline-block cursor-pointer" v-for="file in line" :key="file">
        <img
          class="stickers h-14 hover:h-16"
          :src="'/stickers/' + file['file']"
          @click="$emit('choise', file['id'])"
        />
      </div>
    </div>
  </div>
</template>

<script>
import stickers from "../../public/stickers/stickers.json";

export default {
  data() {
    return {
      opened: true,
      stickers_grid: [[]],
      sticker_grid_width: 5,
    };
  },
  methods: {
    togglePanel() {
      this.opened = !this.opened;
    },
  },
  mounted() {
    stickers.forEach((e) => {
      if (
        this.stickers_grid[this.stickers_grid.length - 1].length <
        this.sticker_grid_width
      ) {
        this.stickers_grid[this.stickers_grid.length - 1].push(e);
      } else {
        this.stickers_grid.push([e]);
      }
    });
  },
};
</script>

<style scoped></style>
