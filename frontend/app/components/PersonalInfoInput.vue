<template>
  <div class="columns is-vcentered">
    <div class="column is-4">
      <b-field>
        <b-input :placeholder="placeholder" :type="fieldType"></b-input>
      </b-field>
    </div>
    <div class="column is-3 is-offset-3 has-text-primary has-text-centered">
      <b-select placeholder="Type">
        <option v-for="option in typeOptions" :value="option" :key="option">
          {{ option }}
        </option>
      </b-select>
    </div>
    <div class="column is-2 has-text-centered">
      <b-radio class="no-control-padding"></b-radio>
    </div>
  </div>
</template>

<script>
  import { PERSONAL_INFO_TYPES } from "../constants";

  const PLACEHOLDER_MAPPING = {
    email: 'Email',
    address: 'Address',
    phoneNumber: 'Phone number',
  };

  const FIELDTYPE_MAPPING = {
    email: 'email',
    address: 'text',
    phoneNumber: 'text',
  };

  export default {
    name: "personal-info-input",
    props: ['type'],
    data() {
      return {}
    },

    computed: {
      typeOptions() {
        return PERSONAL_INFO_TYPES[this.type];
      },

      placeholder() {
        return PLACEHOLDER_MAPPING[this.type];
      },

      fieldType() {
        return FIELDTYPE_MAPPING[this.type];
      }
    }
  }
</script>

<style lang="scss">
  .columns {
    margin-bottom: 0;
  }

  .no-control-padding {
    > span {
      padding-left: 0 !important;
    }
  }
</style>