/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="preprocess-detail-container">
    <div class="detail-des-container">
      <h3 class="api-name">
        {{ detail.api_name }}
      </h3>
      <p class="api-des">
        {{ detail.api_des }}
      </p>
    </div>
    <div class="upload-download-container">
      <div class="upload-container">
        <div class="caption">Please upload a file</div>
        <el-upload
            action=""
            class="uploader"
            :limit="1"
            :on-exceed="handleExceed"
            :auto-upload="false"
            :file-list="file_list"
            @submit="submitUpload"
        >
          <template #trigger>
            <el-button type="primary">select file</el-button>
          </template>
          <el-button class="ml-3" type="success" @click="submitUpload">
            upload to server
          </el-button>
          <template #tip>
            <div class="el-upload__tip text-red">
              limit 1 file, new file will cover the old file
            </div>
          </template>
        </el-upload>
        <div class="link-container">
          <el-link :href="dynamic_download_url" rel="external nofollow" class="link">download data</el-link>

        </div>

      </div>

      <div class="content-container">
        <el-input v-model="res_text" type="textarea" placeholder="Waiting an answer"
                  :autosize="{minRows: 12, maxRows: 25}" :style="{width: '100%'}"></el-input>
      </div>
    </div>

  </div>
</template>

<script lang="ts">
import {defineComponent, onMounted, ref, computed} from 'vue'
import {useRoute} from "vue-router";
import type {UploadInstance, UploadProps, UploadRawFile} from 'element-plus'
import {ElMessage} from 'element-plus'
import {ObsClient} from "../../huaweiobs/index"
import {useStore} from "vuex"
import {preprocess_apis} from "../../enums/preprocess";


export default defineComponent({
  name: 'PreprocessDetail',
  setup() {
    let store = useStore();
    let route = useRoute();
    let p_id = ref(0);
    let detail = ref({});

    let res_text = ref("");
    let dynamic_download_url = ref("");


    onMounted(() => {
      let current_path = route.path;
      p_id.value = Number(current_path.split("/").pop())
      detail.value = preprocess_apis.filter((e) => e.api_id == p_id.value)[0]
    })


    let file_list = ref<UploadUserFile[]>([])

    const handleExceed: UploadProps['onExceed'] = (files, uploadFiles) => {
      ElMessage.warning(
          `The limit is 1, you selected ${files.length} files this time, add up to ${
              files.length + uploadFiles.length
          } totally`
      )
    }


    const submitUpload = () => {
      if (file_list.value.length > 0) {
        let file = file_list.value[0]
        console.log("File:", file.name)
        let reader = new FileReader()
        reader.readAsText(file.raw)
        reader.onload = (event: any) => {
          let file_content = event.target.result


          let ak = 'VFQ6DYBAKATE373J1OSX'
          let sk = 'r97RMrH2xqEbYSSoDR43OEtMgAdSu6AmuPPCMiQg'
          let server = 'https://obs.cn-north-4.myhuaweicloud.com'


          let obsClient = new ObsClient({
            access_key_id: ak,
            secret_access_key: sk,
            server: server
          });

          obsClient.putObject({
            Bucket: 'serverless-preprocess-stage-0',
            Key: file.name,
            Body: file_content
          }, function (err, result) {
            if (err) {
              console.error('Error-->' + err);
            } else {
              if (result.CommonMsg.Status < 300) {
                if (result.InterfaceResult) {
                  console.log('Status-->' + result.CommonMsg.Status);
                  console.log('RequestId-->' + result.CommonMsg.RequestId);
                  (() => {
                    obsClient.getObject({
                      Bucket: 'serverless-preprocess-stage-1',
                      Key: file.name,
                    }, function (err, result) {
                      if (err) {
                        console.error('Error-->' + err);
                      } else {
                        console.log('Status-->' + result.CommonMsg.Status);
                        if (result.CommonMsg.Status < 300 && result.InterfaceResult) {
                          res_text.value = result.InterfaceResult.Content

                        }
                      }
                    })
                  })();
                  (() => {
                    obsClient.getObject({
                      Bucket: 'serverless-preprocess-stage-1',
                      Key: file.name,
                      SaveByType: 'file'
                    }, function (err, result) {
                      if (err) {
                        console.error('Error-->' + err);
                      } else {
                        console.log('Status-->' + result.CommonMsg.Status);
                        if (result.CommonMsg.Status < 300 && result.InterfaceResult) {
                          // console.log('Download Path:');
                          dynamic_download_url.value = result.InterfaceResult.Content.SignedUrl
                          // console.log();
                        }
                      }
                    })
                  })()

                }
              } else {
                console.log('Status-->' + result.CommonMsg.Status);
                console.log('Code-->' + result.CommonMsg.Code);
                console.log('RequestId-->' + result.CommonMsg.RequestId);
              }
            }
          });
        }
      }
    }

    return {
      p_id,
      file_list,
      res_text,
      detail,
      dynamic_download_url,
      handleExceed,
      submitUpload,
    }
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

#preprocess-detail-container {
  min-height: 400px;
  background-color: $container_color;
  border-radius: 10px;
  padding: 10px 20px;

  .detail-des-container {
    display: flex;
    flex-direction: column;

    .api-name, .api-des {
      margin: 0px;
      text-align: left;
    }

    .api-des {
      height: 36px;
      font-size: 16px;
      line-height: 16px;
      color: grey;
      margin-bottom: 10px;
    }


  }

  .upload-download-container {
    display: flex;
    flex-direction: row;
    min-height: 200px;

    .upload-container {
      flex: 0 1 250px;
      display: flex;
      flex-direction: column;
      align-items: left;

      .caption {
        text-align: left;
        margin: 0;
      }

      .uploader {
        width: 100%;
        margin-top: 10px;
        display: flex;
        flex-direction: column;
        align-items: baseline;


        button {
          width: 110px;
          height: 28px;
          font-size: 14px;

          &:nth-child(2) {
            margin-top: 20px;
          }
        }
      }

      .link-container {
        display: flex;
        flex-display: row;
        text-align: left;
        //&:hover{
        //  cursor: pointer;
        //}
      }
    }

    .content-container {
      flex: 1 1 300px;
    }
  }


}
</style>


