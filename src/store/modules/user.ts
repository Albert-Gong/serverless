/**
 * Created on 2022/4/22.
 * @author Zhihao Gong
 * @changeLogs
 */

import {ActionContext} from 'vuex'

export interface userState {
    ak: string,
    sk: string,
    server: string,
}

// let ak = ''
// let sk = ''
// let server = ''
const state = (): userState => <userState>({
    ak: 'VFQ6DYBAKATE373J1OSX',
    sk: 'r97RMrH2xqEbYSSoDR43OEtMgAdSu6AmuPPCMiQg',
    server: 'https://obs.cn-north-4.myhuaweicloud.com',
})

// const token = computed(() => store.getters.getToken);
// getters
const getters = {
    getAk(state: userState) {
        return state.ak
    },
    getSk(state: userState) {
        return state.sk
    },
    getServer(state: userState) {
        return state.server
    },
}

// mutations
const mutations = {

    changeAk(state: userState, ak: string) {
        state.ak = ak
    },
    changeSk(state: userState, sk: string) {
        state.sk = sk
    },
    changeServer(state: userState, server: string) {
        state.server = server
    },

}

// actions
const actions = {
    configure({commit, dispatch}: ActionContext<userState, userState>, params: any) {
        return new Promise((resolve, reject) => {
            commit("changeAk", params.input_ak)
            commit("changeSk", params.input_sk)
            commit("changeServer", params.input_server)
            resolve("OK")
        })
    },
    reset({commit, dispatch}: ActionContext<userState, userState>) {
        return new Promise((resolve, reject) => {
            commit("changeAk", "")
            commit("changeSk", "")
            commit("changeServer", "")
            resolve("OK")
        })
    },
}

export default {
    namespaced: true,
    state,
    actions,
    getters,
    mutations
}
