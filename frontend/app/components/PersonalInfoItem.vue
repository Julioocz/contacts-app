<template>
  <div class="box is-shadowless contact-info-box">
    <div class="columns">
      <div class="column">
        julioocz@gmail.com
      </div>
      <div class="column is-2 has-text-primary has-text-centered">
        <b>Personal</b>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "personal-info-item"
  }
</script>

<style lang="scss" scoped>

  .contact-info-box {
    border: 1px solid rgba(120, 144, 156, 0.15);
    padding: 1rem;
    margin-bottom: 0.1rem;
    border-radius: 0;

    .column {
      padding: 0.3rem;
    }
  }
</style>