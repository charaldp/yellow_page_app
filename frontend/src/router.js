import {createWebHistory, createRouter} from "vue-router";

import ContactsList from "./components/ContactsList.vue";

const routes = [
    {
        path: '/contact',
        component: ContactsList
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router;