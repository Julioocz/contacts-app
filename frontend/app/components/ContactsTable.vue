<template>
  <div class="custom-table">
    <table class="table is-hoverable">
      <thead>
      <tr>
        <th>
          <b-checkbox :value="allChecked" @change.native="checkAll"></b-checkbox>
        </th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>
          <b-tooltip label="Primary Email">Email</b-tooltip>
        </th>
        <th>
          <b-tooltip label="Primary phone number">Phone number</b-tooltip>
        </th>
        <th>
          <b-tooltip label="Primary address">Address</b-tooltip>
        </th>
        <th>Birth date</th>
        <th>
          <page-changer></page-changer>
        </th>
      </tr>
      </thead>
      <tbody>
      <contact-row
        v-for="(contact, index) in sharedState.contacts"
        @checked="value => handleCheck(index, value)"
        :checked="isChecked(index)"
        :key="contact.id"
        :contact="contact"
        @openDetails="() => openContactDetails(index)"
        @deleteContact="() => deleteContact(index)"
        @editContact="() => editContact(index)">
      </contact-row>
      </tbody>
    </table>
  </div>
</template>

<script>
  import PageChanger from './PageChanger';
  import ContactRow from './ContactRow';
  import store from "../store";
  import updateRemoveDetailMixin from './mixins/updateRemoveDetailMixin';

  export default {
    name: "contacts-table",
    mixins: [updateRemoveDetailMixin],
    components: {
      PageChanger,
      ContactRow,
    },

    data() {
      return {
        sharedState: store.state,
      }
    },

    computed: {
      allChecked() {
        return Object.entries(this.sharedState.checkedContacts).filter(([key, value]) => !value).length === 0;
      }
    },

    watch: {
      'sharedState.checkedContacts'() {
        console.log('Change');
      }
    },

    methods: {
      handleCheck(index, value) {
        if (this.sharedState.checkedContacts[index] !== value) {
          store.setContactCheck(index, value);
        }
      },
      isChecked(index) {
        return !!this.sharedState.checkedContacts[index];
      },
      checkAll() {
        const check = !this.allChecked;
        Object.keys(this.sharedState.checkedContacts).forEach(key => store.setContactCheck(key, check));
      }
    }
  }
</script>

<style lang="scss">
  @import "../variables";

  .custom-tr {
    border-radius: 5px;
  }

  .custom-table {
    .table {
      border: none;
      border-collapse: separate;
      width: 100%;
    }

    tbody {
      tr {
        border-radius: 5px;
        border-width: 20px;
        cursor: pointer;
      }
    }

    td {
      border-color: $light !important;
      border-width: 0 0 10px;
    }

    .table-wrapper {
      margin-bottom: 0;
    }

    thead {
      background-color: $light;
      border: none;
    }

    th {
      border-width: 0 !important;
    }
  }
</style>