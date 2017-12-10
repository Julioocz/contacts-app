<template>
  <div class="app-body">
    <div class="box box-light app-container container is-primary">
      <top-bar></top-bar>
      <contacts-table></contacts-table>
    </div>

    <contact-modal :open="true"></contact-modal>
  </div>
</template>

<script>
  import axios from 'axios';

  import ContactsTable from './components/ContactsTable';
  import Segment from './components/Segment';
  import TopBar from './components/TopBar';
  import ContactModal from './components/ContactModal';

  export default {
    name: "app",
    components: {
      ContactsTable,
      Segment,
      TopBar,
      ContactModal,
    },

    props: {
      /**
       * Contact list endpoint
       */
      endpoint: String,
    },

    data() {
      return {
        loading: true,
        contacts: [],
        error: false,
      }
    },

    mounted() {
      axios.get(this.endpoint)
        .then()
        .catch(this.handleError)
    },

    methods: {
      handleError() {
        this.error = true;
      }
    }
  }
</script>

<style lang="scss">
  @import "variables";
  @import "utils";

  .app-body {
    background: linear-gradient(to top right, $secondary, $primary);
    padding-top: 10vh;
    padding-bottom: 10vh;
  }

  .box-light {
    background-color: $light;
  }

  .app-container {
    min-height: 80vh;
    padding: 5vh;
  }
</style>