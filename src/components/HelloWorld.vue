<template>
  <div id="hello-world">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from "vue";

export default defineComponent({
  name: 'HelloWorld',
  props: {
    msg: {
      type: String,
      default: ''
    }
  },
  setup() {
    const count = ref(0)
    return {
      count
    }
  }

})
</script>


<style scoped lang="scss">

</style>
