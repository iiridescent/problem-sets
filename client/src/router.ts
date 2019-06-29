import Katex from 'katex';
import Vue, { ComponentOptions } from 'vue';
import Router from 'vue-router';

import Home from './views/Home.vue';
import Problems from './views/Problems.vue';

Vue.use(Router);

export const router: Router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/problems/:type',
            name: 'problems',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: Problems,
        },
    ],
});
