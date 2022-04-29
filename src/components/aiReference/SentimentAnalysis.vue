/**
* Created on 2022/4/22.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="sentiment-analysis-container">
    <div class="content-container">
      <el-input v-model="sentence" type="textarea" placeholder="Input some test here"
                :autosize="{minRows: 12, maxRows: 25}" :style="{width: '100%'}"></el-input>
      <el-button type="primary" @click="analyzeSentiment">Analyze sentiment</el-button>
    </div>
    <div class="sentiment-result-container">

      <div>
        neg {{ neg}}
      </div>
      <div>
        neu {{ neu}}
      </div>
      <div>
        pos {{ pos }}
      </div>
      <div>
        compound {{ compound}}
      </div>
      <div></div>
      <div></div>
    </div>
  </div>
</template>

<script>
import {computed, defineComponent, ref} from 'vue'
import {ObsClient} from "../../huaweiobs/index"
import {analyse_sentiment} from "../../apis/user";

export default defineComponent({
  name: 'SentimentAnalysis',

  setup() {

    let sentence = ref("")
    let neg = ref("0"), neu = ref("0"), pos = ref("0"), compound = ref("0")

    let analyzeSentiment = () => {
      analyse_sentiment(sentence.value).then(res=>JSON.parse(res.data)).then(data=>{
        neg.value = data['neg']
        neu.value = data['neu']
        pos.value = data['pos']
        compound.value = data['compound']
      })
    }


    return {
      sentence,
      pos,
      neu,
      neg,
      compound,
      analyzeSentiment
    }
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

#sentiment-analysis-container {
  display: flex;
  background-color: $container_color;
  padding: 20px;
  border-radius: 20px;

  .content-container {
    flex: 1 0 250px;
    display: flex;
    flex-direction: column;

    .el-button {
      margin-top: 20px;
      width: 120px;
    }
  }

  .sentiment-result-container {
    flex: 0 0 250px;
  }

}
</style>


