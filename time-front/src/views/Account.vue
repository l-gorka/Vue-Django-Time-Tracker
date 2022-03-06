<template>
    <div class="page-wrapper mt-5">
        <div class="level">
            <div class="level-left">
                <div class="level-item">
                    <div class="title has-text-primary">
                        <span>Account</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns is-multiline is-centered">
            <div class="column is-12 is-8-desktop is-6-fullhd">
                <change-password />
            </div>
            <div class="column is-12 is-8-desktop is-6-fullhd">
                <account-info />
            </div>
        </div>
    </div>
</template>

<script>
import AccountInfo from '../components/account/AccountInfo.vue';
import ChangePassword from '../components/account/ChangePassword.vue';
export default {
    components: { AccountInfo, ChangePassword }

}
</script>

<style>
</style>