<template>
  <b-modal :active="open">
    <contact-detail v-if="editMode"></contact-detail>
    <contact-edit v-else></contact-edit>
  </b-modal>
</template>

<script>
  import ContactDetail from './ContactDetail';
  import ContactEdit from './ContactEdit';

  export default {
    name: "contact-modal",
    components: { ContactDetail, ContactEdit, },
    props: {
      contact: Object,
      editMode: Boolean,
      open: Boolean,
    }
  }
</script>

<style scoped>

</style>