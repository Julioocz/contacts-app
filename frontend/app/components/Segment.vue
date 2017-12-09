<template>
  <div class="segment">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    name: "segment"
  }
</script>

<style lang="scss" scoped>
  .segment {
    padding: 2.5%;
    border-radius: 5px;
  }
</style>