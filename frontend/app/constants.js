const TYPE_HOME = 'home';
const TYPE_WORK = 'work';
const TYPE_MOVIL = 'movil';
const TYPE_PERSONAL = 'personal';
const TYPE_OTHER = 'other';

export const PERSONAL_INFO_TYPES = {
  email: [TYPE_PERSONAL, TYPE_HOME, TYPE_WORK, TYPE_OTHER],
  address: [TYPE_HOME, TYPE_WORK, TYPE_OTHER],
  phoneNumber: [TYPE_MOVIL, TYPE_HOME, TYPE_WORK, TYPE_OTHER]
};
