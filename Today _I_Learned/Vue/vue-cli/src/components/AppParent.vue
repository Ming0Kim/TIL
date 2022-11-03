<template>
  <div>
    <h2>AppParent</h2>
    <input 
    type="text"
    @input="onAppParentInput">
    <p>parentData: {{ appParentMsg }} </p>
    <p>appData: {{ appMsg }} </p>
    <p>childData: {{ appChildMsg }} </p>
    <AppChild
      :app-msg="appMsg"
      :app-parent-msg="appParentMsg"
      @on-app-child-input="parentListening"
      />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild';

export default {
  name:'AppParent',
  components: {
    AppChild
  },
  props: {
    appMsg: String,
  },
  data: function() {
    return {
      appParentMsg : null,
      appChildMsg : null,
    }
  },
  methods: {
    onAppParentInput(ev) {
      this.appParentMsg = ev.target.value
      this.$emit('on-app-data', this.appParentMsg)
    },
    parentListening(appChildData) {
      this.appChildMsg=appChildData
      this.$emit('on-app-child-data', appChildData)
    }
  }
}
</script>

<style>

</style>