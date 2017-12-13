import { PAGE_SIZE } from "./constants";

const defaultCheckedRows = () => {
  const rows = {};
  Array.from(Array(PAGE_SIZE).keys()).forEach(n => rows[n] = false);
  return rows;
};

/**
 * Simple store for the shared state across the app
 */
export default {
  debug: true,
  state: {
    contacts: [],
    contactCount: null,
    loading: false,
    previous: null,
    next: null,
    allChecked: false,
    contactModalOpen: false,
    contactModalMode: 'detail',
    selectedContact: {},
    selectedContactIndex: null,
    initEndpoint: '',
    currentEndpoint: '',
    checkedContacts: defaultCheckedRows(),
  },

  _log(...log) {
    if (this.debug) console.log(...log);
  },

  setInitEndpoint(value) {
    this._log('Init endpoint state set to: ', value);
    this.state.initEndpoint = value;
  },

  setCurrentEndpoint(value) {
    this._log('Current endpoint state set to: ', value);
    this.state.currentEndpoint = value;
  },

  setContactCount(value) {
    this._log('Contact count set to: ', value);
    this.state.contactCount = value;
  },

  setContacts(value) {
    this._log('Contacts set with value: ', value);
    this.state.contacts = value;
  },

  setPrevious(value) {
    this._log('Previous set with value: ', value);
    this.state.previous = value
  },

  setNext(value) {
    this._log('Next set with value: ', value);
    this.state.next = value;
  },

  setContactCheck(index, value) {
    this._log(`Set row ${index} check value to ${value}`);
    this.state.checkedContacts[index] = value;
  },

  clearContactCheck() {
    this._log('Clearing contact check list');
    this.state.checkedContacts = defaultCheckedRows();
    this.state.allChecked = false;
  },

  setLoading(value) {
    this._log('Loading state set to: ', value);
    this.state.loading = value;
  },

  setContactModalOpen(value) {
    this._log('Contact modal open state set to: ', value);
    this.state.contactModalOpen = value;
  },
  setContactModalMode(value) {
    this._log('Contact modal mode state set to: ', value);
    this.state.contactModalMode = value;
  },

  setSelectedContact(value) {
   this._log('Selected contact state set to: ', value);
    this.state.selectedContact = value;
  },

  setSelectedContactIndex(value) {
    this._log('Selected contact index set to: ', value);
    this.state.selectedContactIndex = value;
  },

  setContactCount(value) {
    this._log('Contact count set to: ', value);
    this.state.contactCount = value;
  },
}