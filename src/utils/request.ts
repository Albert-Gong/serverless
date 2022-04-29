/**
 * Created on 2022/4/24.
 * @author Zhihao Gong
 * @changeLogs
 */

import axios, {AxiosError, AxiosRequestConfig, AxiosResponse, AxiosInstance} from 'axios'
// @ts-ignore
import store from '@/store/index'
import {ElMessage} from 'element-plus'


const service: AxiosInstance = axios.create({
    baseURL: '/hw',
    timeout: 10000,
})


// 请求前统一处理
service.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        return config
    },
    (error: AxiosError) => {
        return Promise.reject(error)
    }
)

// 拿到响应后统一处理
service.interceptors.response.use(
    (response: AxiosResponse) => {
        const res = response.data
        if (res.resultCode === 200) {
            return res
        } else {
            showError(res)
            return Promise.reject(res)
        }
    },
    (error: AxiosError) => {
        console.log('error', error)
        const badMessage: any = error.message || error
        const code = parseInt(badMessage.toString().replace('Error: Request failed with status code ', ''))
        showError({code, message: badMessage})
        return Promise.reject(error)
    }
)

function showError(error: any) {
    if (error.code === 403) {
        store.dispatch('user/reset').then((r:any) => console.log(r))
    } else {
        ElMessage({
            message: error.msg || error.message || '服务异常',
            type: 'error',
            duration: 1.5 * 1000
        })
    }

}

export default service
