/**
* Created on 2022/4/24.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="login-view">
      <LoginBox></LoginBox>
  </div>
</template>

<script>
import {defineComponent, reactive, ref} from 'vue'
import LoginBox from "@/components/login/Login.vue"

export default defineComponent({
  name: 'LoginView',
  components:{
    LoginBox
  },
  setup() {

    return {
    }
  }
})
</script>

<style scoped lang="scss">
#login-view{
  height: 100vh;
  display: flex;

  align-items: center;
}
</style>


