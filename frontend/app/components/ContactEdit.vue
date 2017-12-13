<template>
  <div class="box box-light">
    <div class="level">
      <div class="level-left">
        <h4 class="title is-4 has-text-secondary">{{ header }}</h4>
      </div>
      <div class="level-right">
        <button-icon class="edit-button is-danger" icon="delete" @click.native="handleDiscard">{{ cancelLabel }}
        </button-icon>
        <button-icon class="edit-button is-primary" type="submit" icon="content-save" @click.native="handleSave">
          {{ submitLabel }}
        </button-icon>
      </div>
    </div>

    <div class="columns">
      <div class="column">
        <b-field
          label="First Name"
          class="label-dark"
          :type="temporalContact.first_name_error && 'is-danger'"
          :message="temporalContact.first_name_error">
          <b-input v-model="temporalContact.first_name"></b-input>
        </b-field>
      </div>
      <div class="column">
        <b-field
          label="Last Name"
          class="label-dark"
          :type="temporalContact.last_name_error && 'is-danger'"
          :message="temporalContact.last_name_error">
          <b-input v-model="temporalContact.last_name"></b-input>
        </b-field>
      </div>
    </div>

    <div class="columns">
      <div class="column is-half">
        <b-field
          label="Birth date"
          class="label-dark"
          :type="temporalContact.date_of_birth_error && 'is-danger'"
          :message="temporalContact.date_of_birth_error">
          <b-datepicker
            v-model="temporalContact.date_of_birth"
            placeholder="Click to select..."
            :date-parser="date => new Date(date)"
            :date-formatter="dateToIsoSimplified"
            :max-date="new Date()"
            icon="calendar-today">
          </b-datepicker>
        </b-field>
      </div>
    </div>

    <h5 class="title is-5 has-text-secondary">Personal info:</h5>
    <personal-info-input-section
      type="email"
      valueProperty="email"
      :info.sync="temporalContact.emails">
    </personal-info-input-section>
    <personal-info-input-section
      type="phoneNumber"
      valueProperty="number"
      :info.sync="temporalContact.phone_numbers">
    </personal-info-input-section>
    <personal-info-input-section
      type="address"
      valueProperty="name"
      :info.sync="temporalContact.addresses">
    </personal-info-input-section>
  </div>
</template>

<script>
  import axios from 'axios';

  import ButtonIcon from './ButtonIcon';
  import PersonalInfoInput from './PersonalInfoInput';
  import PersonalInfoInputSection from './PersonalInfoInputSection';
  import store from "../store";
  import { TYPE_HOME, TYPE_MOVIL, TYPE_PERSONAL } from "../constants";
  import { emptyContactInfo, handleContactResponse } from "../utils";

  const emptyContact = () => ({
    first_name: null,
    last_name: null,
    date_of_birth: null,
    emails: [emptyContactInfo('email', true)],
    addresses: [emptyContactInfo('address', true)],
    phone_numbers: [emptyContactInfo('phoneNumber', true)]
  });

  export default {
    name: "contact-edit",
    components: {
      ButtonIcon,
      PersonalInfoInput,
      PersonalInfoInputSection
    },

    data() {
      const editMode = store.state.contactModalMode === 'edit';
      const temporalContact = editMode ? Object.assign({}, store.state.selectedContact) : emptyContact();
      // Transforming the date to a date object if in edit mode (is needed for the datepicker comp)
      if (editMode && temporalContact.date_of_birth) {
        temporalContact.date_of_birth = new Date(temporalContact.date_of_birth)
      }
      ;

      return {
        sharedState: store.state,
        temporalContact: temporalContact,
      }
    },

    computed: {
      header() {
        return this.editMode ? 'Edit contact' : 'Create contact';
      },

      editMode() {
        return store.state.contactModalMode === 'edit';
      },

      submitLabel() {
        return this.editMode ? 'Save' : 'Create';
      },

      cancelLabel() {
        return this.editMode ? 'Discard changes' : 'Discard contact';
      },

      successMessage() {
        return this.editMode ? 'The contact has been edited successfully' : 'The contact has been created successfully'
      },

      saveEndpoint() {
        return this.editMode ? this.temporalContact.url : this.sharedState.initEndpoint;
      }

    },

    methods: {
      handleDiscard() {
        if (confirm('Are you sure that you want to discard all your progress?')) {
          store.setContactModalOpen(false);
        }
      },

      handleSave() {
        store.setLoading(true);
        const payload = Object.assign({}, this.temporalContact);
        if (payload.date_of_birth) {
          payload.date_of_birth = this.dateToIsoSimplified(payload.date_of_birth)
        }

        const method = this.editMode ? 'put' : 'post';
        axios[method](this.saveEndpoint, payload)
          .then(this.handleGoodResponse)
          .catch(this.handleBadResponse)
      },

      dateToIsoSimplified(date) {
        return date.toISOString().split('T')[0]
      },

      handleGoodResponse() {
        store.setContactModalOpen(false);
        axios.get(this.sharedState.initEndpoint)
          .then(handleContactResponse)
          .then(() => store.setCurrentEndpoint(this.sharedState.initEndpoint))
          .then(() => store.setLoading(false))
          .then(() => this.$toast.open({ message: this.successMessage, type: 'is-success' }));
      },

      handleBadResponse(err) {
        const { data } = err.response;
        console.log(data);
        const errors = {
          first_name_error: data.first_name && data.first_name[0],
          last_name_error: data.last_name && data.last_name[0],
          date_of_birth_error: data.date_of_birth && data.date_of_birth[0],
        };
        this.temporalContact = Object.assign({}, this.temporalContact, errors);
        // this.temporalContact.first_name_error = data.first_name && data.first_name[0];
        // this.temporalContact.last_name_error = data.last_name && data.last_name[0];
        // this.temporalContact.date_of_birth_error = data.date_of_birth && data.date_of_birth[0];
        data.emails.forEach((error, index) => this.$set(this.temporalContact.emails[index], 'error', error.email));
        data.addresses.forEach((error, index) => this.$set(this.temporalContact.addresses[index], 'error', error.name));
        data.phone_numbers.forEach((error, index) => this.$set(this.temporalContact.phone_numbers[index], 'error', error.number));
        store.setLoading(false);
        this.$toast.open({
          message: 'There was an error processing your form. Please review the marked fields',
          type: 'is-danger',
        })
      }

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