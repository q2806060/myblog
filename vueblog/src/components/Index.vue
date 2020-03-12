<template>
    <div class="container">
      <div class="note" :style="note"></div>
      <el-container>
          <Header></Header>
      </el-container>
    </div>
</template>

<script>
export default {
  name: 'Index',
  data () {
    return {
      note:{
        backgroundImage:"url(" + require("../assets/mainbj.jpg") + ")",
      },
    }
  },
  methods: {

  },
  mounted() {

  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container{
}
.note{
    position: fixed;
    height: 100%;
    width: 100%;
    background: no-repeat center top;
    background-size: cover;
    z-index: -100;
    top: 0;
    left: 0;
    opacity:0.7;
}
</style>
