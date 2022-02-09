<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>{{store}}</h2>
    <h2>{{loggedIn}}</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {

    }
  },
  computed: {
    store() {
      return this.$store.state
    },
    loggedIn() {
      return this.$store.getters.loggedIn
    }
  }
}
</script>