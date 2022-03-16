<template>
    <div class="has-background-white">
        <div class="page-wrapper">
            <div class="hero is-fullheight-with-navbar is-bold">
                <div class="hero-body">
                    <div class="container">
                        <div class="columns is-vcentered">
                            <div class="column is-5 is-offset-1 landing-caption">
                                <h1 class="title is-1 is-bold is-spaced">Time tracker</h1>
                                <h2
                                    class="subtitle is-5 is-muted"
                                >Lorem ipsum sit dolor amet is a dummy text used by typography industry</h2>
                                <div class="button-wrap">
                                    <a  
                                        @click="$router.push('/tracker')"
                                        v-if="isLoggedIn"
                                        class="button is-rounded is-primary raised mr-2"
                                    >Go to tracker</a>
                                    <a
                                        v-else
                                        class="button is-rounded is-primary raised mr-2"
                                    >Get Started</a>
                                    <a @click="scrollTo()" class="button is-rounded">Discover</a>
                                </div>
                            </div>
                            <div class="column is-5">
                                <figure class="image">
                                    <img
                                        src="https://res.cloudinary.com/dgmcox/image/upload/v1646557492/15_1_qdsmnx.png"
                                        alt="Description"
                                    />
                                </figure>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <div class="hero is-fullheight-with-navbar is-bold">
                    <div class="hero-head has-text-centered">
                        <h2 ref="howItWorks" class="title is-2 is-bold is-spaced">How it works:</h2>
                    </div>
                    <div class="hero-body is-vcentered px-0">
                        <b-carousel>
                            <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
                                <div class="hero">
                                    <div class="hero-body px-0">
                                        <div
                                            class="columns is-multiline has-text-centered is-vcentered"
                                        >
                                            <div class="column is-12-tablet is-6-desktop">
                                                <h4 class="subtitle is-bold is-3">{{carousel.title}}</h4>
                                                <h4 class="subtitle is-5">{{carousel.subtitle}}</h4>
                                            </div>
                                            <div class="column is-12-tablet is-6-desktop">
                                                <img :src="carousel.url" alt />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </b-carousel-item>
                        </b-carousel>
                    </div>
                </div>
            </div>
            <div class="hero is-fullheight-with-navbar">
                <div class="hero-head">
                    <div class="hero-head has-text-centered">
                        <h2 class="title is-2 is-bold is-spaced">Blah blah:</h2>
                    </div>
                </div>
                <div class="hero-body">
                    <img
                        src="https://res.cloudinary.com/dgmcox/image/upload/v1646586865/screens_s8daxt.png"
                        alt
                    />
                </div>
            </div>
            <div>
                <div class="hero">
                    <div class="hero-head">
                        <div class="hero-head has-text-centered">
                            <h2 class="title is-2 is-bold is-spaced">Created with</h2>
                        </div>
                    </div>
                    <div class="hero-body">
                        <div class="columns is-centered is-mobile">
                            <div class="column is-3 has-text-centered">
                                <img
                                    src="https://res.cloudinary.com/dgmcox/image/upload/c_pad,h_120,w_120/v1646426610/1184px-Vue.js_Logo_2.svg_njfaal.png"
                                    alt
                                />
                            </div>
                            <div class="column is-3 has-text-centered">
                                <img
                                    src="https://res.cloudinary.com/dgmcox/image/upload/c_pad,h_120,w_120/v1646426480/26799900_tnwy94.png"
                                    alt
                                />
                            </div>
                            <div class="column is-3 has-text-centered">
                                <img
                                    src="https://res.cloudinary.com/dgmcox/image/upload/c_pad,h_120,w_120/v1646425651/bulma-logo_ixsvyd.png"
                                    alt
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    computed: {
        isMobile() {
            if (window.innerWidth < 768) {
                return true;
            } else return false;
        },
        isLoggedIn() {
            return this.$store.getters.loggedIn;
        },
    },
    data() {
        return {
            email: "",
            carousels: [
                {
                    title: "Track your time using stopwatch",
                    subtitle:
                        "Type what you're working on, select project and start the timer",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/v1646582252/timeTracker1_w3rbos.png",
                },
                {
                    title: "Enter or edit time entries manually",
                    subtitle:
                        "Set time and date, continue activity with one click",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/v1646582252/timeTrackerSetDate_lkpfcd.png",
                },
                {
                    title: "See where you spend time",
                    subtitle: "",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/v1646582252/dashboard_wuohd8.png",
                },
                {
                    title: "Track time on projects, and keep an eye on progress",
                    subtitle: "",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/v1646582252/projects_okzlet.png",
                },
            ],
        };
    },
    methods: {
        scrollTo() {
            const element = this.$refs.howItWorks;
            console.log(element);
            element.scrollIntoView({ behavior: "smooth" });
        },
    },
    components: {},
};
</script>

<style>
body {
    background: #f5f5f5;
}
.level-item {
    flex-shrink: 1;
}
</style>