<template>
  <div class="container-fluid">
      <div class="level">
        <div class="level-left">
          <div class="level-item">
            <div class="footer-copyright">
              <b>&copy; {{ year }}, Luke G</b>. <a
                href="https://github.com/"
                target="_blank"
              >GitHub</a>
            </div>
          </div>
        </div>
        <div class="level-right">
          <div class="level-item">
            <div class="logo">
              Logo here
            </div>
          </div>
        </div>
      </div>
    </div>
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