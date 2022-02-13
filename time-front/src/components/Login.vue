<template>
  <div class="modal-card" style="">
    <header class="modal-card-head">
      <h2 class="modal-card-title">Log In</h2>
    </header>
    <section class="modal-card-body">
      <b-field label="Username">
        <b-input @keyup.native.enter="loginUser" v-model="username" value=""></b-input>
      </b-field>
      <b-field label="Password">
        <b-input @keyup.native.enter="loginUser" v-model="password" type="password" password-reveal></b-input>
      </b-field>
      <b-notification
        v-if="wrongCred"
        type="is-danger"
        aria-close-label="Close notification"
        role="alert"
      >
        Sorry, Invalid credentials. Please try again.
      </b-notification>
    </section>
    <footer class="modal-card-foot">
      <b-button label="Close" @click="$emit('close')" />
      <b-button @click="loginUser" label="Login" type="is-primary" />
    </footer>
  </div>
</template>

<script>
export default {
  name: "login",
  components: {},
  mounted() {
    console.log("Login");
  },
  data() {
    return {
      username: "",
      password: "",
      wrongCred: false, // activate appropriate message if set to true
    };
  },
  methods: {
    loginUser() {
      // Call loginUser action.
      this.wrongCred = false;
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
          console.log(err);
          alert(err)
          this.wrongCred = true; // if the credentials were wrong set wrongCred to true
        });
    },
  },
};
</script>

<style>
</style>