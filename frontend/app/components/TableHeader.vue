<template>
  <columns>
    <b-checkbox slot="first" class="align-text-top">
    </b-checkbox>
    <span slot="second" class="has-text-dark">Fist name</span>
    <span slot="third" class="has-text-dark">Last name</span>
    <span slot="forth" class="has-text-dark">Email</span>
    <span slot="fifth" class="has-text-dark">Phone number</span>
    <span slot="sixth" class="has-text-dark">Address</span>
    <span slot="seventh" class="has-text-dark">Birth Date</span>
    <div slot="eighth">
      <page-changer></page-changer>
    </div>
  </columns>
</template>

<script>
  import Columns from './Columns';
  import PageChanger from './PageChanger';

  export default {
    name: "table-header",
    components: {
      Columns,
      PageChanger,
    },
  }
</script>

<style scoped>

</style>