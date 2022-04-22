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
            // proxy: {
            //     '/cj': {
            //         target: 'http://43.138.10.182:8081/api',
            //         changeOrigin: true,
            //         ws: true,
            //         rewrite: path => path.replace(/^\/cj/, '')
            //     }
            // }
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
