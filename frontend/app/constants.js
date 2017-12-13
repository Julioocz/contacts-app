export const TYPE_HOME = 'home';
export const TYPE_WORK = 'work';
export const TYPE_MOVIL = 'movil';
export const TYPE_PERSONAL = 'personal';
export const TYPE_OTHER = 'other';

export const PERSONAL_INFO_TYPES = {
  email: [TYPE_PERSONAL, TYPE_HOME, TYPE_WORK, TYPE_OTHER],
  address: [TYPE_HOME, TYPE_WORK, TYPE_OTHER],
  phoneNumber: [TYPE_MOVIL, TYPE_HOME, TYPE_WORK, TYPE_OTHER, TYPE_PERSONAL]
};

export const PAGE_SIZE = 10;

export const CONTACT_HEADER_MAPPING = {
  email: 'Emails:',
  phoneNumber: 'Phone Numbers',
  address: 'Addresses'
};

export const CONTACT_INFO_VALUE_PROPERTY_MAP = {
  email: 'email',
  phoneNumber: 'number',
  address: 'name',
};