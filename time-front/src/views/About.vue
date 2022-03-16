<template>
    <div class="container">
        <div class="hero is-medium mt-6">
            a
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