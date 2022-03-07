<template>
    <div class="container">
        <div class="hero is-medium mt-6">
            <div class="hero-head">
                <b-button type="is-primary" label="Wait" @click="wait" />
            </div>
            <div class="hero-body">
                <p>{{waiting}}</p>
                <p v-if="$wait.any">
                    <b-icon icon="reload" size="is-large"></b-icon>
                </p>
                <b-notification :closable="false">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id fermentum quam. Proin sagittis, nibh id hendrerit imperdiet, elit sapien laoreet elit
                    <b-loading :is-full-page="isFullPage" v-model="waiting" :can-cancel="true">
                    </b-loading>
                </b-notification>
            </div>
        </div>
    </div>
</template>

<script>
import "vue-swatches/dist/vue-swatches.css";
import VSwatches from "vue-swatches";
export default {
    components: { VSwatches },
    data() {
        return {
            color: "#000000",
        };
    },
    methods: {
        wait() {
            this.$wait.start("clicked");
            setTimeout(() => {
                this.$wait.end("clicked");
            }, 5000);
        },
    },
    computed: {
        waiting() {
            return this.$wait.any;
        },
        store() {
            return this.$store.state;
        },
        loggedIn() {
            return this.$store.getters.loggedIn;
        },
    },
};
</script>