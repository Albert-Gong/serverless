/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="preprocess">
    <div class="list-container" v-if="!is_detail">
      <BriefList v-for="item in preprocess_items" @click="goDetailedProcess(item.api_id)" :key="item.api_id" :item="item"/>
    </div>
    <div v-else>
      <router-view/>
    </div>
  </div>

</template>

<script>
import {defineComponent, reactive, ref, watch} from 'vue'
import BriefList from "@/components/preprocess/BriefList.vue"
import {useRouter} from "vue-router"
import {preprocess_apis} from "../../enums/preprocess";

export default defineComponent({
  name: 'Preprocess',
  components: {
    BriefList
  },

  setup() {
    let router = useRouter();
    let is_detail = ref(false);
    let preprocess_items = preprocess_apis;

    watch(() => router.currentRoute.value.name, (new_value, old_value) => {
      if (new_value === "preprocessDetail") {
        is_detail.value = true
      } else {
        is_detail.value = false
      }
    }, {immediate: true})


    const goDetailedProcess = (api_id) => {
      router.push({
        name: "preprocessDetail",
        params: {
          id: api_id
        }
      })

      console.log(api_id)

    }

    return {
      is_detail,
      preprocess_items,
      goDetailedProcess,

    }
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

#preprocess {
  .list-container{
    width: 100%;
  }
  //height: 100px;
  //background-color: $container_color;
}
</style>


