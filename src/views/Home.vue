/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="home">
    <h1>Home Page</h1>
    <el-button @click="goAbout"> go about</el-button>
  </div>
</template>

<script>
import {defineComponent, reactive} from 'vue'
import {useRouter} from "vue-router";

export default defineComponent({
  name: 'Home',
  props: {
    msg: {
      type: String,
      default: ''
    }
  },
  setup() {
    let router = useRouter()

    let state = reactive({
      count: 0,
    })

    let goAbout = () => {
      router.push({
        name: "about",
        params: {
          "name": "gzh"
        }

      })

    }

    return {
      state,
      goAbout
    }
  }
})
</script>

<style scoped lang="scss">

</style>


