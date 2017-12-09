<template>
  <div class="app-body">
    <div class="box app-container container is-primary">
      <top-bar></top-bar>
      <contacts-table></contacts-table>
    </div>
  </div>
</template>

<script>
  import ContactsTable from './components/ContactsTable';
  import Segment from './components/Segment';
  import TopBar from './components/TopBar';

  export default {
    name: "app",
    components: {
      ContactsTable,
      Segment,
      TopBar,
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

  .app-container {
    min-height: 80vh;
    background-color: $light;
    padding: 5vh;
  }
</style>