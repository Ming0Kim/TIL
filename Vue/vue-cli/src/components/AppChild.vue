<template>
  <div>
    <h2>AppChild</h2>
    <input type="text"
    @input="onAppChildInput">
    <p>appData: {{ appMsg }} </p>
    <p>parentData: {{ appParentMsg }} </p>
    <p>childData: {{ appChildMsg }} </p>
  </div>
</template>

<script>
export default {
  name:'AppChild',
  props: {
    appMsg: String,
    appParentMsg: String,
  },
  data: function() {
    return {
      appChildMsg: null,
    }
  },
  methods: {
    onAppChildInput: function(event) {
      this.appChildMsg=event.target.value
      this.$emit('on-app-child-input', this.appChildMsg)
    }
  }
}
</script>

<style>

</style>