<template>
  <div class="box is-paddingless contact-item">
    <columns>
      <b-checkbox slot="first" v-model="checked" class="align-text-top">
      </b-checkbox>
      <span slot="second">Julio</span>
      <span slot="third">Navarro</span>
      <span slot="forth">julioocz@gmail.com</span>
      <span slot="fifth">+584248882574</span>
      <span slot="sixth">Barcelona, Ven</span>
      <span slot="seventh">02/24/94</span>
      <b-icon slot="eighth" class="cursor-pointer" icon="dots-horizontal" type="is-dark"></b-icon>
    </columns>
  </div>
</template>

<script>
  import Columns from './Columns';

  export default {
    name: "contact-item",
    components: {
      Columns,
    },
    data() {
      return {
        checked: false,
      }
    }
  }
</script>

<style lang="scss" scoped>
  .contact-item {
    -webkit-box-shadow: none;
    -moz-box-shadow: none;
    box-shadow: none;

    &:not(:last-child) {
      margin-bottom: 1.2rem;
    }

    .column {
      padding: 0.5rem;
    }
  }
</style>