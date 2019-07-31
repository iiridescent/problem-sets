import Vue from 'vue';
import Router from 'vue-router';

import Home from '@/views/Home.vue';
import Problems from '@/views/Problems.vue';
import ManageStatic from "@/views/ManageStatic.vue";
import CreateStaticSet from "@/views/CreateStaticSet.vue";

Vue.use(Router);

export const router: Router = new Router({
    mode: "history",
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
            component: Problems,
        },
        {
            path: '/manage/static',
            name: 'manage-static',
            component: ManageStatic,
            children: [
                {
                    path: 'set',
                    redirect: 'set/create'
                },
                {
                    path: 'set/create',
                    name: 'create-set',
                    component: CreateStaticSet
                },
                {
                    path: 'set/edit',
                    name: 'edit-set',
                    component: Home
                }
            ]
        }
    ],
});
