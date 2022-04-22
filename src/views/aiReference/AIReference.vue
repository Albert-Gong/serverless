/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="ai-reference">
    <div class="list-container" v-if="!is_detail">
      <BriefList v-for="item in reference_items" @click="goDetailedReference(item.api_id)" :key="item.api_id"
                 :item="item"/>
    </div>
    <div v-else>
      <router-view/>
    </div>
  </div>
</template>

<script>
import {defineComponent, ref, watch} from 'vue'
import BriefList from "@/components/preprocess/BriefList.vue"
import {useRouter} from "vue-router"
import {reference_apis} from "../../enums/reference.ts";


export default defineComponent({
  name: 'AIReference',
  components: {
    BriefList
  },
  setup() {
    let router = useRouter();
    let is_detail = ref(false);
    let reference_items = reference_apis;

    watch(() => router.currentRoute.value.name, (new_value, old_value) => {
      let options = ["sentimentAnalysis"]
      let flag = false;
      for (let i = 0; i < options.length; i++)
        flag = options[i] === new_value
      if (flag) {
        is_detail.value = true
      } else {
        is_detail.value = false
      }
    }, {immediate: true})


    const goDetailedReference = (api_id) => {
      router.push({
        name: "sentimentAnalysis",
      })

      console.log(api_id)

    }

    return {
      is_detail,
      reference_items,
      goDetailedReference,

    }
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

#ai-reference {
  .list-container {
    width: 100%;
  }

}
</style>



