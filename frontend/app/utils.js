/**
 * Returns the first item in the provided array that the provided evaluator returns true. If no item return
 * True null is returned.
 */
import axios from 'axios';
import store from "./store";
import { CONTACT_INFO_VALUE_PROPERTY_MAP, PERSONAL_INFO_TYPES } from "./constants";

export const getFirstItem = (array, evaluator) => {
  for (let item of array) {
    if (evaluator(item)) return item;
  }

  return null
};

export const handleContactResponse = (response) => {
  const { data } = response;
  store.setContacts(data.results);
  store.setNext(data.next);
  store.setPrevious(data.previous);
  store.setContactCount(data.count);
};

export const getAndSetContactList = () => (
    axios.get(store.state.currentEndpoint)
      .then(handleContactResponse)
  );


export const emptyContactInfo = (type, primary) => {
  const valueProperty = CONTACT_INFO_VALUE_PROPERTY_MAP[type];
  const infoType = PERSONAL_INFO_TYPES[type][0];
  return {
    primary,
    [valueProperty]: null,
    info_type: infoType,
  }
};