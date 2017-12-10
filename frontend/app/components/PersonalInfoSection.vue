<template>
  <div class="personal-info-section">
    <h6 class="title is-6 section-title has-text-dark">
      Emails
    </h6>
    <personal-info-item></personal-info-item>
    <personal-info-item></personal-info-item>
  </div>
</template>

<script>
  import PersonalInfoItem from './PersonalInfoItem';

  export default {
    name: "personal-info-section",
    components: { PersonalInfoItem, }

  }
</script>

<style lang="scss" scoped>
  .section-title {
    margin-bottom: 0.5rem;
  }

  .personal-info-section {
    margin-bottom: 1rem;

    .title {
      margin-left: 0.15rem;
    }
  }
</style>