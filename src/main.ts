import {createApp} from 'vue'
// @ts-ignore
import ElementPlus from "element-plus"
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router/index'
import store from "./store"
import '@/styles/index.scss';
import '@/styles/common.scss';
import * as ELIcons from '@element-plus/icons-vue'

const app = createApp(App)
for (let iconName in ELIcons) {
    // @ts-ignore
    app.component(iconName, ELIcons[iconName])
}
app.use(ElementPlus, {size: 'small', zIndex: 3000})
app.use(router)
app.use(store)
app.mount('#app')

