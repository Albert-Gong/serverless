/**
* Created on 2022/4/22.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="sentiment-analysis-container">
    123
  </div>
</template>

<script>
import {defineComponent, reactive} from 'vue'

export default defineComponent({
  name: 'SentimentAnalysis',
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
@import "@/styles/common";
#sentiment-analysis-container{
  background-color: $container_color;

}
</style>


