/**
 * Created on 2022/4/24.
 * @author Zhihao Gong
 * @changeLogs
 */

import axios, {AxiosError, AxiosRequestConfig, AxiosResponse, AxiosInstance} from 'axios'
import store from '@/store/index'
import {ElMessage} from 'element-plus'
// const baseURL: any = import.meta.env.VITE_BASE_URL

// axios.defaults.withCredentials = true


const service: AxiosInstance = axios.create({
    baseURL: '/cj',
    timeout: 1000,

})


// 请求前的统一处理
service.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        return config
    },
    (error: AxiosError) => {
        console.log(error) // for debug
        return Promise.reject(error)
    }
)

service.interceptors.response.use(
    (response: AxiosResponse) => {
        console.log('success', response)
        // console.log('headers', response.headers)
        const res = response.data

        if (res.code === 0) {
            return res
        } else {
            showError(res)
            return Promise.reject(res)
        }
    },
    (error: AxiosError) => {
        console.log('error', error) // for debug
        const badMessage: any = error.message || error
        const code = parseInt(badMessage.toString().replace('Error: Request failed with status code ', ''))
        showError({code, message: badMessage})
        return Promise.reject(error)
    }
)

// 错误处理
function showError(error: any) {
    // token过期，清除本地数据，并跳转至登录页面
    if (error.code === 403) {
        // to re-login
        store.dispatch('user/loginOut').then(r => console.log(r))
    } else {
        ElMessage({
            message: error.msg || error.message || '服务异常',
            type: 'error',
            duration: 1.5 * 1000
        })
    }

}

export default service
