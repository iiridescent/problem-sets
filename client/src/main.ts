import Vue, { CreateElement, VNode } from 'vue';

import App from './App.vue';
// tslint:disable-next-line:no-import-side-effect
import './registerServiceWorker';
import { router } from './router';
import { store } from './store';

Vue.config.productionTip = false;
// @ts-ignore
import VueClipboard from 'vue-clipboard2'

Vue.use(VueClipboard)

new Vue({
  router,
  store,
  render: (createElement: CreateElement): VNode => createElement(App),
}).$mount('#app');
