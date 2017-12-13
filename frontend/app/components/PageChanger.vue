<template>
  <div>
    <button class="button is-small" @click="previousPage" :disabled="!sharedState.previous">
      <b-icon icon="menu-left" type="is-dark"></b-icon>
    </button>
    <button class="button is-small" @click="nextPage" :disabled="!sharedState.next">
      <b-icon icon="menu-right" type="is-dark"></b-icon>
    </button>
  </div>
</template>

<script>
  import axios from 'axios';
  import store from '../store';
  import { handleContactResponse } from '../utils';

  export default {
    name: "page-changer",

    data() {
      return {
        sharedState: store.state
      }
    },

    methods: {
      getContacts(endpoint) {
        store.setLoading(true);
        axios.get(endpoint)
          .then(handleContactResponse)
          .then(() => store.setCurrentEndpoint(endpoint))
          .then(() => store.setLoading(false))
          .catch(this.handleError)
      },

      nextPage() {
        if (this.sharedState.next) this.getContacts(this.sharedState.next);
      },
      previousPage() {
        if (this.sharedState.previous) this.getContacts(this.sharedState.previous);
      },
      handleError() {
        this.$toast.open({
          message: 'An error ocurred processing the request for the new page!',
          type: 'is-danger'
        });

      }
    }
  }

</script>

<style scoped>

</style>