/**
 * Created on 2022/4/24.
 * @author Zhihao Gong
 * @changeLogs
 */

// @ts-ignore
import request from '@/utils/request';
// @ts-ignore
import Qs from "qs";

/** test **/
export function test(data: object) {
    return request({
        url: '/sentiment_analysis',
        method: 'post',
        data: Qs.stringify(data)
    })
}

/** huawei_func **/
export function huawei_func(data: object) {
    return request({
        url: '/preprocess_apig',
        method: 'post',
        data: Qs.stringify(data)
    })
}

/** analyse_sentiment **/
export function analyse_sentiment(sentence: string) {
    return request({
        url: 'sentiment_analysis',
        method: 'post',
        params: {
            "sentence": sentence,
        }
    })
}

/** register **/
export function register(data: object) {
    return request({
        url: 'auth/register',
        method: 'post',
        data: Qs.stringify(data)
    })
}

/** login **/
export function login(data: object) {
    return request({
            url: 'auth/login',
            method: 'post',
            data: Qs.stringify(data),
        }
    )
}

/** modify info **/
export function modifyInfo() {
    return request({
            url: 'user/info',
            method: 'put',
            data: Qs.stringify({password: 2}),
        }
    )
}


// getInfo
export function getUserInfo(data: object) {
    return request({
        url: '/user/info',
        method: 'post',
        // baseURL: '/mock',
        data
    })
}

/** 退出登录Api */
export function loginOut() {
    return request({
        url: '/user/out',
        method: 'post',
        // baseURL: '/mock'
    })
}

/** 获取登录后需要展示的菜单 */
export function getMenuApi() {
    return request({
        url: '/menu/list',
        method: 'post',
    })
}
