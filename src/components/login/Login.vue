/**
* Created on 2022/4/24.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="login-container">
    <div class="logo-image">
    </div>
    <!--    <Logo></Logo>-->

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

    <div class="row-container">
      <div class="prefix">
        Token
      </div>
      <div class="input-box">
        <el-input
            size="default"
            v-model="input_token"
            placeholder="input secret key"
        ></el-input>
      </div>
    </div>


    {{ name }}
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
import {defineComponent, ref, computed} from 'vue'
import {useStore} from 'vuex';
import {useRouter} from "vue-router";
import {analyse_sentiment} from "../../apis/user";
// import Logo from "@/components/logo/Logo.vue";


export default defineComponent({
  name: 'LoginBox',
  components: {
    // Logo
  },
  setup() {

    let store = useStore();
    let router = useRouter();

    let input_ak = ref("")
    let input_sk = ref("")
    let input_server = ref("")
    let input_token = ref("")

    const name = computed(() => store.getters['user/getName'])

    let saveConfiguration = () => {
      let data = {
        "input_ak": input_ak.value,
        "input_sk": input_sk.value,
        "input_server": input_server.value,
        "input_token": input_token.value,
      }
      store.dispatch("user/configure", data).then(res => {
        console.log("ok", data)
        analyse_sentiment("I am superman").then(res => {
          console.log(res)
        })

        // store.dispatch('user/requestToken', data).then(res=>{
        //   console.log(res)
        // })
      }).catch(err => console.log(err));
    }

    let resetConfiguration = () => {
      store.dispatch("user/reset").then(res => {
        console.log(res)
      }).catch(err => console.log(err));

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
      input_token,

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
  height: 425px;
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


