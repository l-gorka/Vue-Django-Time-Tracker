<template>
    <div class="container is-fluid mt-5">
        <div class="level">
            <div class="level-left">
                <div class="level-item">
                    <div class="title">
                        <b-icon icon="view-dashboard" size="is-small"></b-icon>
                        <span>Projects</span>
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
            <div class="column">
                <div class="panel is-success is-light has-background-white">
                    <p class="panel-heading mb-2">Projects</p>
                    <div class="panel-block">
                        <b-button
                            icon-left="plus-circle"
                            class="is-ghost"
                            label="Create new project"
                        />
                    </div>
                    <div class="panel-block">
                        <b-input icon="magnify" v-model="searchTerm" placeholder="search" expanded />
                    </div>
                    <a
                        v-for="project in projects"
                        :key="project.id"
                        class="panel-block is-flex is-justify-content-space-between"
                    >
                        <div :style="{color: project.color}" class="is-flex has-text-weight-normal">
                            <b-icon icon="circle-medium"></b-icon>
                            <p  class>{{project.title}}</p>
                        </div>
                        <div>{{ displayTime(project.time_total) }}</div>
                    </a>
                </div>
            </div>
            <div class="column is-8 has-background-info-light"></div>
        </div>
    </div>
</template>

<script>
import { Duration } from "luxon";
import { getAPI } from "@/axios-base.js";
import DatePicker from "../components/dashboard/DatePicker.vue";
export default {
    components: { DatePicker },
    mounted() {
        this.getProjects();
    },
    computed: {
        projectsObj() {
            return this.$store.state.projects;
        },
    },
    data() {
        return {
            isLoaded: false,
            projects: {},
            searchTerm: "",
            columns: [
                {
                    field: "title",
                    label: "Title",
                },
                {
                    field: "time_total",
                    label: "Time total",
                },
            ],
        };
    },
    methods: {
        getProjects() {
            this.$store.dispatch("getProjects").then(() => {
                this.projects = this.$store.state.projects;
            });
        },
        displayTime(seconds) {
            return Duration.fromMillis(seconds * 1000).toFormat("hh:mm:ss");
        },
        setDate() { },
    },
};
</script>

<style>
</style>