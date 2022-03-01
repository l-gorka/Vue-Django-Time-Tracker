<template>
    <div class="section">
        <div v-if="isUserDataLoaded" class="panel is-dark has-background-white">
            <div class="panel-heading is-flex is-justify-content-space-between">
                <span>Profile Info</span>
                <b-icon icon="account"></b-icon>
            </div>
            <div class="panel-block">
                <b-field label="Last logged in">
                    
                    <p>{{lastLogin}}</p>
                </b-field>
            </div>
            <div class="panel-block">
                <b-field label="Date joined">
                    <p>{{ dateJoined }}</p>
                </b-field>
            </div>
            <div class="panel-block">
                <b-field label="Email">
                    <p>{{ email }}</p>
                </b-field>
            </div>

            <div class="panel-block">asd</div>
        </div>
    </div>
</template>

<script>
import { DateTime } from "luxon";
import { getAPI } from "../../axios-base";
export default {
    mounted() {
        this.getUserData();
    },
    data() {
        return {
            isUserDataLoaded: false,
            dateJoined: null,
            lastLogin: null,
            email: "",
        };
    },
    methods: {
        getUserData() {
            getAPI
                .get("/account/", {
                    headers: {
                        Authorization: `Bearer ${this.$store.state.accessToken}`,
                    },
                })
                .then((response) => {
                    this.lastLogin = new Date(response.data.last_login);
                    this.dateJoined = new Date(response.data.date_joined);
                    this.email = response.data.email;
                    this.isUserDataLoaded = true;
                });
        },
    },
};
</script>

<style>
</style>