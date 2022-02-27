<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>{{store}}</h2>
    <h2>{{loggedIn}}</h2>
    <v-swatches v-model="color"></v-swatches>
  </div>
</template>

<script>
import 'vue-swatches/dist/vue-swatches.css'
import VSwatches from 'vue-swatches';
export default {
  components: { VSwatches },
  data() {
    return {
      color: '#000000'
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