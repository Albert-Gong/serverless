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
        neg {{ results[0] }}
      </div>
      <div>
        neu {{ results[1] }}
      </div>
      <div>
        pos {{ results[2] }}
      </div>
      <div>
        compound {{ results[3] }}
      </div>


      <div></div>
      <div></div>

    </div>
  </div>
</template>

<script>
import {computed, defineComponent, ref} from 'vue'
import {ObsClient} from "../../huaweiobs/index"

export default defineComponent({
  name: 'SentimentAnalysis',

  setup() {
    let sentence = ref("")
    let results = ref([])


    let analyzeSentiment = () => {
      let ak = 'VFQ6DYBAKATE373J1OSX'
      let sk = 'r97RMrH2xqEbYSSoDR43OEtMgAdSu6AmuPPCMiQg'
      let server = 'https://obs.cn-north-4.myhuaweicloud.com'

      let obsClient = new ObsClient({
        access_key_id: ak,
        secret_access_key: sk,
        server: server
      });

      obsClient.putObject({
        Bucket: 'serverless-ai-stage-0',
        Key: "sentiment_sentence.txt",
        Body: sentence.value
      }, function (err, result) {
        if (err) {
          console.error('Error-->' + err);
        } else {
          if (result.CommonMsg.Status < 300) {
            if (result.InterfaceResult) {
              console.log('Status-->' + result.CommonMsg.Status);
              console.log('RequestId-->' + result.CommonMsg.RequestId);

              function query() {
                obsClient.getObject({
                  Bucket: 'serverless-ai-stage-1',
                  Key: "sentiment_sentence.txt"
                }, function (err, result) {
                  if (err) {
                    console.error('Error-->' + err);
                  } else {
                    console.log('Status-->' + result.CommonMsg.Status);
                    if (result.CommonMsg.Status < 300 && result.InterfaceResult) {
                      let str_obj = result.InterfaceResult.Content
                      console.log(str_obj)
                      results.value = []
                      str_obj.slice(1, -1).split(",").forEach(e => {
                        let ele = e.slice(e.indexOf(":") + 1)
                        results.value.push(ele)
                      })
                      console.log(results)
                    }
                  }
                })
              }

              setTimeout(query, 1000)

            }
          } else {
            console.log('Status-->' + result.CommonMsg.Status);
            console.log('Code-->' + result.CommonMsg.Code);
            console.log('RequestId-->' + result.CommonMsg.RequestId);
          }
        }
      });
    }


    return {
      sentence,
      results,
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


