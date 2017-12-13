<template>
  <label class="b-radio radio"
         ref="label"
         @keydown.prevent.enter.space="$refs.label.click()">
    <input type="radio" :checked="this.value" @change="(e) => $emit('input', e.target.value)">
    <span class="check"></span>
  </label>
</template>

<script>
  export default {
    name: "custom-radio",
    props: ['value']
  }
</script>

<style scoped>

</style>