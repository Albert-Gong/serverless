/**
 * Created on 2022/4/21.
 * @author Zhihao Gong
 * @changeLogs
 */
// @ts-ignore
import {createRouter, createWebHistory, RouteRecordRaw} from "vue-router";
import serverlessCenter from "@/views/serverlessCenter/ServerlessCenter.vue";

const routes: Array<RouteRecordRaw> = [
    {
        path: '/:currentPath(.*)*', // the router is not matched
        redirect: (_) => {
            return {path: '/serverlessCenter'}
        },
    },
    {
        path: '',
        redirect: (_) => {
            return {path: '/serverlessCenter'}
        },
    },
    {
        path: "/",
        redirect: "/serverlessCenter",
    },
    {
        path: "/serverlessCenter",
        name: "serverlessCenter",
        component: serverlessCenter,
        children: [
            {
                path: "preprocess",
                name: "preprocess",
                component: () => import("@/views/preprocess/Preprocess.vue"),
                children: [
                    {
                        path: "preprocessDetail/:id",
                        name: "preprocessDetail",
                        component: () => import("@/components/preprocess/PreprocessDetail.vue")
                    }
                ],
            },
            {
                path: "aiReference",
                name: "aiReference",
                component: () => import("@/views/aiReference/AIReference.vue"),
                children: [
                    {
                        path: "sentimentAnalysis",
                        name: "sentimentAnalysis",
                        component: () => import("@/components/aiReference/SentimentAnalysis.vue")
                    }
                ]
            },
            {
                path: "pipeline",
                name: "pipeline",
                component: () => import("@/views/pipeline/Pipeline.vue")
            },
        ]
    },

];

const history = createWebHistory()
const router = createRouter({
    history,
    routes
})
export default router
