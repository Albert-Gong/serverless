/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="about">
    <h1>About page</h1>
    {{route.params}}
    <HelloWorld :msg="TJU"></HelloWorld>
  </div>
</template>

<script>
import {defineComponent, reactive} from 'vue'
import HelloWorld from "@/components/HelloWorld.vue";
import {useRoute} from "vue-router";

export default defineComponent({
  name: 'About',
  components: {HelloWorld},

  setup() {
    let route = useRoute()
    let state = reactive({
      count: 0,
    })
    let TJU = "1";
    // let query = route.params
    return {
      state,
      TJU,
      route

    }
  }
})
</script>

<style scoped lang="scss">

</style>


