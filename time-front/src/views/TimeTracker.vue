<template>
    <div class="page-wrapper">
        <div>
            <CurrentTask v-if="isLoaded" @timeEntryCreated="getEntries" />
        </div>
        <div class v-if="numberOfEntries">
            <DayEntry
                :class="`day-entry-${index}`"
                @dataChanged="getEntries"
                :dayEntry="dayEntry"
                v-for="(dayEntry, index) in paginatedDayEntries"
                :key="dayEntry.id"
            />
        </div>
        <div v-else>
            <div class="hero is-halfheight">
                <div class="hero-body">
                    <div class="container has-text-centered">
                        <h2 class="title muted">You don't have any entries yet</h2>
                        <h3 class="subtitle muted mt-2">Click START button to begin new activity.</h3>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="numberOfEntries > 5" class="mx-2 pb-5">
            <b-pagination
                size="is-medium"
                :total="numberOfEntries"
                :current.sync="pageNumber"
                :per-page="perPage"
            ></b-pagination>
        </div>
    </div>
</template>

<script>
import { getAPI } from "../axios-base";
import TimeEntry from "../components/TimeEntry.vue";
import DayEntry from "../components/DayEntry.vue";
import CurrentTask from "../components/CurrentTask.vue";
import axios from "axios";
export default {
    components: { DayEntry, TimeEntry, CurrentTask },
    data() {
        return {
            dayEntries: [],
            pageNumber: 1,
            perPage: 5,
            isLoaded: false,
        };
    },
    created() {
        this.$store.dispatch("getProjects");
        this.getEntries();
    },
    computed: {
        numberOfEntries() {
            return this.dayEntries.length;
        },
        paginatedDayEntries() {
            // return sliced day entries array
            let pageNumber = this.pageNumber - 1;
            return this.dayEntries.slice(
                pageNumber * this.perPage,
                (pageNumber + 1) * this.perPage
            );
        },
        token() {
            return this.$store.state.accessToken;
        },
        isLoading() {
            // check if
            return this.$wait.any;
        },
        projects() {
            return this.$store.state.projects;
        },
    },
    methods: {
        getEntries() {
            this.$wait.start("getEntries");
            this.$store
                .dispatch("getTimeEntries")
                .then(() => {
                    this.dayEntries = this.$store.state.dayEntries;
                    this.$wait.end("getEntries");
                })
                .catch((error) => console.log("time tracker", error))
                .finally(() => (this.isLoaded = true));
        },
    },
};
</script>

<style>
.muted {
    color: darkgray;
}
.input-text-center input {
    text-align: center;
}
</style>