/**
 * Created on 2022/4/22.
 * @author Zhihao Gong
 * @changeLogs
 */

import {createStore, createLogger} from 'vuex'
// @ts-ignore
import {userState} from "@/store/modules/user";

const files = import.meta.globEager('./modules/*.ts')


// commit 和 dispatch 是调用 mutation 的两种方法
// commit 同步操作
// dispatch 异步操作

export interface RootState {
    user: userState,
}

let modules: any = {}
Object.keys(files).forEach((c: string) => {
    const module = files[c].default
    const moduleName: string = c.replace(/^\.\/(.*)\/(.*)\.\w+$/, '$2')
    modules[moduleName] = module
})


export default createStore<RootState>({
    modules: {
        ...modules
    },
})
