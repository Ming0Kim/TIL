<template>
  <div>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name: "HelloView",
  data() {
    return {
      userName: this.$route.params.userName,
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.userName = this.params.userName
    next()
  },
}
</script>

<style></style>
