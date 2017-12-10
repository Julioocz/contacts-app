<template>
  <div class="box box-light">
    <div class="level">
      <div class="level-left">
        <h4 class="title is-4 has-text-secondary">Edit Contact</h4>
      </div>
      <div class="level-right">
        <button-icon class="edit-button is-danger" icon="delete">Discard Changes</button-icon>
        <button-icon class="edit-button is-primary" icon="content-save">Save</button-icon>
      </div>
    </div>

    <div class="columns">
      <div class="column">
        <b-field label="First Name" class="label-dark">
          <b-input></b-input>
        </b-field>
      </div>
      <div class="column">
        <b-field label="Last Name" class="label-dark">
          <b-input></b-input>
        </b-field>
      </div>
    </div>

    <h5 class="title is-5 has-text-secondary">Personal info:</h5>
    <personal-info-input-section name="email"></personal-info-input-section>
    <personal-info-input-section name="phoneNumber"></personal-info-input-section>
    <personal-info-input-section name="address"></personal-info-input-section>
  </div>
</template>

<script>
  import ButtonIcon from './ButtonIcon';
  import PersonalInfoInput from './PersonalInfoInput';
  import PersonalInfoInputSection from './PersonalInfoInputSection';

  export default {
    name: "contact-edit",
    components: {
      ButtonIcon,
      PersonalInfoInput,
      PersonalInfoInputSection
    }
  }
</script>

<style lang="scss">
  @import "../variables";

  .edit-button {
    margin-left: 10px;
  }

  .label-dark {
    label {
      color: $dark !important;
    }
  }
</style>