<template>
  <div id="app">
    <CatComponent/>
  </div>
</template>

<script>
import CatComponent from '@/components/CatComponent';

export default {
  name: 'App',
  components: {
    CatComponent,
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
}
</style>
