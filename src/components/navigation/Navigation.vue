/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="navigation">
    <div class="option-container">
      <div :class="{'default-option':default_option[3], 'active-option':!default_option[4]}"
           @click="jumpToPage('serverlessCenter')">Center
      </div>
      <div :class="{'default-option':default_option[0], 'active-option':!default_option[0]}"
           @click="jumpToPage('preprocess')">Preprocess
      </div>
      <div :class="{'default-option':default_option[1], 'active-option':!default_option[1]}"
           @click="jumpToPage('aiReference')">AI-Reference
      </div>
      <div :class="{'default-option':default_option[2], 'active-option':!default_option[2]}"
           @click="jumpToPage('pipeline')">Pipeline
      </div>
    </div>

  </div>
</template>

<script>
import {defineComponent, reactive, ref, watch} from 'vue'
import {useRouter} from "vue-router"

export default defineComponent({
  name: 'Navigation',

  setup() {

    let router = useRouter()

    let default_option = ref([true, true, true])


    watch(() => router.currentRoute.value.name, (new_value, old_value) => {
      console.log(new_value)
      let dict = {"preprocess": 0, "aiReference": 1, "pipeline": 2, 'serverlessCenter':3}

      let index = dict[new_value];
      default_option.value = [true, true, true];
      default_option.value[index] = !default_option.value[index];

    }, {immediate: true})

    let jumpToPage = (view) => {

      router.push({
        name: view
      })
    }

    return {
      default_option,
      jumpToPage
    }
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

#navigation {

  width: 100%;
  height: 75px;
  background-color: $container_color;
  display: flex;
  flex-direction: row;
  align-items: center;

  .option-container {
    margin: 0 auto;
    display: flex;
    justify-self: center;

  }

  .default-option {
    font-family: Arial, sans-serif;
    color: #7c795d;
    font-weight: 500;
    font-size: 20px;
    margin: 0;
    width: 135px;

    text-decoration: none;
    line-height: 1;
    padding-bottom: 2px;
    --bg-h: 2px;
    background: $theme_background no-repeat right bottom / 0 var(--bg-h);
    transition: background-size 350ms;

    &:where(:hover, :focus-visible) {
      background-size: 80% var(--bg-h);
      background-position-x: center;
      cursor: pointer;
      //color: rgb(17, 19, 51);
    }
  }

  .active-option {
    font-family: Arial, sans-serif;
    color: #7c795d;
    font-weight: 500;
    font-size: 20px;
    margin: 0;
    width: 135px;

    text-decoration: none;
    line-height: 1;
    padding-bottom: 2px;
    --bg-h: 2px;
    background: $theme_background no-repeat right bottom / 0 var(--bg-h);
    background-size: 80% var(--bg-h);
    background-position-x: center;
    cursor: pointer;
  }

}
</style>


