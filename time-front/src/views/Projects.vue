<template>
    <div class="container is-fluid mt-5">
        <div class="level">
            <!-- TITLE -->
            <div class="level-left">
                <div class="level-item">
                    <div class="title has-text-primary">
                        <span>Projects</span>
                    </div>
                </div>
            </div>
            <div class="level-right">
                <div class="level-item"></div>
            </div>
        </div>
        <div class="columns is-multiline">
            <div class="column is-4">
                <!-- PROJECTS MENU -->
                <b-collapse
                    aria-id="contentIdForA11y2"
                    class="panel is-shadowless is-primary has-background-white"
                    animation="slide"
                    icon="account"
                    v-model="dropdownOpen"
                    v-if="projectsLoaded && entriesLoaded"
                >
                    <template #trigger>
                        <div
                            class="panel-heading mb-2 is-flex is-justify-content-space-between"
                            role="button"
                            aria-controls="contentIdForA11y2"
                        >
                            <span class>Select project</span>
                            <b-icon icon="menu-down"></b-icon>
                        </div>
                    </template>
                    <div class="panel-block">
                        <b-button
                            @click="showAddProjectModal"
                            icon-left="plus-circle"
                            class="is-ghost"
                            label="Create new project"
                        />
                    </div>
                    <div class="panel-block">
                        <b-input icon="magnify" v-model="searchTerm" placeholder="search" expanded />
                    </div>
                    <a
                        @click="selectProject(project)"
                        v-for="project in filteredProjects()"
                        :key="project.id"
                        class="panel-block is-flex is-justify-content-space-between"
                    >
                        <div :style="{color: project.color}" class="is-flex has-text-weight-normal">
                            <b-icon icon="circle-medium"></b-icon>
                            <p class>{{project.title}}</p>
                        </div>
                        <div>
                            <p class="is-family-primary">{{ displayTime(project.time_total) }}</p>
                        </div>
                    </a>
                </b-collapse>
            </div>
            <div v-if="selectedProject" class="column is-8">
                <div class="level">
                    <!-- PROJECT TITLE -->
                    <div class="level-left">
                        <div class="level-item">
                            <div class="title">
                                <span
                                    :style="{color: selectedProject.color}"
                                >{{selectedProject.title}}</span>
                            </div>
                        </div>
                    </div>
                    <div class="level-right">
                        <div class="level-item">
                            <div class="title is-flex is-justify-content-space-evenly">
                                <b-button class="mr-2" outlined type="is-primary" size="is-medium">
                                    <b-icon icon="circle-edit-outline" class="is-size-4"></b-icon>
                                    <span>Edit</span>
                                </b-button>
                                <b-button outlined type="is-primary" size="is-medium">
                                    <b-icon icon="delete" class="is-size-4"></b-icon>
                                    <span>Delete</span>
                                </b-button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="columns is-multiline">
                    <!-- BOXES -->
                    <div class="column">
                        <div class="columns is-multiline">
                            <div class="column is-half">
                                <div class="box notification is-primary">
                                    <div class="heading">Nubmer of entries</div>
                                    <div class="title">{{selectedProject.time_entries.length }}</div>
                                </div>
                            </div>
                            <div class="column is-half">
                                <div class="box notification is-primary">
                                    <div class="heading">Time total</div>
                                    <div class="title">{{ displayTime(selectedProject.time_total) }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-full">
                        <div class="message">
                            <!-- CHART -->
                            <div class="message-header is-flex is-justify-content-space-between">
                                <span>Timeline</span>
                                <date-picker />
                            </div>
                            <div class="message-body">
                                <project-bar
                                    v-if="filteredEntries"
                                    :entries="filteredEntries"
                                    :color="selectedProject.color"
                                    :project="selectedProject.title"
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
import { Duration } from "luxon";
import DatePicker from "../components/dashboard/DatePicker.vue";
import ProjectBar from '../components/charts/ProjectBar.vue'
import AddProject from '../components/AddProject.vue'
export default {
    components: { DatePicker, ProjectBar, AddProject },
    mounted() {
        this.getProjects();
        this.getEntries()
        this.isMobile()

    },
    data() {
        return {
            dropdownOpen: true,
            projectsLoaded: false,
            entriesLoaded: false,
            projects: {},
            searchTerm: "",
            selectedProject: null,
            entries: {},
            filteredEntries: [],
        };
    },
    methods: {
        selectProject(project) {
            this.selectedProject = project
            if (window.innerWidth < 768) {
                this.dropdownOpen = false
            }
            this.filteredEntries = this.entries.filter((entry) => {
                return entry.project == this.selectedProject.id
            })

        },
        getProjects() {
            this.$store.dispatch("getProjects").then(() => {
                this.projects = this.$store.state.projects;
                this.projectsLoaded = true
            });
        },
        getEntries() {
            this.$store.dispatch('getTimeEntries').then(() => {
                this.entries = this.$store.state.timeEntries
                this.entriesLoaded = true
            })
        },
        isMobile() {
            if (window.innerWidth < 768) {
                console.log('is mobile')
                this.dropdownOpen = false;
            }
        },
        displayTime(seconds) {
            return Duration.fromMillis(seconds * 1000).toFormat("hh:mm:ss");
        },
        filteredProjects() {
            return this.projects.filter((project) => {
                return project.title
                    .toLowerCase()
                    .includes(this.searchTerm.toLowerCase());
            });
        },
        showAddProjectModal() {
            let isMobile = false // check window size
            if (window.innerWidth < 768) {
                isMobile = true
            }
            this.$buefy.modal.open({
                parent: this,
                component: AddProject,
                fullScreen: isMobile, // if window < 768px 
                hasModalCard: true,
                customClass: "",
                trapFocus: true,
                events: {
                    projectAdded: () => this.getProjects(),
                },
            });
        },
        setDate() { },
    },
};
</script>

<style>
</style>