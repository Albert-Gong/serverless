/**
 * Created on 2022/4/24.
 * @author Zhihao Gong
 * @changeLogs
 */

import request from '@/utils/request';
// @ts-ignore
import Qs from "qs";

/** request token **/
export function analyse_sentiment(sentence) {
    return request({
        url: 'https://f1cbbbb3abf244d3b7dbe955451b5c7c.apig.cn-north-4.huaweicloudapis.com/sentiment_analysis',
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
