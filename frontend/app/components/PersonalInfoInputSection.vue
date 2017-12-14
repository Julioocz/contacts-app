<template>
  <div>
    <div class="columns">
      <div class="column is-4">
        <span class="title is-6 section-title has-text-dark">{{ header }}:</span>
      </div>
      <div class="column is-3 is-offset-2 has-text-dark">
        Type
      </div>
      <div class="column is-2 has-text-centered has-text-dark">
        Primary
      </div>
    </div>
    <personal-info-input
      v-for="(item, index) in info"
      :type="type"
      :value="item[valueProperty]"
      :infoType="item.info_type"
      :primary="item.primary"
      :key="index"
      :error="item.error"
      @valueChange="value => handleChange(index, value, valueProperty)"
      @infoTypeChange="value => handleChange(index, value, 'info_type')"
      @primaryChange="value => handleChange(index, value, 'primary')"
      @delete="() => handleDelete(index)"
    >
    </personal-info-input>
    <div class="columns">
      <div class="column is-2 is-offset-9 has-text-centered">
        <b-icon @click.native="addInfoItem" icon="plus-circle" type="is-primary" class="cursor-pointer"></b-icon>
      </div>
    </div>
  </div>
</template>

<script>
  import PersonalInfoInput from './PersonalInfoInput';
  import { CONTACT_HEADER_MAPPING } from "../constants";
  import { emptyContactInfo } from "../utils";

  export default {
    name: "personal-info-input-headers",
    props: ['type', 'info', 'valueProperty'],
    components: { PersonalInfoInput, },
    computed: {
      header() {
        return CONTACT_HEADER_MAPPING[this.type];
      }
    },

    watch: {
      info() {
        console.log(this.info);
      }
    },
    methods: {
      handleChange(index, value, valueProperty) {
        console.log('Handling change', index, value, valueProperty);
        const newInfo = this.info.slice();
        // There can only be a primary value
        if (valueProperty === 'primary') {
          newInfo.forEach(item => item.primary = false);
        }
        console.log(newInfo);
        newInfo[index][valueProperty] = value;
        newInfo[index].error = '';
        this.$emit('update:info', newInfo);
      },

      handleDelete(index) {
        console.log('DELETE');
        const newInfo = this.info.slice();
        const removedItem = newInfo.splice(index, 1);
        // Checking if the removed item was the primary one. If so the first item is set to primary
        if (removedItem[0].primary && newInfo.length > 0) {
          newInfo[0].primary = true
        }

        this.$emit('update:info', newInfo);
      },

      addInfoItem() {
        console.log('ADD ITEM');
        const newInfo = this.info.slice();
        newInfo.push(emptyContactInfo(this.type, newInfo.length === 0));
        this.$emit('update:info', newInfo);
      }
    }
  }
</script>

<style lang="scss" scoped>
  .columns {
    margin-bottom: 0.2rem;
  }

  .rounded-button {
    border-radius: 50%;
  }
</style>