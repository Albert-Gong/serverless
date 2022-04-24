/**
* Created on 2022/4/24.
* @author Zhihao Gong
* @changeLogs
*/
/**
* Created on 2022/4/10.
* @author Zhihao Gong
*/
<template>
  <div class="content">
    <h2>Serverless</h2>
    <h2>Serverless</h2>
  </div>
</template>

<script>
export default {
  name: "Logo"
}

</script>

<style lang="scss" scoped>
* {
  font-family: "Poppins", sans-serif;
}

.content {
  height: 50px;
  position: relative;
  left: -85px;
  top: -10px;

}

.content h2 {
  margin: 0;
  color: #fff;
  font-size: 32px;
  position: absolute;
  top:30px;
  left: 92px;
  transform: translate(-50%, -50%);
}

.content h2:nth-child(1) {

  color: transparent;
  -webkit-text-stroke: 1px rgba(24, 183, 255, 0.7);
}

.content h2:nth-child(2) {
  //color: #03a9f4;
  background: linear-gradient(
          -45deg,
          rgb(53, 171, 148) 0%,
          rgba(142, 68, 173, 1) 100%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: animate 4s ease-in-out infinite;
}

@keyframes animate {
  0%,
  100% {
    clip-path: polygon(
            0% 45%,
            16% 44%,
            33% 50%,
            54% 60%,
            70% 61%,
            84% 59%,
            100% 52%,
            100% 100%,
            0% 100%
    );
  }

  50% {
    clip-path: polygon(
            0% 60%,
            15% 65%,
            34% 66%,
            51% 62%,
            67% 50%,
            84% 45%,
            100% 46%,
            100% 100%,
            0% 100%
    );
  }
}

</style>
