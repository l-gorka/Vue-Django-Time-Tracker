<template>
  <b-navbar class="" fixed-top>
    <template #brand>
      <p> a {{loginModalActive}}</p>
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
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a @click="showModal" class="button is-light"> Log in </a>
          <b-modal
            @close="loginModalActive = false"
            :active="loginModalActive"
            has-modal-card
            full-screen="true"
            trap-focus
            :destroy-on-hide="false"
            aria-role="dialog"
            aria-label="Example Modal"
            close-button-aria-label="Close"
            aria-modal
          >
            <template #default="props">
              <Login
                @projectAdded="projectAdded($event)"
                @close="props.close"
              ></Login>
            </template>
          </b-modal>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import Login from '../components/Login.vue'
export default {
    components: { Login },
    data() {
        return {
            loginModalActive: false,
        }
        
    },
    methods: {
      showModal() {
        this.loginModalActive = true
      }
    }
}
</script>