<template>
  <div class="box box-light">
    <div class="level">
      <div class="level-left">
        <h4 class="title is-4 has-text-secondary">Julio Navarro</h4>
      </div>
      <div class="level-right">
        <b-icon class="cursor-pointer" icon="dots-horizontal" size="is-medium" type="is-dark"></b-icon>
      </div>
    </div>
    <h5 class="title is-5">Personal info:</h5>
    <personal-info-section name="emails"></personal-info-section>
    <personal-info-section name="phone numbers"></personal-info-section>
    <personal-info-section name="address"></personal-info-section>
  </div>
</template>

<script>
  import PersonalInfoSection from './PersonalInfoSection';

  export default {
    name: "contact-detail",
    components: {
      PersonalInfoSection,
    }
  }
</script>

<style lang="scss" scoped>
  @import '../variables';

  .title {
    margin-bottom: 1rem;
  }

  .level {
    margin-bottom: 0rem;
  }

</style>