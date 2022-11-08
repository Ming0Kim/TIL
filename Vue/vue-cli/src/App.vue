<template>
  <div id="app">
    <h2>App</h2>
    <input 
      type="text"
      @input="onAppInput"
    >
    <p>appData: {{ appMsg }}</p>
    <p>parentData: {{ appParentMsg }} </p>
    <p>childData: {{ appChildMsg }} </p>
    <AppParent
      :app-msg="appMsg"
      @on-app-child-data="appListening"
      @on-app-data = 'abcde'
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent';

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function() {
    return {
      appMsg: null,
      appParentMsg: null,
      appChildMsg: null,
    }
  },
  methods: {
    onAppInput(e) {
      this.appMsg = e.target.value
    },
    appListening(appChildData) {
      this.appChildMsg = appChildData
    },
    abcde(appParentMsg) {
      this.appParentMsg = appParentMsg
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
