<template>
    <div class="section">
        <div v-if="userData" class="panel is-dark has-background-white">
            <div class="panel-heading is-flex is-justify-content-space-between">
                <span>Profile Info</span>
                <b-icon icon="account"></b-icon>
            </div>
            <div class="panel-block">
                <b-field label="Last logged in">
                    <p>{{userData.last_login}}</p>
                </b-field>
            </div>
            <div class="panel-block">
                <b-field label="Date joined">
                    <p>{{userData.date_joined}}</p>
                </b-field>
            </div>
            <div class="panel-block">
                <b-field label="Email">
                    <p>{{userData.email}}</p>
                </b-field>
            </div>

            <div class="panel-block">asd</div>
        </div>
    </div>
</template>

<script>
import { getAPI } from "../../axios-base";
export default {
    mounted() {
        this.getUserData()
    },
    data() {
        return {
            userData: {}
        }
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
        console.log('resp account', response.data)
        this.userData = response.data
        });
        }
    }
}
</script>

<style>
</style>