/**
* Created on 2022/4/22.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="ai-reference-detail-container">
    hello
  </div>
</template>

<script>
import {defineComponent, reactive} from 'vue'

export default defineComponent({
  name: '',
  props: {
    msg: {
      type: String,
      default: ''
    }
  },
  setup() {
    let state = reactive({
      count: 0,
    })
    return {
      state,
    }
  }
})
</script>

<style scoped lang="scss">

</style>


