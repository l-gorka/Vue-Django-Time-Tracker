<template>
    <div class="page-wrapper mt-5">
        <div class="">
            <div class="level is-centered">
                <div class="level-left">
                    <div class="level-item">
                        <h1 class="title is-3 has-text-primary">Dashboard</h1>
                    </div>
                </div>
                <div class="level-right">
                    <div class="level-item">
                        <div class="title">
                            <date-picker
                                :largeIcon="true"
                                v-if="dataLoaded"
                                @setDate="setDate"
                            />
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
                            <div class="box box-time-total notification is-primary">
                                <div class="heading">{{ dateLabel }}</div>
                                <div class="title">{{ timeTotalLabel }}</div>
                            </div>
                        </div>
                        <div class="column is-half">
                            <div class="box box-top-project notification is-info">
                                <div class="heading">Top project</div>
                                <div class="title">{{ topProjectLabel }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="message">
                        <div class="message-header is-flex is-justify-content-space-between">
                            <span>Timeline</span>
                            <b-icon icon="chart-box-outline"></b-icon>
                        </div>
                        <div class="message-body">
                            <Bar
                                v-if="filteredEntries"
                                :entries="filteredEntries"
                                :projects="sortedProjects"
                                :dateStart="dateStart"
                                :dateEnd="dateEnd"
                            />
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="message">
                        <div class="message-header is-flex is-justify-content-space-between">
                            <span>Projects</span>
                            <b-icon icon="chart-donut"></b-icon>
                        </div>
                        <div class="message-body">
                            <doughnut
                                v-if="dataLoaded"
                                :projects="sortedProjects"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { DateTime, Duration } from "luxon";
import { getAPI } from "@/axios-base.js";
import Bar from "../components/charts/StackedBar.vue";
import Doughnut from "../components/charts/Doughnut.vue";
import DatePicker from "../components/dashboard/DatePicker.vue";
export default {
    components: { Bar, Doughnut, DatePicker },
    data() {
        return {
            dataLoaded: false,
            projects: {},
            sortedProjects: {},
            timeEntries: {},
            filteredEntries: {},
            dateStart: null,
            dateEnd: null,
            dateLabel: "",
            totalSeconds: 0,
            timeTotalLabel: "",
            topProjectLabel: "",
        };
    },
    computed: {
        token() {
            return this.$store.state.accessToken;
        },
    },
    mounted() {
        this.$wait.start('getData')
        this.getData()
    },
    methods: {
        setDate(dateStart, dateEnd, dateOptionSelected) {
            this.totalSeconds = 0;
            // filter TimeEntries by dates from datepicker
            this.dateStart = dateStart;
            this.dateEnd = dateEnd;
            this.filteredEntries = this.timeEntries;
            let unixStart = dateStart.ts / 1000;
            let unixEnd = dateEnd.ts / 1000;
            this.filteredEntries = this.timeEntries.filter((entry) => {
                return (
                    entry.start_date > unixStart && unixEnd > entry.start_date
                );
            });
            this.sortedProjects = this.getProjectsData(); // sort projects by time
            this.timeTotalLabel = Duration.fromMillis(
                this.totalSeconds * 1000
            ).toFormat("hh:mm:ss"); // set time total label
            // if no entries in given time range, set top project label to
            if (this.totalSeconds) {
                this.topProjectLabel = this.sortedProjects[0].title; // set label to project with the largest duration
            } else {
                this.topProjectLabel = "No project"; // if no entries in given time range, set label to no project
            }

            this.dateLabel = dateOptionSelected;
        },
        getProjectsData() {
            let sortedProjects = JSON.parse(JSON.stringify(this.projects));

            let noProject = { title: "No project", color: "#808080", time: 0 }; //create object to store entries without project
            sortedProjects.map((object) => (object.time = 0)); // add time field to projects object
            // iterate over entries and add time to projects
            for (let entry of this.filteredEntries) {
                if (entry.project) {
                    for (let project of sortedProjects) {
                        if (entry.project === project.id) {
                            this.totalSeconds +=
                                entry.end_date - entry.start_date;
                            project["time"] +=
                                entry.end_date - entry.start_date;
                        }
                    }
                } else {
                    this.totalSeconds += entry.end_date - entry.start_date;
                    noProject.time += entry.end_date - entry.start_date; // add time to antries without project
                }
            }
            // add noProject to projects
            sortedProjects.push(noProject);
            sortedProjects.sort((a, b) => (a.time > b.time ? -1 : 1)); // sort projects by time in seconds
            return sortedProjects;
        },
        getData() {
            // call vuex action to load data
            this.$store.dispatch("getTimeEntries").then(() => {
                this.projects = this.$store.state.projects;
                this.timeEntries = this.$store.state.timeEntries;
                this.$wait.end('getData') // remove waiting state from vuex
                this.dataLoaded = true // show charts
            });
        },
    },
};
</script>

<style>
</style>