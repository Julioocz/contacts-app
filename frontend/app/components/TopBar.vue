<template>
  <div class="level">
    <div class="level-left">
      <h4 class="title is-4 has-text-secondary has-text-weight-light">Contacts</h4>
    </div>
    <div class="level-right">
      <button class="button is-primary" @click="$emit('addContact')">
        <span class="icon"><i class="mdi mdi-18px mdi-account-plus"></i></span> Add Contact
      </button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "top-bar"
  }
</script>

<style scoped>
  .icon {
    margin-right: 5px !important;
  }
</style>