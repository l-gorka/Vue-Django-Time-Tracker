<template>
    <div class="modal-card" style>
        <header class="modal-card-head">
            <h2 class="modal-card-title is-bolder">Log In</h2>
        </header>
        <section class="modal-card-body">
            <b-notification
            class="is-light"
            type="is-info"
                v-if="isRedirected"
                
                aria-close-label="Close notification"
            >To visit this section, you must be logged in.</b-notification>
            <form @submit.prevent="loginUser">
                <!-- USERNAME -->
                <b-field v-if="credentialsAreValid" label="Username">
                    <b-input class="input-username" @keyup.native.enter="loginUser" v-model="username" value></b-input>
                </b-field>
                <b-field v-else type="is-danger" :message="credentialsErrorPhrase" label="Username">
                    <b-input class="input-username" @input="clearError" v-model="username" value></b-input>
                </b-field>
                <!-- PASSWORD -->
                <b-field v-if="credentialsAreValid" label="Password">
                    <b-input
                        class="input-password"
                        @keyup.native.enter="loginUser"
                        v-model="password"
                        type="password"
                        password-reveal
                    ></b-input>
                </b-field>
                <b-field v-else type="is-danger" label="Password">
                    <b-input class="input-password" @input="clearError" v-model="password" type="password" password-reveal></b-input>
                </b-field>
            </form>
        </section>
        <footer class="modal-card-foot">
            <b-button class="btn-close" label="Close" @click="$emit('close')" />
            <b-button class="btn-login-submit" :loading="isLoading" @click="loginUser" label="Login" type="is-primary" />
        </footer>
    </div>
</template>

<script>
export default {
    name: "login",
    props: ['isRedirected'],
    components: {},
    mounted() {
    },
    data() {
        return {
            username: "",
            password: "",
            credentialsErrorPhrase: "",
            credentialsAreValid: true, // activate appropriate message if set to true
            isLoading: false,
        };
    },
    methods: {
        clearError() {
            this.credentialsAreValid = true;
        },
        loginUser() {
            // check if username and password are entered
            if (!this.username || !this.password) {
                this.credentialsErrorPhrase = "Enter username and password";
                this.credentialsAreValid = false;
                return false;
            }
            // set loading state
            this.isLoading = true;
            // Call loginUser action.
            this.$store
                .dispatch("loginUser", {
                    username: this.username,
                    password: this.password,
                })
                .then(() => {
                    this.$emit("close");
                    this.wrongCred = false;
                    this.$router.push({ name: "TimeTracker" });
                })
                .catch((err) => {
                    console.log(err.response);
                    this.credentialsErrorPhrase =
                        "Either username or password is incorrect. Please retype your credentials.";
                    this.credentialsAreValid = false;
                })
                .finally(() => (this.isLoading = false));
        },
    },
};
</script>

<style>
</style>