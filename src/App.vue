<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script lang="ts">
import {defineComponent, reactive, watch} from 'vue'
import HelloWorld from "@/components/HelloWorld.vue";
import {useRouter} from "vue-router";

export default defineComponent({
  name: 'Home',
  components:{
    HelloWorld
  },
  props: {
    msg: {
      type: String,
      default: ''
    }
  },
  // watch:{
  //   route(new_val, old_val){
  //     console.log(new_val, old_val)
  // },
  setup() {
    // let router = useRouter();
    // let current_route = router.currentRoute;
    // watch(current_route, (new_val, old_val) => {
    //   console.log(new_val.name)
    // }, {immediate:true})

    return {

    }
  }
})
</script>

<style lang="scss">


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
