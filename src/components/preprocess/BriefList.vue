/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="brief-container">
    <img :src="item.image" alt="image here" class="image"/>
    <div class="content-container">
      <h3>{{ item.api_name }}</h3>
      <p class="brief-des-container">{{item.api_des}}.</p>
    </div>
  </div>
</template>

<script>
import {defineComponent, reactive} from 'vue'

export default defineComponent({
  name: 'BriefList',
  props:{
    item:{
      type: Object,
      default: {},
    }
  },
  setup() {

    return {}
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

#brief-container {
  height: 80px;
  background-color: $container_color;
  border-radius: 10px;
  margin-bottom: 20px;
  display: flex;
  padding: 10px;

  &:hover {
    cursor: pointer;
    animation: scale 0.1s ease-in-out 1;
    animation-fill-mode: forwards;
  }

  .image {
    display: block;
    height: 60px;
    width: 60px;
  }

  .content-container {
    margin-left: 20px;
    display: flex;
    flex-direction: column;

    p, h3 {
      margin: 0;
      text-align: left;
    }

    ::-webkit-scrollbar {
      display: none
    }
    .brief-des-container {
      max-width: 600px;
      text-align: left;
      font-size: 16px;
      line-height: 16px;
      height: 36px;
      overflow-x: scroll;
    }
  }


}
</style>


