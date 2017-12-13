<template>
  <b-modal :active.sync="modalActive" @cancel="handleModalCancel">
    <contact-detail v-if="sharedState.contactModalMode === 'detail'"></contact-detail>
    <contact-edit v-else></contact-edit>
  </b-modal>
</template>

<script>
  import ContactDetail from './ContactDetail';
  import ContactEdit from './ContactEdit';
  import store from "../store";

  export default {
    name: "contact-modal",
    components: { ContactDetail, ContactEdit, },
    props: {
      contact: Object,
      editMode: Boolean,
      open: Boolean,
    },

    data() {
      return {
        sharedState: store.state,
      }
    },

    computed: {
      modalActive: {
        get() {
          return this.sharedState.contactModalOpen;
        },
        set(value) {
          store.setContactModalOpen(value)
        }
      }
    },

    methods: {
      handleModalCancel() {
        console.log('cancel');
        store.setContactModalOpen(false);
      }
    }
  }
</script>

<style scoped>

</style>