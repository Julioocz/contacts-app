<template>
  <tr @click="handleContactClick" :class="{'is-selected': checked}">
    <td ref="checkbox">
      <b-checkbox @input="value => $emit('checked', value)" :value="checked" class="align-text-top"></b-checkbox>
    </td>
    <td>{{ contact.first_name }}</td>
    <td>{{ contact.last_name }}</td>
    <td>{{ primaryEmail }}</td>
    <td>{{ primaryPhoneNumber }}</td>
    <td>{{ primaryAddress }}</td>
    <td>{{ contact.date_of_birth }}</td>
    <td>
      <crud-dropdown
        :remove="true"
        :edit="true"
        :detail="true"
        @detailClick="$emit('openDetails')"
        @removeClick="$emit('deleteContact')"
        @editClick="$emit('editContact')">
        <b-icon ref="actions" class="cursor-pointer" icon="dots-horizontal" :type="checked ? 'is-white' : 'is-dark'"></b-icon>
      </crud-dropdown>
    </td>
  </tr>
</template>

<script>
  import Columns from './Columns';
  import CrudDropdown from './CrudDropdown';
  import { getAndSetContactList, getFirstItem } from "../utils";
  import store from "../store";

  export default {
    name: "contact-row",
    props: {
      contact: Object,
      checked: Boolean,
    },
    components: {
      Columns,
      CrudDropdown,
    },
    computed: {
      primaryEmail() {
        return this.getPrimary(this.contact.emails, 'email');
      },
      primaryPhoneNumber() {
        return this.getPrimary(this.contact.phone_numbers, 'number');
      },
      primaryAddress() {
        let address = this.getPrimary(this.contact.addresses, 'name');
        if (address.length >= 30) {
          address = address.slice(0, 30) + '...'
        }
        return address
      }
    },
    methods: {
      getPrimary(array, property) {
        if (array.length > 0) {
          return getFirstItem(array, item => item.primary)[property]
        } else {
          return '---'
        }
      },

      handleContactClick(event) {
        if (this.$refs.actions.$el.contains(event.target) || this.$refs.checkbox.contains(event.target)) {
          return
        }

        this.$emit('openDetails');
      }
    }
  }
</script>

<style lang="scss" scoped>
  .contact-item {
    -webkit-box-shadow: none;
    -moz-box-shadow: none;
    box-shadow: none;

    &:not(:last-child) {
      margin-bottom: 1.2rem;
    }

    .column {
      padding: 0.5rem;
    }
  }
</style>