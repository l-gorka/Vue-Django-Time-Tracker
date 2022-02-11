<template>
  <b-navbar class="" fixed-top>
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <img
          src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
          alt="Lightweight UI components for Vue.js based on Bulma"
        />
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item tag="router-link" :to="{ path: '/about/' }">
        About
      </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ path: '/tracker/' }">
        Tracker
      </b-navbar-item>
      <b-navbar-dropdown hoverable label="Info">
        <b-navbar-item href="#"> About </b-navbar-item>
        <b-navbar-item href="#"> Contact </b-navbar-item>
      </b-navbar-dropdown>
    </template>

    <template #end>
      <b-navbar-item tag="div">
        <div v-if="isLoggedIn" class="buttons">
          <a @click="logoutUser" class="button is-ghost">
            <strong>Log out</strong>
          </a>
        </div>
        <div v-else class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a class="button is-light" @click="cardModal">
            <strong>Log In</strong>
          </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import Login from "../components/Login.vue";
export default {
  components: { Login },
  data() {
    return {};
  },
  computed: {
    isLoggedIn() {
      console.log(this.$store);
      return this.$store.getters.loggedIn;
    },
  },
  methods: {
    showModal() {
      this.loginModalActive = true;
    },
    cardModal() {
      this.$buefy.modal.open({
        parent: this,
        component: Login,
        hasModalCard: true,
        customClass: "custom-class custom-class-2",
        trapFocus: true,
      });
    },
    logoutUser() {
        this.$store.dispatch('logoutUser')
        this.$router.push({ name: "Home" });
      },
  },
};
</script>