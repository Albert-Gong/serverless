/**
* Created on 2022/4/24.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="login-container">
    <div class="logo-image">
    </div>
    <div class="row-container">
      <div class="prefix">
        AK
      </div>
      <div class="input-box">
        <el-input
            size="default"
            v-model="input_ak"
            placeholder="input access key"
        ></el-input>
      </div>
    </div>

    <div class="row-container">
      <div class="prefix">
        Sk
      </div>
      <div class="input-box">
        <el-input
            size="default"
            v-model="input_sk"
            type="password"
            placeholder="input secret key"
        ></el-input>
      </div>
    </div>

    <div class="row-container">
      <div class="prefix">
        Server
      </div>
      <div class="input-box">
        <el-input
            size="default"
            v-model="input_server"
            placeholder="input server name"
        ></el-input>
      </div>
    </div>

    <div class="button-group">
      <el-link type="success" class="button" @click="saveConfiguration">
        Save
      </el-link>
      <el-link type="warning" class="button" @click="resetConfiguration">
        Reset
      </el-link>
    </div>
    <el-button type="primary" size="default" class="serverless-button" @click="goToServerless">Serverless Center
    </el-button>
  </div>
</template>

<script>
import {defineComponent, ref, computed, onMounted} from 'vue'
import {useStore} from 'vuex';
import {useRouter} from "vue-router";
import {analyse_sentiment} from "../../apis/user";
import {ElMessage} from "element-plus";
// import Logo from "@/components/logo/Logo.vue";


export default defineComponent({
  name: 'LoginBox',
  components: {
    // Logo
  },
  setup() {
    let store = useStore();
    let router = useRouter();

    let ak = "", sk = "", server = ""
    onMounted(() => {
      ak = computed(() => store.getters['user/getAk'])
      sk = computed(() => store.getters['user/getSk'])
      server = computed(() => store.getters['user/getServer'])
      console.log(ak.value)
    })
    let input_ak = ref(ak)
    let input_sk = ref(sk)
    let input_server = ref(server)


    let saveConfiguration = () => {
      let data = {
        "input_ak": input_ak.value,
        "input_sk": input_sk.value,
        "input_server": input_server.value,
      }
      store.dispatch('user/configure', data).then(res => {
        if (res === 'OK') {
          ElMessage({
            message: 'Successfully finish the configuration',
            type: 'success',
          })
        }

      }).catch(e => {
        console.log(e)
      })

    }

    let resetConfiguration = () => {
      store.dispatch("user/reset").then(res => {
        if (res === 'OK') {
          ElMessage({
            message: 'Successfully reset the configuration',
            type: 'success',
          })
        }
      }).catch(err => {
        console.log(err)
      });
    }

    let goToServerless = () => {
      router.push({
        name: "serverlessCenter"
      })
    }

    return {
      input_ak,
      input_sk,
      input_server,
      name,
      saveConfiguration,
      resetConfiguration,
      goToServerless
    }
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

$imageURL: "../../assets/images/logo.png";

#login-container {
  margin: 0 auto;
  padding: 0px 20px;
  border-radius: 10px;
  align-self: center;
  width: 350px;
  height: 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: $container_color;

  .logo-image {
    //border-radius: 20px 20px 0 0;
    position: relative;
    width: 80%;
    height: 100px;
    background: url($imageURL) no-repeat center center;
    background-size: cover;
    display: flex;
    flex-flow: column-reverse;
  }

  .logo {
    height: 100px;
  }

  .prefix {
    width: 65px;
    margin-right: 5px;
    font-size: 16px;
    text-align: left;
  }

  .row-container {
    display: flex;
    align-items: center;
    width: 100%;

    .input-box {
      width: 250px;

      .el-input {
        width: 240px;
      }
    }

    & {
      margin-bottom: 10px;
    }
  }

  .serverless-button {
    width: 180px;
    border-radius: 20px;
  }

  .button-group {
    width: 100%;
    display: flex;
    justify-content: space-between;

    .el-button {
      width: 120px;
      height: 30px;
      font-size: 15px;

    }
  }

}

</style>


