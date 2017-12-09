import Vue from 'vue';

import Buefy from 'buefy';
import './app/bulma-custom.scss'

import App from './app/App';

Vue.use(Buefy);

document.addEventListener('DOMContentLoaded', () => new Vue({
  el: '#contact-app',
  render(c) {
    return c(App, { props: { endpoint: this.$el.dataset.endpoint } })
  }
}));
