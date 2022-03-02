<template>
    <div class="container mb-5 is-fullhd">
        <div>
            <CurrentTask @timeEntryCreated="getDayEntries" />
        </div>
        <div class="" v-if="dayEntries">
            <DayEntry
                @dataChanged="getDayEntries"
                :dayEntry="dayEntry"
                v-for="dayEntry in paginatedDayEntries"
                :key="dayEntry.id"
            />
        </div>
        <b-pagination :total="numberOfEntries" :current.sync="pageNumber" :per-page="perPage"></b-pagination>
    </div>
</template>

<script>
import { getAPI } from "../axios-base";
import TimeEntry from "../components/TimeEntry.vue";
import DayEntry from "../components/DayEntry.vue";
import CurrentTask from "../components/CurrentTask.vue";
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
        this.$store.dispatch("getTimeEntries").then(() => {
            this.getDayEntries();
        });
    },
    computed: {
        numberOfEntries() {
            return this.dayEntries.length;
        },
        paginatedDayEntries() {
          let pageNumber = this.pageNumber - 1
            return this.dayEntries.slice(pageNumber * this.perPage,(pageNumber + 1) * this.perPage);
        },
        token() {
            return this.$store.state.accessToken;
        },
    },
    methods: {
        getDayEntries() {
            getAPI
                .get("/day-entries/", {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    },
                })
                .then((response) => {
                    this.dayEntries = response.data;
                    for (let item of this.dayEntries) {
                        item.time_entries.reverse();
                    }
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