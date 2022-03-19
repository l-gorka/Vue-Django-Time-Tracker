<template>
    <div class="page-wrapper mt-5">
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
            <div class="column is-12-tablet is-4-desktop">
                <!-- PROJECTS MENU -->
                <b-collapse
                    aria-id="contentIdForA11y2"
                    class="panel cy-panel-select-project is-shadowless is-primary has-background-white"
                    animation="slide"
                    icon="account"
                    v-model="dropdownOpen"
                    v-if="dataLoaded"
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
                            @click="showAddProjectModal(edit=false)"
                            icon-left="plus-circle"
                            class="is-ghost"
                            label="Create new project"
                        />
                    </div>
                    <div class="panel-block">
                        <b-input class="cy-input-search" icon="magnify" v-model="searchTerm" placeholder="search" expanded />
                    </div>
                    <div id="projects-menu">
                        <a
                            @click="selectProject(project)"
                            v-for="project in filteredProjects()"
                            :key="project.id"
                            class="panel-block is-flex is-justify-content-space-between"
                        >
                            <div
                                :style="{color: project.color}"
                                class="is-flex cy-project-colored has-text-weight-normal"
                            >
                                <b-icon icon="circle-medium"></b-icon>
                                <p class>{{project.title}}</p>
                            </div>
                            <div>
                                <p class="is-family-primary">{{ displayTime(project.time_total) }}</p>
                            </div>
                        </a>
                    </div>
                </b-collapse>
            </div>
            <div
                v-if="selectedProject"
                class="cy-selected-project column is-12-tablet is-8-desktop"
            >
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
                                <b-button
                                    @click="showAddProjectModal(edit=true)"
                                    class="mr-2 cy-btn-edit"
                                    type="is-primary"
                                    icon-left="circle-edit-outline"
                                    label="Edit"
                                ></b-button>
                                <b-button
                                    @click="deleteProject"
                                    class="cy-btn-delete"
                                    type="is-primary"
                                    icon-left="delete"
                                    label="Delete"
                                >
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
                                <div class="box cy-box-total-entries notification is-primary">
                                    <div class="heading">Nubmer of entries</div>
                                    <div class="title">{{selectedProject.time_entries.length }}</div>
                                </div>
                            </div>
                            <div class="column is-half">
                                <div class="box cy-box-total-time notification is-primary">
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
                                <b-icon icon="chart-box-outline"></b-icon>
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
            <div v-else class="column is-12-tablet is-8-desktop">
                <div class="message">
                    <div class="message-header is-flex is-justify-content-space-between">
                        <span>No project selected</span>
                        <b-icon icon="chart-box-outline"></b-icon>
                    </div>
                    <div class="message-body m-6">
                        <div class="hero is-halfheight">
                            <div class="hero-body">
                                <div class="container has-text-centered">
                                    <p class="title muted">No project selected</p>
                                </div>
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
import { getAPI } from "../axios-base";
import DatePicker from "../components/dashboard/DatePicker.vue";
import ProjectBar from "../components/charts/ProjectBar.vue";
import AddProject from "../components/AddProject.vue";
export default {
    components: { DatePicker, ProjectBar, AddProject },
    mounted() {
        this.$wait.start("getData");
        this.getData();
        this.isMobile();
    },
    data() {
        return {
            dropdownOpen: true,
            dataLoaded: false,
            projects: {},
            searchTerm: "",
            selectedProject: null,
            entries: {},
            filteredEntries: [],
        };
    },
    methods: {
        selectProject(project) {
            // after selecting project, hide projects dropdown on mobile
            this.selectedProject = project;
            if (window.innerWidth < 1024) {
                this.dropdownOpen = false;
            }
            this.filteredEntries = this.entries.filter((entry) => {
                // select project to be displayed
                return entry.project == this.selectedProject.id;
            });
        },
        getData() {
            // call vuex action to load data
            this.$store.dispatch("getTimeEntries").then(() => {
                this.projects = this.$store.state.projects;
                this.entries = this.$store.state.timeEntries;
                this.$wait.end("getData"); // remove waiting state from vuex
                this.dataLoaded = true; // show projects menu
            });
        },
        isMobile() {
            // if mobile, project dropdown should be hidden by default
            if (window.innerWidth < 1024) {
                console.log("is mobile");
                this.dropdownOpen = false;
            }
        },
        displayTime(seconds) {
            // display timestamp in format readable by humans
            return Duration.fromMillis(seconds * 1000).toFormat("hh:mm:ss");
        },
        filteredProjects() {
            // filter project by name
            return this.projects.filter((project) => {
                return project.title
                    .toLowerCase()
                    .includes(this.searchTerm.toLowerCase());
            });
        },
        showAddProjectModal(edit) {
            // fire modal to add project
            let isMobile = false; // check window size
            if (window.innerWidth < 768) {
                isMobile = true;
            }
            let props = {};
            // if
            if (edit) {
                props = {
                    projectID: this.selectedProject.id,
                    projectTitle: this.selectedProject.title,
                    projectColor: this.selectedProject.color,
                    showUpdateModal: true,
                };
            }
            this.$buefy.modal.open({
                parent: this,
                props: props,
                component: AddProject,
                fullScreen: isMobile, // if window < 768px
                hasModalCard: true,
                customClass: "",
                trapFocus: true,
                events: {
                    projectAdded: (project) => {
                        // if project added, call store action for list of projects
                        this.getData();
                        this.selectedProject = project;
                    },
                },
            });
        },
        deleteProject() {
            // open dialog for confirmation
            this.$buefy.dialog.confirm({
                customClass: "cy-delete-prompt",
                title: "Deleting project",
                message:
                    "Are you sure you want to <b>delete</b> this project? This action cannot be undone.",
                confirmText: "Delete Project",
                type: "is-danger",
                hasIcon: true,
                // if confirmed, hit API with project ID
                onConfirm: () => {
                    getAPI
                        .post(
                            `project-list/${this.selectedProject.id}/delete/`,
                            null,
                            {
                                headers: {
                                    Authorization: `Bearer ${this.$store.state.accessToken}`,
                                },
                            }
                        )
                        .then((response) => {
                            this.toast("Project has been deleted");
                            this.getData();
                            this.selectedProject = null;
                        })
                        .then((error) => console.log(error));
                },
            });
        },
        toast(toastMessage) {
            this.$buefy.toast.open({
                duration: 5000,
                message: toastMessage,
                position: "is-bottom",
                type: "is-success",
            });
        },
    },
};
</script>

<style>
#projects-menu {
    max-height: 50vh;
    overflow-y: auto;
}
.level-left {
    flex-shrink: 1;
}
.level-item {
    flex-shrink: 1;
}
</style>