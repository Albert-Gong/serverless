/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="serverless-container">
    <Navigation/>
    <div class="overview-container" v-if="is_center_page">
      <Overview v-for="service in services_info" :key="service.name" :service="service"/>
    </div>
    <div class="view-container" v-else>
      <router-view/>
    </div>
  </div>
</template>

<script>
import {defineComponent, ref, watch} from 'vue'
import Navigation from "@/components/navigation/Navigation.vue"
import Overview from "@/components/serverlessCenter/Overview.vue"
import {services} from "../../utils/basic";
import {useRouter} from "vue-router";
import {test} from "../../apis/user"
import {fromBase64} from "js-base64";

export default defineComponent({
  name: '',
  components: {
    Navigation,
    Overview
  },


  setup() {
    let router = useRouter();

    let is_center_page = ref(true);
    const services_info = services

    watch(() => router.currentRoute.value.name, (new_value, old_value) => {
      if (new_value === "serverlessCenter") {
        is_center_page.value = true
      } else {
        is_center_page.value = false
      }
    }, {immediate: true})

    let goToApig = ()=>{
      let data = {
        "cmd" : "hello, nice to see you",
        "param": '123'
      }
      test(data).then(res=>res.data).then(data=>{
        console.log(unescape(data))
      })
    }


    return {
      services_info,
      is_center_page,
      goToApig
    }
  }
})
</script>

<style scoped lang="scss">
//@import "@/styles/common";

#serverless-container {
  padding-bottom: 20px;

  .overview-container {
    margin: 30px auto;
    min-height: 700px;
    width: 700px;
  }

  .view-container {
    margin: 30px auto;
    min-height: 700px;
    width: 700px;
  }
}

</style>


