<template>
  <div>
    <div class="columns">
      <div class="column is-4">
        <span class="title is-6 section-title has-text-dark">{{ header }}:</span>
      </div>
      <div class="column is-3 is-offset-3 has-text-dark">
        Type
      </div>
      <div class="column is-2 has-text-centered has-text-dark">
        Primary
      </div>
    </div>
    <personal-info-input :type="name"></personal-info-input>
    <personal-info-input :type="name"></personal-info-input>
    <personal-info-input :type="name"></personal-info-input>
    <div class="columns is-">
      <div class="column is-2 is-offset-10 has-text-centered">
        <b-icon icon="plus-circle" type="is-primary" class="cursor-pointer"></b-icon>
      </div>
    </div>
  </div>
</template>

<script>
  import PersonalInfoInput from './PersonalInfoInput';

  const HEADER_MAPPING = {
    email: 'Emails:',
    phoneNumber: 'Phone Number',
    address: 'Addresses'
  };

  export default {
    name: "personal-info-input-headers",
    props: ['name'],
    components: { PersonalInfoInput, },
    computed: {
      header() {
        return HEADER_MAPPING[this.name];
      }
    },
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