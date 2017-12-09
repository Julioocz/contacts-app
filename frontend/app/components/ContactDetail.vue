<template>
  <div class="box contact-detail-box ">
    <div class="level">
      <div class="level-left">
        <h4 class="title is-4 has-text-secondary">Julio Navarro</h4>
      </div>
      <div class="level-right">
        <b-icon class="cursor-pointer" icon="dots-horizontal" size="is-medium" type="is-dark"></b-icon>
      </div>
    </div>
    <h5 class="title is-5 has-text-dark">Personal info:</h5>
    <div class="personal-info-section">
      <h6 class="title is-6 section-title">Email:</h6>
      <personal-info-item></personal-info-item>
      <personal-info-item></personal-info-item>
    </div>
    <div class="personal-info-section">
      <h6 class="title is-6 section-title">Phone numbers:</h6>
      <personal-info-item></personal-info-item>
      <personal-info-item></personal-info-item>
      <personal-info-item></personal-info-item>
    </div>
    <div class="personal-info-section">
      <h6 class="title is-6 section-title">Address:</h6>
      <personal-info-item></personal-info-item>
      <personal-info-item></personal-info-item>
      <personal-info-item></personal-info-item>
    </div>
  </div>

</template>

<script>
  import PersonalInfoItem from './PersonalInfoItem';

  export default {
    name: "contact-detail",
    components: {
      PersonalInfoItem,
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

  .section-title {
    margin-bottom: 0.5rem;
  }

  .contact-detail-box {
    width: 100%;
    margin: auto;
    background-color: $light;
  }

  .personal-info-section {
    margin-bottom: 1rem;

    .title {
      margin-left: 0.15rem;
    }
  }

</style>