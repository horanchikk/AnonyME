<template>
  <div v-if="opened">
    <div
      v-for="line in stickers_grid"
      :key="line"
      class="flex justify-center gap-5 my-2"
    >
      <img
        class="h-14 inline-block cursor-pointer hover:scale-120"
        v-for="file in line"
        :key="file"
        :src="'/stickers/' + file['file']"
        @click="$emit('choise', file['id'])"
      />
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
    console.log(this.stickers_grid);
  },
};
</script>

<style scoped></style>
