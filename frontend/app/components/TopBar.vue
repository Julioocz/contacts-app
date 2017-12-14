<template>
  <div class="level">
    <div class="level-item hast-text-left left-level">
      <h4 class="title is-4 has-text-secondary has-text-weight-light">Contacts</h4>
      <span class="has-text-dark" v-if="sharedState.contactCount" style="margin-left: 1rem; margin-top: 0.3rem">{{ sharedState.contactCount }} total</span>
    </div>

    <div class="level-item">
      <b-field>
        <b-input placeholder="Search" v-model="query" type="search" icon="magnify" @keyup.native.enter="search"></b-input>
        <button class="button is-secondary" @click="search">Search</button>
        <button class="button is-primary" v-if="inSearch" @click="undo">
          <b-icon icon="undo"></b-icon>
        </button>
      </b-field>
    </div>

    <div class="level-item right-level">
      <button-icon class="is-primary" @click.native="handleAddContact" icon="account-plus">Add Contact</button-icon>
      <b-tooltip label="Actions for the selected contacts">
        <crud-dropdown :remove="true" @removeClick="handleDeleteClick">
          <button class="button is-info">
            <b-icon icon="dots-horizontal" type="is-primary" size="is-small" custom-size="mdi-18px"></b-icon>
          </button>
        </crud-dropdown>
      </b-tooltip>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  import ButtonIcon from './ButtonIcon';
  import CrudDropdown from './CrudDropdown';
  import store from "../store";
  import { handleContactResponse } from "../utils";

  export default {
    name: "top-bar",
    components: {
      ButtonIcon,
      CrudDropdown,
    },
    data() {
      return {
        sharedState: store.state,
        query: '',
        inSearch: false,
        beforeSearchUrl: '',
      }
    },

    methods: {
      /**
       * Handles the table wide delete action by deleting all the selected contacts on the table.
       *
       * If no contact is selected it displays a toast message to remind the user to select a contact
       * before triggering this action
       */
      handleDeleteClick() {
        const selectedContacts = Object.entries(this.sharedState.checkedContacts)
          .filter(([key, value]) => value)
          .map(([key, value]) => this.sharedState.contacts[key]);

        if (selectedContacts.length === 0) {
          this.$toast.open({
            message: 'You must check a contact first before using this action',
            type: 'is-danger',
          });
          return;
        }

        // Deleting contacts
        store.setLoading(true);
        axios.all(selectedContacts.map(contact => axios.delete(contact.url)))
          .then(() => {
            this.$emit('contactsDeleted');
            store.clearContactCheck();
            this.$toast.open({
              message: 'Contacts removed successfully',
              type: 'is-success',
            })
          })

      },

      /**
       * Handles the app search. If no query is set it handles it as an *undo* action
       */
      search() {
        store.setLoading(true);
        if (this.query === '') {
          this.undo();
          return;
        }

        if (!this.inSearch) {
          this.beforeSearchUrl = this.sharedState.currentEndpoint;
        }
        axios.get(this.sharedState.initEndpoint, { params: { query: this.query } })
          .then(handleContactResponse)
          .then(() => {
            this.inSearch = true;
            store.setLoading(false);
          })
      },

      /**
       * Undo all the searchs or goes back to the non search mode by returning to the initial or beforeSearchUrl
       */
      undo() {
        this.query = '';
        this.inSearch = false;
        store.setLoading(true);
        axios.get(this.beforeSearchUrl)
          .then(handleContactResponse)
          .then(() => store.setLoading(false))
      },

      /**
       * Handles the add contact action by opening the edit/create modal in create mode
       */
      handleAddContact() {
        store.setContactModalMode('create');
        store.setContactModalOpen(true);
        store.setSelectedContact(null);
      }
    }
  }
</script>

<style scoped>
  .title {
    margin-bottom: 0;
  }

  .button {
    margin-right: 10px;
  }

  .left-level {
    justify-content: left;
  }

  .right-level {
    justify-content: right;
  }
</style>