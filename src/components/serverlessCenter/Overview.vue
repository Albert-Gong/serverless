/**
* Created on 2022/4/21.
* @author Zhihao Gong
* @changeLogs
*/
<template>
  <div id="overview-container" @click="goToService">
    <img :src="service.image" alt="image" class="image"/>
    <div class="content-container">
      <h2>{{ service.name }}</h2>
    </div>

  </div>
</template>

<script>
import {defineComponent, reactive, onMounted} from 'vue';

export default defineComponent({
  name: 'Overview',
  props: {
    service: {
      type: Object,
      default: {}
    }
  },
  setup() {
    // let image_src = this.service.image;
    // console.log(image_src)

    let goToService = function () {
      console.log(this.service)
    }

    return {
      // image_src,
      goToService
    }
  }
})
</script>

<style scoped lang="scss">
@import "@/styles/common";

#overview-container {
  height: 190px;
  background-color: $container_color;
  border-radius: 10px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  padding: 20px;


  .image {
    display: block;
    width: 150px;
    height: 150px;
  }
  .content-container{
    width: 100%;
    margin-left: 20px;
    height: 150px;
    border: 1px solid red;
  }

}
</style>


