<template>
  <div class="app-body">
    <div class="box box-light app-container container is-primary">
      <top-bar :count="count" @contactsDeleted="getContacts"></top-bar>
      <contacts-table></contacts-table>
      <page-numerator></page-numerator>
    </div>

    <contact-modal></contact-modal>
    <b-loading :active="sharedState.loading"></b-loading>
  </div>
</template>

<script>
  import axios from 'axios';

  import store from './store';
  import ContactsTable from './components/ContactsTable';
  import TopBar from './components/TopBar';
  import ContactModal from './components/ContactModal';
  import PageNumerator from './components/PageNumerator';
  import { getAndSetContactList } from "./utils";


  export default {
    name: "app",
    components: {
      ContactsTable,
      TopBar,
      ContactModal,
      PageNumerator
    },

    props: {
      /**
       * Contact list endpoint
       */
      endpoint: String,
    },

    data() {
      return {
        sharedState: store.state,
        error: false,
        count: null,
      }
    },

    mounted() {
      store.setInitEndpoint(this.endpoint);
      store.setCurrentEndpoint(this.endpoint);
      this.getContacts();
    },

    methods: {
      getContacts() {
        store.setLoading(true);
        getAndSetContactList()
          .then(() => store.setLoading(false))
          .catch(this.handleError);
      },

      handleError(error) {
        console.error(error);
        this.error = true;
      },
    }
  }
</script>

<style lang="scss">
  @import "variables";
  @import "utils";

  .app-body {
    background: linear-gradient(to top right, $secondary, $primary);
    padding-top: 5vh;
    padding-bottom: 10vh;
    min-height: 100vh;
  }

  .box-light {
    background-color: $light;
  }

  .app-container {
    min-height: 90vh;
    padding: 5vh;
  }
</style>