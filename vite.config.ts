import {ConfigEnv, UserConfigExport} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'

const pathResolve = (dir: string): any => {
    return resolve(__dirname, ".", dir)
}

const alias: Record<string, string> = {
    '@': pathResolve("src")
}

export default ({command}: ConfigEnv): UserConfigExport => {
    const prodMock = true;
    return {
        base: './',
        resolve: {
            alias
        },
        server: {
            host: 'localhost',
            port: 8090,
            open: true,
            proxy: {
                '/hw': {
                    target: 'https://a6112d413d5346b29a888dfc8bfb3a4e.apig.cn-north-4.huaweicloudapis.com',
                    changeOrigin: true,
                    ws: true,
                    rewrite: path => path.replace(/^\/hw/, '')
                }
            }
        },
        build: {
            rollupOptions: {
                output: {
                    manualChunks: {}
                }
            }
        },
        plugins: [
            vue(),
        ]
    };
}
