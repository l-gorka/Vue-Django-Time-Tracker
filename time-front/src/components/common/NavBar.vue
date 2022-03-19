<template>
    <section class>
        <b-loading v-model="isLoading" :can-cancel="true"></b-loading>
        <b-navbar shadow fixed-top>
            <template #brand>
                <b-navbar-item class="py-0" tag="router-link" :to="{ path: '/' }">
                    <img
                        src="https://res.cloudinary.com/dgmcox/image/upload/v1646519282/Tracker500x60_xppaai.png"
                        alt="Time tracker logo"
                    />
                </b-navbar-item>
            </template>
            <template #start>
                <b-navbar-item tag="router-link" :to="{ path: '/' }">Home</b-navbar-item>
                <b-navbar-item tag="router-link" :to="{ path: '/tracker/' }">Tracker</b-navbar-item>
                <b-navbar-item
                    v-if="isLoggedIn"
                    tag="router-link"
                    :to="{ path: '/dashboard' }"
                >Dashboard</b-navbar-item>
                <b-navbar-item
                    v-if="isLoggedIn"
                    tag="router-link"
                    :to="{ path: '/projects' }"
                >Projects</b-navbar-item>
                <b-navbar-item
                    v-if="isLoggedIn"
                    tag="router-link"
                    :to="{ path: '/account' }"
                >Account</b-navbar-item>
            </template>

            <template #end>
                <b-navbar-item tag="div">
                    <div v-if="isLoggedIn" class="buttons">
                        <a @click="logoutUser" class="button is-ghost nav-btn-logout">
                            <strong>Log out</strong>
                        </a>
                    </div>
                    <div v-else class="buttons">
                        <a class="nav-btn-register button is-primary" @click="showRegisterModal">
                            <strong>Sign up</strong>
                        </a>
                        <a
                            class="nav-btn-login button is-light"
                            @click="showLoginModal(isRedirected=false)"
                        >
                            <strong>Log In</strong>
                        </a>
                    </div>
                </b-navbar-item>
            </template>
        </b-navbar>
    </section>
</template>

<script>
import Register from "./Register.vue";
import Login from "./Login.vue";
export default {
    components: { Login, Register },
    data() {
        return {};
    },
    computed: {
        isLoggedIn() {
            return this.$store.getters.loggedIn;
        },
        loginModalOpen() {
            return this.$store.state.loginModalOpen;
        },
        registerModalOpen() {
            return this.$store.state.registerModalOpen;
        },
        isLoading() {
            // check if there is waiting state,
            return this.$wait.any;
        },
    },
    watch: {
        // when state is changed to true, show login modal
        "$store.state.loginModalOpen": {
            handler(open) {
                if (open) {
                    let isRedirected = true; // display redirection message
                    this.showLoginModal(isRedirected);
                }
            },
        },

        // when state is changed to true, show register modal
        "$store.state.registerModalOpen": {
            handler(open) {
                if (open) {
                    this.showRegisterModal();
                }
            },
        },
    },
    methods: {
        showLoginModal(isRedirected) {
            this.$buefy.modal.open({
                props: { isRedirected: isRedirected },
                parent: this,
                component: Login,
                hasModalCard: true,
                customClass: "",
                trapFocus: true,
                onCancel: () => this.$store.commit("closeLoginModal"),
                events: {
                    close: () => this.$store.commit("closeLoginModal"),
                },
            });
        },
        showRegisterModal() {
            let isMobile = false;
            if (window.innerWidth < 768) {
                isMobile = true;
            }
            this.$buefy.modal.open({
                parent: this,
                fullScreen: isMobile,
                component: Register,
                hasModalCard: true,
                customClass: "",
                trapFocus: true,
                onCancel: () => {
                    console.log("navbar");
                    this.$store.commit("closeRegisterModal");
                },
                events: {
                    userRegistered: () => {
                        this.$store.commit("closeRegisterModal");
                        this.showLoginModal();
                    },
                    close: () => this.$store.commit("closeRegisterModal"),
                },
            });
        },
        logoutUser() {
            this.$store.dispatch("logoutUser");
            this.$router.push({ name: "Home" });
        },
    },
};
</script>