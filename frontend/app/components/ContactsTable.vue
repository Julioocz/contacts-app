<template>
  <div class="contact-table">
    <table-header></table-header>
    <contact-item v-for="_ in 10"></contact-item>
  </div>
</template>

<script>
  import TableHeader from './TableHeader';
  import ContactItem from './ContactItem';

  export default {
    name: "contacts-table",
    components: {
      TableHeader,
      ContactItem,
    },
  }
</script>

<style lang="scss" scoped>
  .contact-table {
    margin-top: 4vh;
    margin-bottom: 2vh;
  }
</style>