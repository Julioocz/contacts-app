<template>
  <div class="box box-light">
    <div class="level">
      <div class="level-left">
        <h4 class="title is-4 has-text-secondary">{{ name }}</h4>
      </div>
      <div class="level-right">
        <crud-dropdown :remove="true"
                       :edit="true"
                       @editClick="() => editContact(sharedState.selectedContactIndex)"
                       @removeClick="() => deleteContact(sharedState.selectedContactIndex)">
          <b-icon class="cursor-pointer" icon="dots-horizontal" size="is-medium" type="is-dark"></b-icon>
        </crud-dropdown>
      </div>
    </div>
    <h5 class="title is-5 has-text-secondary">Personal info:</h5>
    <h6 class="title is-6 has-text-dark" v-if="contact.date_of_birth">Birth date: {{ contact.date_of_birth }}</h6>
    <personal-info-section type="email" :info="contact.emails" valueProperty="email"></personal-info-section>
    <personal-info-section type="phoneNumber" :info="contact.phone_numbers" valueProperty="number">
    </personal-info-section>
    <personal-info-section type="address" :info="contact.addresses" valueProperty="name"></personal-info-section>
  </div>
</template>

<script>
  import PersonalInfoSection from './PersonalInfoSection';
  import store from "../store";
  import CrudDropdown from './CrudDropdown';
  import updateRemoveDetailMixin from "./mixins/updateRemoveDetailMixin";

  export default {
    name: "contact-detail",
    mixins: [updateRemoveDetailMixin],
    components: {
      PersonalInfoSection,
      CrudDropdown,
    },
    data() {
      return {
        sharedState: store.state,
      }
    },

    computed: {
      contact() {
          return this.sharedState.selectedContact;
      },

      name() {
        return `${this.contact.first_name} ${this.contact.last_name}`
      },
    },
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