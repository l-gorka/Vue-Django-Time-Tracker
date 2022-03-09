<template>
    <div class="modal-card" style>
        <header class="modal-card-head">
            <h2 class="modal-card-title">Register new Account</h2>
        </header>
        <section class="modal-card-body">
            <!-- USERNAME -->
            <b-field v-if="usernameIsValid" label="Username">
                <b-input @blur="validateUsername" v-model="registerData.username"></b-input>
            </b-field>
            <b-field v-else type="is-danger" :message="usernameErrorPhrase" label="Username">
                <b-input @input="validateUsername" v-model="registerData.username"></b-input>
            </b-field>
            <!-- EMAIL -->
            <b-field v-if="emailIsValid" label="Email">
                <b-input @blur="validateEmail" v-model="registerData.email"></b-input>
            </b-field>
            <b-field v-else type="is-danger" message="Enter valid e-mail address." label="Email">
                <b-input @input="validateEmail" v-model="registerData.email"></b-input>
            </b-field>
            <!-- PASSWORD1 -->
            <b-field v-if="passwordIsValid" label="Password">
                <b-input
                    @blur="validatePassword"
                    v-model="registerData.password1"
                    type="password"
                    password-reveal
                ></b-input>
            </b-field>
            <b-field
                v-else
                type="is-danger"
                :message="passwordErrorPhrase"
                label="Password"
            >
                <b-input
                    @input="validatePassword"
                    v-model="registerData.password1"
                    type="password"
                    password-reveal
                ></b-input>
            </b-field>
            <!-- PASSWORD2 -->
            <b-field v-if="passwordsMatch" label="Re-enter password">
                <b-input
                    @blur="validatePassword"
                    @keyup.native.enter="registerUser"
                    v-model="registerData.password2"
                    type="password"
                    password-reveal
                ></b-input>
            </b-field>

            <b-field
                type="is-danger"
                message="Passwords must be the same."
                v-else
                label="Re-enter password"
            >
                <b-input
                    @input="validatePassword"
                    v-model="registerData.password2"
                    type="password"
                    password-reveal
                ></b-input>
            </b-field>
            <!-- CHECKBOX -->
            <b-field>
                <b-checkbox>
                    I accept
                    <span>terms and conditions.</span>
                </b-checkbox>
            </b-field>
        </section>
        <footer class="modal-card-foot">
            <b-button label="Close" @click="$emit('close')" />
            <b-button @click="registerUser" label="Register" type="is-primary" />
        </footer>
    </div>
</template>

<script>
export default {
    name: "login",
    components: {},
    mounted() {},
    data() {
        return {
            registerData: {
                username: "",
                email: "",
                password1: "",
                password2: "",
            },
            usernameIsValid: true,
            emailIsValid: true,

            passwordIsValid: true,
            passwordsMatch: true,

            usernameErrorPhrase: "",
            passwordErrorPhrase: "",
        };
    },
    methods: {
        validateUsername() {
            this.usernameIsValid = true;
            let loginRegex = /^(?=^\w{3,20}$)[a-zA-Z][a-zA-Z0-9]+$/;
            if (!loginRegex.test(this.registerData.username)) {
                this.usernameIsValid = false;
                this.usernameErrorPhrase =
                    "3-20 characters, starting with letter. No special characters allowed.";
                return false;
            }
        },

        validateEmail() {
            this.emailIsValid = true;
            let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(this.registerData.email)) {
                this.emailIsValid = false;
                return false;
            }
        },
        validatePassword() {
            this.passwordIsValid = true;
            this.passwordsMatch = true;
            // check if password has more than 8 characters
            if (this.registerData.password1.length < 8) {
                this.passwordErrorPhrase = "Your password must contain at least 8 characters."
                this.passwordIsValid = false;
                return false;
            }
            // check if passwords are matching
            if (!(this.registerData.password1 == this.registerData.password2)) {
                this.passwordsMatch = false;
                return false;
            }
        },
        registerUser() {
            // Check if data is valid.
            this.validateUsername();
            this.validateEmail();
            this.validatePassword();
            if (
                this.usernameIsValid &&
                this.emailIsValid &&
                this.passwordIsValid &&
                this.passwordsMatch
            ) {
                this.$store
                    .dispatch("registerUser", this.registerData) // call registerUser action in store
                    .then(() => {
                        this.$buefy.toast.open({
                            duration: 5000,
                            message: "Account has been created",
                            position: "is-bottom",
                            type: "is-success",
                        });
                        this.$emit("userRegistered");
                        this.$emit("close");
                    })
                    .catch((err) => {
                        // get error msg and display it as input message
                        console.log(err.response);
                        if (err.response.data == "Username already taken") {
                            this.usernameErrorPhrase = "Username already taken";
                            this.usernameIsValid = false;
                        } else if (err.response.data == "Password incorrect") {
                            this.passwordErrorPhrase = "Password can't be a commonly used password or similar to your other personal information."
                            this.passwordIsValid = false;
                        }
                    });
            } else return false;
        },
    },
};
</script>

<style>
</style>