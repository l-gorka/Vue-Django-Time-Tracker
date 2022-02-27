<template>
    <b-dropdown append-to-body aria-role="menu" scrollable max-height="300" trap-focus>
        <template #trigger>
            <a :style="projectColor" @click="loadProjects" class="navbar-item p-0" role="button">
                <span
                    :style="projectColor"
                    v-if="project"
                    class="is-ghost is-size-6"
                >{{projectName}}</span>
                <b-button
                    v-else
                    size="is-small"
                    icon-left="plus-circle"
                    class="is-ghost is-size-6"
                    label="Project"
                />
            </a>
        </template>
        <b-dropdown-item aria-role="listitem" type="is-primary" size="is-medium">
            <b-button
                icon-left="plus-circle"
                class="is-ghost"
                label="Create new project"
                @click="showModal"
            />
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
        >{{ project.title }}</b-dropdown-item>
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
            this.getProject();
        },
    },

    methods: {
        showModal() {
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
                    projectAdded: (project) => this.setProject(project.id),
                },
            });
        },
        projectAdded(id) {
            this.projectId = id;
            this.getProject();
            this.setProject(id);
        },
        getProject() {
            this.projects = this.$store.state.projects
            if (this.projectId) {
                for (let project of this.projects) {
                    if (project.id == this.projectId) {
                        this.projectName = project.title
                        this.projectColor = `color: ${project.color}`
                    }
                 }
            }
        },
        getProject2() {
            if (this.projectId) {
                getAPI
                    .get("/project-list/" + this.projectId, {
                        headers: {
                            Authorization: `Bearer ${this.$store.state.accessToken}`,
                        },
                    })
                    .then((response) => {
                        this.projectName = response.data.title;
                        this.projectColor = `color: ${response.data.color}`;
                    });
            }
        },
        setProject(id) {
            if (!(this.project == id)) {
                this.$emit("ProjectChanged", id);
                this.projectId = id;
                this.loadProjects();
                this.getProject();
            }
        },
        loadProjects() {
            this.projects = this.$store.state.projects
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