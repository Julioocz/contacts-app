<template>
  <div class="columns">
    <div class="column is-1 has-text-centered">
      <slot name="first"></slot>
    </div>
    <div class="column">
      <slot name="second"></slot>
    </div>
    <div class="column">
      <slot name="third"></slot>
    </div>
    <div class="column">
      <slot name="forth"></slot>
    </div>
    <div class="column">
      <slot name="fifth"></slot>
    </div>
    <div class="column">
      <slot name="sixth"></slot>
    </div>
    <div class="column">
      <slot name="seventh"></slot>
    </div>
    <div class="column is-1">
      <slot name="eighth"></slot>
    </div>
  </div>
</template>

<script>
  export default {
    name: "columns"
  }
</script>

<style scoped>

</style>