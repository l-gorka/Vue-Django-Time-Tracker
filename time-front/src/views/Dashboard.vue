<template>
    <div class="container is-fluid mt-5">
        <div class="level">
            <div class="level-left">
                <div class="level-item">
                    <div class="title is-danger">
                        <b-icon icon="view-dashboard" size="is-small"></b-icon>
                        <span class="is-danger"> Dashboard</span>
                    </div>
                </div>
            </div>
            <div class="level-right">
                <div class="level-item">
                    <div class="title">
                        <date-picker v-if="isLoaded" @setDate="setDate" />
                        <b-button
                            v-else
                            type="is-primary is-light"
                            icon-left="calendar"
                            label="Set time"
                        />
                    </div>
                </div>
            </div>
        </div>
        <div class="columns is-multiline">
            <div class="column is-8">
                <div class="columns">
                    <div class="column is-half">
                        <div class="box notification is-danger">
                            <div class="heading">{{ dateLabel }}</div>
                            <div class="title">{{ timeTotalLabel }}</div>
                            <div class="level">
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Billable</div>
                                        <div class="title is-5">100%</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Amount</div>
                                        <div class="title is-5">$ 56</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Success %</div>
                                        <div class="title is-5">+ 28,5%</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-half">
                        <div class="box notification is-info">
                            <div class="heading">Top project</div>
                            <div class="title">Some project here</div>
                            <div class="level">
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Orders $</div>
                                        <div class="title is-5">425K</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Returns $</div>
                                        <div class="title is-5">106K</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Success %</div>
                                        <div class="title is-5">+ 28,5%</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="message">
                    <div class="message-header">
                        <p>Chart</p>
                    </div>
                    <div class="message-body">
                        <bar />
                    </div>
                </div>
            </div>
            <div class="column is-4">
                <div class="message">
                    <div class="message-header">
                        <p>Chart</p>
                    </div>
                    <div class="message-body">
                        <doughnut
                            @projectsData="displayProjectsData"
                            v-if="filteredEntries && projectsObj"
                            :entries="filteredEntries"
                            :projects="projectsObj"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { DateTime, Duration } from "luxon";
import { getAPI } from "@/axios-base.js";
import Bar from "../components/dashboard/Bar.vue";
import Doughnut from "../components/dashboard/Doughnut.vue";
import DatePicker from "../components/dashboard/DatePicker.vue";
export default {
    components: { Bar, Doughnut, DatePicker },
    data() {
        return {
            isLoaded: false,
            projectsObj: {},
            timeEntries: {},
            filteredEntries: {},
            dateStart: null,
            dateEnd: null,
            dateLabel: "",
            timeTotalLabel: "",
        };
    },
    methods: {
        setDate(dateStart, dateEnd, dateOptionSelected) {
            this.filteredEntries = this.timeEntries;
            let unixStart = dateStart.ts / 1000;
            let unixEnd = dateEnd.ts / 1000;
            this.filteredEntries = this.timeEntries.filter((entry) => {
                return (
                    entry.start_date > unixStart && unixEnd > entry.start_date
                );
            });
            this.dateLabel = dateOptionSelected;
        },
        displayProjectsData(totalSeconds, projectsData) {
            console.log("display", totalSeconds, projectsData);
            let timeStr = Duration.fromMillis(totalSeconds * 1000).toFormat(
                "hh:mm:ss"
            );
            this.timeTotalLabel = `${timeStr}`;
        },
        getProjects() {
            getAPI
                .get("/project-list/", {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    },
                })
                .then((response) => {
                    this.projectsObj = response.data;
                });
        },
        getTimeEntries() {
            getAPI
                .get("/time-entries/", {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    },
                })
                .then((response) => {
                    this.timeEntries = response.data;
                    this.isLoaded = true;
                });
        },
    },
    computed: {
        token() {
            return this.$store.state.accessToken;
        },
    },
    mounted() {
        this.getProjects();
        this.getTimeEntries();
    },
};
</script>

<style>
</style>