/**
 * Created on 2022/4/22.
 * @author Zhihao Gong
 * @changeLogs
 */

import {ActionContext} from 'vuex'
import {analyse_sentiment, requestToken} from "../../apis/user";
import {token_data} from "@/utils/basic"

export interface userState {
    token: string,
    ak: string,
    sk: string,
    server: string,
    user: string,
    name: string,
    pw: string
}

const state = (): userState => <userState>({
    token: '',
    ak: '',
    sk: '',
    server: '',
    user: '',
    name: '',
    pw: ''
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
    },
    getServer(state: userState) {
        return state.server
    },
    getUser(state: userState) {
        return state.user
    },
    getName(state: userState) {
        return state.name
    },
    getPw(state: userState) {
        return state.pw
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
    },
    changeServer(state: userState, server: string) {
        state.server = server
    },
    changeUser(state: userState, user: string) {
        state.user = user
    },
    changeName(state: userState, name: string) {
        state.name = name
    },
    changePw(state: userState, pw: string) {
        state.pw = pw
    }
}

// actions
const actions = {
    configure({commit, dispatch}: ActionContext<userState, userState>, params: any) {
        return new Promise((resolve, reject) => {
            commit("changeAk", params.input_ak)
            commit("changeSk", params.input_sk)
            commit("changeServer", params.input_server)
            commit("changeToken", params.input_token)
            // commit("changeName", params.input_name)
            // commit("changePw", params.input_pw)
            resolve("OK")
        })
    },
    reset({commit, dispatch}: ActionContext<userState, userState>) {
        return new Promise((resolve, reject) => {
            commit("changeAk", "")
            commit("changeSk", "")
            commit("changeServer", "")
            commit("changeToken", "")
            // commit("changeName", "")
            // commit("changePw", "")
            resolve("OK")
        })
    },
    // requestToken({commit, dispatch}: ActionContext<userState, userState>, params:any) {
    //     return new Promise((resolve, reject) => {
    //
    //         token_data["auth"]["identity"]["password"]["user"]["domain"]["name"] = params["input_user"]
    //         token_data["auth"]["identity"]["password"]["user"]["name"] = params["input_name"]
    //         token_data["auth"]["identity"]["password"]["user"]["password"] = params["input_pw"]
    //         analyse_sentiment().then(res => {
    //             console.log(res)
    //         })
    //     })
    // },
}

export default {
    namespaced: true,
    state,
    actions,
    getters,
    mutations
}
