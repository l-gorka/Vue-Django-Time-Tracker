<template>
    <div class="about">
        <div class="section hero has-background-white is-bold">
            <div class="hero-body has-text-centered">
                <h2 class="title is-2 is-bold is-spaced">Subscribe for the newsletter</h2>
                <h3
                    class="subtitle is-5"
                >Lorem ipsum sit dolor amet is a dummy text used by typography industry</h3>
                <!-- CAROUSEL -->
                <div class="hero-body px-0">
                    <div class="columns is-multiline has-text-centered is-vcentered">
                        <div class="column is-12-tablet is-6-desktop">
                            <h4 class="subtitle is-bold is-3">{{carousel.title}}</h4>
                            <h4 class="subtitle is-5">{{carousel.subtitle}}</h4>
                        </div>
                        <div class="column is-12-tablet is-6-desktop">
                            <img :src="carousel.url" alt />
                        </div>
                    </div>
                </div>
                <div class="is-flex mt-4 mt-5-desktop is-justify-content-center">
                    <b-input
                        class="mr-4"
                        placeholder="Email"
                        v-model="email"
                        type="email"
                        icon="email"
                        :size="isMobile ? '' : 'is-large'"
                        rounded
                    ></b-input>
                    <b-button :size="isMobile ? '' : 'is-large'" rounded type="is-primary">Submit</b-button>
                </div>
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
    computed: {
        store() {
            return this.$store.state;
        },
        loggedIn() {
            return this.$store.getters.loggedIn;
        },
    },
};
</script>