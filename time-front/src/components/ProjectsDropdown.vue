<template>
    <b-dropdown
        class="projects-dropdown"
        append-to-body
        aria-role="menu"
        scrollable
        max-height="300"
        trap-focus
    >
        <template #trigger>
            <a>
                <b-tooltip
                    position="is-top"
                    :delay="500"
                    label="Create new project or select existing"
                >
                    <b-button
                        :style="projectColor"
                        @click="getProjects"
                        :label="projectName"
                        role="button"
                        v-if="project"
                        class="is-ghost is-size-6"
                        size="is-small"
                    >
                        <b-icon icon="circle-medium"></b-icon>
                        <span>{{projectName}}</span>
                    </b-button>
                    <b-button
                        @click="getProjects"
                        v-else
                        size="is-small"
                        icon-left="plus-circle"
                        class="is-ghost is-size-6"
                        label="Project"
                    />
                </b-tooltip>
            </a>
        </template>
        <b-dropdown-item
            class="btn-open-project-modal"
            @click="showModal"
            aria-role="listitem"
            type="is-primary"
            size="is-medium"
        >
            <b-button icon-left="plus-circle" class="is-ghost" label="Create new project" />
        </b-dropdown-item>

        <b-dropdown-item custom aria-role="listitem">
            <b-input v-model="searchTerm" placeholder="search" expanded />
        </b-dropdown-item>
        <b-dropdown-item
            @click="setProject(project.id)"
            v-for="project of filteredProjects()"
            :key="project.id"
            aria-role="listitem"
            :style="{color: project.color}"
        >
            <div class="is-flex is-align-items-center">
                <b-icon icon="circle-medium"></b-icon>
                <p>{{ project.title }}</p>
            </div>
        </b-dropdown-item>
    </b-dropdown>
</template>

<script>
import { getAPI } from "../axios-base";
import AddProject from "./AddProject.vue";
export default {
    emits: ["ProjectChanged"],
    props: ["project"],
    components: { AddProject },
    data() {
        return {
            projectId: null,
            projectName: "",
            projects: [],
            projectColor: "",
            searchTerm: "",
            addProjectActive: false,
        };
    },
    watch: {
        project: function () {
            this.projectId = this.project;
            this.loadProjects();
        },
    },
    mounted() {
        this.loadProjects();
    },
    methods: {
        showModal() {
            let isMobile = false; // check window size
            if (window.innerWidth < 768) {
                isMobile = true;
            }
            this.$buefy.modal.open({
                parent: this,
                component: AddProject,
                fullScreen: isMobile, // if window < 768px
                hasModalCard: true,
                customClass: "",
                trapFocus: true,
                events: {
                    projectAdded: (project) => this.setProject(project.id),
                },
            });
        },
        setProject(id) {
            if (!(this.project == id)) {
                this.projectId = id;
                this.getProjects();
                console.log("projects dropdwon", this.projects);
                this.$emit("ProjectChanged", id);
            }
        },
        getProjects() {
            // hit API for updated projects, then load projects
            this.$store.dispatch("getProjects").then(() => {
                this.projects = this.$store.state.projects;
                if (this.projectId) {
                    for (let project of this.projects) {
                        if (project.id == this.projectId) {
                            this.projectName = project.title;
                            this.projectColor = `color: ${project.color}`;
                        }
                    }
                }
            });
        },
        loadProjects() {
            // get projects from vuex, select current one
            this.projects = this.$store.state.projects;
            if (this.projectId) {
                for (let project of this.projects) {
                    if (project.id == this.projectId) {
                        this.projectName = project.title;
                        this.projectColor = `color: ${project.color}`;
                    }
                }
            }
        },
        filteredProjects() {
            return this.projects.filter((project) => {
                return project.title
                    .toLowerCase()
                    .includes(this.searchTerm.toLowerCase());
            });
        },
    },
};
</script>

<style>
</style>