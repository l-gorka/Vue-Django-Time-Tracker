<template>
  <div class="container is-fluid mt-5">
      <div class="level">
          <div class="level-left">
                <div class="level-item">
                    <div class="title has-text-primary">
                        <span>Account</span>
                    </div>
                </div>
            </div>
      </div>
      <div class="columns is-centered ">
          <div class="column is-12 is-8-desktop is-6-fullhd">
              <account-info />
          </div>
      </div>
  </div>
</template>

<script>
import AccountInfo from '../components/account/AccountInfo.vue'
export default {
    components: { AccountInfo }

}
</script>

<style>

</style>