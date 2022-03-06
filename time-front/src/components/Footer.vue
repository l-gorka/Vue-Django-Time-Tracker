<template>
  <footer class="footer">
  <div class=" has-text-centered">
    <p>
      <strong>Trackerrr</strong> by Luke G &copy; {{year}}
    </p>
  </div>
</footer>
</template>

<script>
export default {
data () {
    return {
      year: new Date().getFullYear()
    }
  },
}
</script>

<style>

</style>