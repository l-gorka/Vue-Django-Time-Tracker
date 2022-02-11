<template>
  <b-dropdown
    append-to-body
    aria-role="menu"
    scrollable
    max-height="300"
    trap-focus
  >
    <template #trigger>
      <a
        :style="projectColor"
        @click="loadProjects"
        class="navbar-item"
        role="button"
      >
        <span :style="projectColor" v-if="project" class="is-ghost is-size-6">{{
          projectName
        }}</span
        ><b-button
          v-else
          icon-left="plus-circle"
          class="is-ghost is-size-6"
          label="Project"
        />
      </a>
    </template>
    <b-dropdown-item
      aria-role="listitem"
      type="is-primary"
      size="is-medium"
      custom
      ><b-button
        icon-left="plus-circle"
        class="is-ghost"
        label="Create new project"
        @click="addProjectActive = true"
      />

      <b-modal
        @close="addProjectActive = false"
        :active="addProjectActive"
        has-modal-card
        trap-focus
        :destroy-on-hide="false"
        aria-role="dialog"
        aria-label="Example Modal"
        close-button-aria-label="Close"
        aria-modal
      >
        <template #default="props">
          <AddProject
            @projectAdded="projectAdded($event)"
            @close="props.close"
          ></AddProject>
        </template>
      </b-modal>
    </b-dropdown-item>

    <b-dropdown-item custom aria-role="listitem">
      <b-input v-model="searchTerm" placeholder="search" expanded />
    </b-dropdown-item>

    <b-dropdown-item
      @click="setProject(project.id)"
      v-for="project of filteredProjects()"
      :key="project.id"
      aria-role="listitem"
      >{{ project.title }}</b-dropdown-item
    >
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
    projectAdded(id) {
      this.projectId = id;
      this.getProject();
      this.setProject(id);
    },
    getProject() {
      if (this.projectId) {
        getAPI
          .get("/project-list/" + this.projectId, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then((response) => {
            console.log(response);
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
      getAPI
          .get("/project-list/", {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then((response) => {
            this.projects = response.data
          });
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