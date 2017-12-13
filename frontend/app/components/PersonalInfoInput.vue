<template>
  <div class="columns is-vcentered">
    <div class="column is-4">
      <b-field :type="error && 'is-danger'" :message="error">
        <b-input :placeholder="placeholder"
                 :value="value"
                 @input="value => $emit('valueChange', value)"
                 :type="fieldType">
        </b-input>
      </b-field>
    </div>
    <div class="column is-3 is-offset-2 has-text-primary has-text-centered">
      <b-select placeholder="Type" :value="infoType" @input="value => $emit('infoTypeChange', value)">
        <option v-for="option in typeOptions" :value="option" :key="option">
          {{ option }}
        </option>
      </b-select>
    </div>
    <div class="column is-2 has-text-centered">
      <custom-radio class="no-control-padding"
                    :value="primary"
                    @input="(value) => $emit('primaryChange', value)">
      </custom-radio>
    </div>

    <div class="column is-1">
      <button class="delete custom-delete" @click="$emit('delete')"></button>
    </div>
  </div>
</template>

<script>
  import { PERSONAL_INFO_TYPES } from "../constants";
  import CustomRadio from "./CustomRadio";

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
    components: { CustomRadio },
    name: "personal-info-input",
    props: ['type', 'value', 'infoType', 'primary', 'error'],
    data() {
      return {}
    },

    watch: {
      value() {
        console.log(this.value, this.infoType, this.primary);
      }
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

  .relative {
    position: relative;
  }

  .no-control-padding {
    > span {
      padding-left: 0 !important;
    }
  }

  .custom-delete {
    margin-top: 2px;
  }
</style>