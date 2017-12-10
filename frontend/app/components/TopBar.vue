<template>
  <div class="level">
    <div class="level-left">
      <h4 class="title is-4 has-text-secondary has-text-weight-light">Contacts</h4>
    </div>
    <div class="level-right">
      <button-icon class="is-primary" @click="$emit('addContact')" icon="action-plus">Add Contact</button-icon>
    </div>
  </div>
</template>

<script>
  import ButtonIcon from './ButtonIcon';

  export default {
    name: "top-bar",
    components: {
      ButtonIcon,
    }
  }
</script>

<style scoped>
</style>