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
                                >Capture every task you work on. Take control over time intervals.</h2>
                                <div class="button-wrap">
                                    <a
                                        @click="$router.push('/tracker')"
                                        v-if="isLoggedIn"
                                        class="button is-rounded is-primary raised mr-2"
                                    >Go to tracker</a>
                                    <a
                                        @click="showRegisterModal()"
                                        v-else
                                        class="button is-rounded is-primary raised mr-2"
                                    >Get Started</a>
                                    <a @click="scrollTo()" class="button is-rounded">Discover</a>
                                </div>
                            </div>
                            <div class="column is-5">
                                <figure class="image is-square">
                                    <img
                                        src="https://res.cloudinary.com/dgmcox/image/upload/v1646557492/15_1_qdsmnx.webp"
                                        alt="Description"
                                    />
                                </figure>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div ref="howItWorks" class="section px-0 is-primary has-background-primary">
            <div class="page-wrapper">
                <div class="hero is-bold">
                    <div class="hero-head has-text-centered">
                        <h2 class="title has-text-white pt-6 is-1 is-bold is-spaced">How it works:</h2>
                    </div>
                    <div class="hero-body is-vcentered px-0">
                        <b-carousel>
                            <b-carousel-item v-for="(carousel, i) in carousels" :key="i">
                                <div class="hero carousel-body">
                                    <div class="hero-body px-2">
                                        <div
                                            class="columns is-multiline has-text-centered is-vcentered"
                                        >
                                            <div
                                                class="carousel-caption column is-12-tablet is-6-desktop"
                                            >
                                                <div class="hero">
                                                    <h4
                                                        class="subtitle has-text-white is-bold is-3"
                                                    >{{carousel.title}}</h4>
                                                    <h4
                                                        class="subtitle has-text-white is-5"
                                                    >{{carousel.subtitle}}</h4>
                                                </div>
                                            </div>

                                            <div class="column is-12-tablet is-6-desktop">
                                                <img :src="carousel.url" alt="carousel-image" />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </b-carousel-item>
                        </b-carousel>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-wrapper">
            <div class="section px-0 hero is-fullheight-with-navbar">
                <div class="hero-head">
                    <div class="hero-head has-text-centered">
                        <h2 class="title is-2 is-bold is-spaced">Responsive design</h2>
                    </div>
                </div>
                <div class="hero-body">
                    <img
                        src="https://res.cloudinary.com/dgmcox/image/upload/v1647803166/screens_s8daxt.webp"
                        alt
                    />
                </div>
            </div>
            <div class="section">
                <div class="hero">
                    <div class="hero-head">
                        <div class="hero-head has-text-centered">
                            <h2 class="title is-2 is-bold is-spaced">Created with</h2>
                        </div>
                    </div>
                    <div class="hero-body">
                        <div class="columns is-centered is-mobile is-multiline">
                            <div class="column is-3-mobile is-2-desktop has-text-centered">
                                <img
                                    src="https://res.cloudinary.com/dgmcox/image/upload/c_pad,h_120,w_120/v1646426610/1184px-Vue.js_Logo_2.svg_njfaal.webp"
                                    alt
                                />
                            </div>
                            <div class="column is-3-mobile is-2-desktop has-text-centered">
                                <img
                                    src="https://res.cloudinary.com/dgmcox/image/upload/c_pad,h_120,w_120/v1646426480/26799900_tnwy94.webp"
                                    alt
                                />
                            </div>
                            <div class="column is-3-mobile is-2-desktop has-text-centered">
                                <img
                                    src="https://res.cloudinary.com/dgmcox/image/upload/c_pad,h_120,w_120/v1646425651/bulma-logo_ixsvyd.webp"
                                    alt
                                />
                            </div>
                            <div
                                class="column is-6-mobile is-5-tablet is-4-desktop is-3-widescreen has-text-centered"
                            >
                                <img
                                    src="https://res.cloudinary.com/dgmcox/image/upload/c_scale,h_120/v1647974074/logo_u81zno.png"
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
import { axiosBase } from "../axios-base";
export default {
    created() {
        axiosBase
            .get("wake-up/")
            .then((response) => {
                this.isBackendOn = true;
                console.log('home', response);
            })
            .catch((err) => console.log(err));
    },
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
            isBackendOn: false,
            carousels: [
                {
                    title: "Track your time using stopwatch",
                    subtitle:
                        "Hit start button to begin tracking your activity",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/c_scale,w_1080/v1647802625/timeTracker1_w3rbos.webp",
                },
                {
                    title: "Enter or edit time entries manually",
                    subtitle:
                        "Set time and date, project and description. Continue past activity with just one click",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/c_scale,w_1080/v1647802782/timeTrackerSetDate_lkpfcd.webp",
                },
                {
                    title: "See where you spend time",
                    subtitle:
                        "You can see all your activities in a given period, and how much time you've spent on each one.",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/c_scale,w_1080/v1647802919/dashboard_wuohd8.webp",
                },
                {
                    title: "Manage projects",
                    subtitle:
                        "Projects make it easier to analyze data, generate more useful reports, and see where and how you spend time.",
                    url: "https://res.cloudinary.com/dgmcox/image/upload/c_scale,w_1080/v1647803067/projects_okzlet.webp",
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
        showRegisterModal() {
            this.$store.commit("openRegisterModal");
        },
    },
    components: {},
};
</script>

<style>
.carousel-body {
    height: 70vh;
}
body {
    background: #f5f5f5;
}
.level-item {
    flex-shrink: 1;
}
</style>