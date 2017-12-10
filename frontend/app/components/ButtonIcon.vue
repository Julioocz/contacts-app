<template>
  <button class="button">
    <b-icon :icon="icon" size="is-small" custom-size="mdi-18px"></b-icon>
    <slot></slot>
  </button>
</template>

<script>
  export default {
    name: "button-icon",
    props: ['icon'],
  }
</script>

<style scoped>
  .icon {
    margin-right: 5px !important;
  }
</style>