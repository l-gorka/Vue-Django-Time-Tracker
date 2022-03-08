<template>
    <div class="page-wrapper">
        <div>
            <CurrentTask @timeEntryCreated="getEntries" />
        </div>
        <div class v-if="dayEntries">
            <DayEntry
                @dataChanged="getEntries"
                :dayEntry="dayEntry"
                v-for="dayEntry in paginatedDayEntries"
                :key="dayEntry.id"
            />
        </div>
        <div class="mx-2 pb-5">
            <b-pagination
                size="is-medium"
                :total="numberOfEntries"
                :current.sync="pageNumber"
                :per-page="perPage"
            ></b-pagination>
        </div>
        <b-notification :closable="false">
            <b-loading is-full-page="isFullPage" v-model="isLoading" :can-cancel="true"></b-loading>
        </b-notification>
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
        };
    },
    created() {
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
            return this.$wait.any
        }
    },
    methods: {
        getEntries() {
            this.$wait.start('getEntries')
            
            getAPI
                .get("/day-entries/", {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    },
                })
                .then((response) => {
                    this.$store.dispatch("getTimeEntries")
                    this.dayEntries = response.data;
                    for (let item of this.dayEntries) {
                        item.time_entries.reverse();
                    }
                    this.$wait.end('getEntries')
                });
        },
    },
};
</script>

<style>
.input-text-center input {
    text-align: center;
}
</style>