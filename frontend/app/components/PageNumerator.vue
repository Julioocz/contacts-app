<template>
  <div class="has-text-centered">
    <h6 class="title is-6">Page {{ currentPage }} of {{ totalPages }}</h6>
  </div>
</template>

<script>
  import store from "../store";
  import { PAGE_SIZE } from "../constants";

  export default {
    name: "page-numerator",
    data() {
      return {
        sharedState: store.state,
      }
    },

    computed: {
      currentPage() {

        if (this.sharedState.next) {
          const offset = parseInt(this.sharedState.next.match(/offset=(.+)/)[1]);
          console.log('OFFSETTTTTTT', offset);
          return offset / PAGE_SIZE;
        } else {
          return this.totalPages;
        }
      },

      totalPages() {
        return Math.ceil(this.sharedState.contactCount / PAGE_SIZE);
      },
    }
  }
</script>

<style scoped>

</style>