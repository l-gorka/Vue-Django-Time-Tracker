<template>
    <div class>
        <div class="panel is-dark has-background-white">
            <div class="panel-heading is-flex is-justify-content-space-between">
                <span>Change password</span>
                <b-icon icon="lock"></b-icon>
            </div>
            <div class="panel-body p-3 is-expanded">
                <form @submit.prevent="changePassword">
                    <!-- OLD PASSWORD -->
                    <b-field v-if="oldPasswordIsValid" label="Old password">
                        <b-input
                            class="cy-input-old-password"
                            v-model="changePasswordData.oldPassword"
                            type="password"
                            password-reveal
                        ></b-input>
                    </b-field>
                    <b-field
                        v-else
                        type="is-danger"
                        message="The password you entered is incorrect. Please retype your current password."
                        label="Password"
                    >
                        <b-input
                            class="cy-input-old-password"
                            @input="validatePassword"
                            v-model="changePasswordData.oldPassword"
                            type="password"
                            password-reveal
                        ></b-input>
                    </b-field>
                    <!-- PASSWORD1 -->
                    <b-field v-if="passwordIsValid" label="Password">
                        <b-input
                            class="is-expanded cy-input-password"
                            @blur="validatePassword"
                            v-model="changePasswordData.password1"
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
                            class="is-expanded cy-input-password"
                            @input="validatePassword"
                            v-model="changePasswordData.password1"
                            type="password"
                            password-reveal
                        ></b-input>
                    </b-field>

                    <!-- PASSWORD2 -->
                    <b-field v-if="passwordsMatch" label="Re-enter password">
                        <b-input
                            class="is-expanded cy-input-password2"
                            @blur="validatePassword"
                            @keyup.native.enter="changePassword"
                            v-model="changePasswordData.password2"
                            type="password"
                            password-reveal
                        ></b-input>
                    </b-field>

                    <b-field
                        type="is-danger"
                        message="Password must be the same."
                        v-else
                        label="Re-enter password"
                    >
                        <b-input
                            class="is-expanded cy-input-password2"
                            @input="validatePassword"
                            v-model="changePasswordData.password2"
                            type="password"
                            password-reveal
                        ></b-input>
                    </b-field>

                    <b-button
                        class="btn-change-password"
                        :loading="isLoading"
                        @click="changePassword"
                        type="is-primary"
                    >Change password</b-button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from "../../axios-base";
export default {
    data() {
        return {
            changePasswordData: {
                oldPassword: "",
                password1: "",
                password2: "",
            },
            oldPasswordIsValid: true,
            passwordIsValid: true,
            passwordsMatch: true,
            passwordErrorPhrase: "",
            oldPasswordErrorPhrase: "",
            isLoading: false,
        };
    },
    methods: {
        validatePassword() {
            // set isValid to true before checking
            this.passwordIsValid = true;
            this.passwordsMatch = true;
            this.oldPasswordIsValid = true;
            // check if old password has more than 8 characters
            if (this.changePasswordData.oldPassword.length < 8) {
                this.oldPasswordIsValid = false;
                return false;
            }
            // check if new password has more than 8 characters
            if (this.changePasswordData.password1.length < 8) {
                this.passwordErrorPhrase =
                    "Your password must contain at least 8 characters.";
                this.passwordIsValid = false;
                return false;
            }
            // check if passwords match
            if (
                !(
                    this.changePasswordData.password1 ==
                    this.changePasswordData.password2
                )
            ) {
                this.passwordsMatch = false;
                return false;
            }
        },
        changePassword() {
            // if passwords are valid
            this.validatePassword();
            if (
                this.oldPasswordIsValid &&
                this.passwordIsValid &&
                this.passwordsMatch
            ) {
                this.isLoading = true;
                let data = {
                    old_password: this.changePasswordData.oldPassword,
                    password: this.changePasswordData.password1,
                    password2: this.changePasswordData.password2,
                };
                getAPI
                    .post("/change-password/", data, {
                        headers: {
                            Authorization: `Bearer ${this.$store.state.accessToken}`,
                        },
                    })
                    .then((response) => {
                        console.log("change password");
                        this.toast("Password successfully updated");
                        this.changePasswordData = {};
                        this.isLoading = false;
                    })
                    .catch((error) => {
                        console.log(error);
                        // if error, show message on input
                        if (error.response.status == 401) {
                            this.oldPasswordErrorPhrase = error.response.data;
                            this.oldPasswordIsValid = false;
                        } else if (error.response.status == 400) {
                            this.passwordErrorPhrase = error.response.data;
                            this.passwordIsValid = false;
                        }
                        this.changePasswordData = {};
                        this.isLoading = false;
                    });
            }
        },
        toast(toastMessage) {
            this.$buefy.toast.open({
                duration: 5000,
                message: toastMessage,
                position: "is-bottom",
                type: "is-success",
            });
        },
    },
};
</script>

<style>
</style>