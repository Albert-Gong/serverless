/**
 * Created on 2022/4/22.
 * @author Zhihao Gong
 * @changeLogs
 */

import {ActionContext} from 'vuex'

export interface userState {
    token: string,
    ak: string,
    sk: string,
}

const state = (): userState => ({
    token: '',
    ak: 'VFQ6DYBAKATE373J1OSX',
    sk: 'r97RMrH2xqEbYSSoDR43OEtMgAdSu6AmuPPCMiQg',

})

// const token = computed(() => store.getters.getToken);
// getters
const getters = {
    getToken(state: userState) {
        return state.token
    },
    getAk(state: userState) {
        return state.ak
    },
    getSk(state: userState) {
        return state.sk
    }
}

// mutations
const mutations = {
    changeToken(state: userState, token: string) {
        state.token = token

    },
    changeAk(state: userState, ak: string) {
        state.ak = ak
    },
    changeSk(state: userState, sk: string) {
        state.sk = sk
    }
}

// actions
const actions = {
    login({commit, dispatch}: ActionContext<userState, userState>, params: any) {
        return new Promise((resolve, reject) => {
            // commit("changeToken", params.token)
            commit("changeAk", params.ak)
            commit("changeSk", params.sk)
            resolve("OK")
        })
    },

    loginOut({commit}: ActionContext<userState, userState>) {
        return new Promise((resolve, reject) => {
            commit("changeToken", "")
            commit("changeAk", "")
            commit("changeSk", "")
            resolve("OK")
        })
    }
}

export default {
    namespaced: true,
    state,
    actions,
    getters,
    mutations
}
