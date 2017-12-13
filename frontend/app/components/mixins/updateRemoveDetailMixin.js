import axios from 'axios';

import store from '../../store';
import { getAndSetContactList } from "../../utils";

/**
 * Mixin to add methods to update, remove and see the details of a contact
 */
export default {
  methods: {
    openContactDetails(contactIndex) {
      store.setSelectedContact(Object.assign({}, store.state.contacts[contactIndex]));
      store.setSelectedContactIndex(contactIndex);
      store.setContactModalMode('detail');
      store.setContactModalOpen(true);
    },

    deleteContact(contactIndex) {
      store.setLoading(true);
      axios
        .delete(store.state.contacts[contactIndex].url)
        .then(getAndSetContactList)
        .then(() => {
          store.setContactModalOpen(false);
          store.setLoading(false);
          this.$toast.open({
            message: 'Contact removed successfully',
            type: 'is-success',
          })
        })

    },

    editContact(contactIndex) {
      store.setSelectedContact(Object.assign({}, store.state.contacts[contactIndex]));
      store.setSelectedContactIndex(contactIndex);
      store.setContactModalMode('edit');
      store.setContactModalOpen(true);
    }
  }
}