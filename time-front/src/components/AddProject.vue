<template>
    <div class="modal-card" style>
        <header class="modal-card-head">
            <h2 class="modal-card-title">Create new project</h2>
        </header>
        <section class="modal-card-body">
            <div class="columns">
                <div class="column">
                    <b-field v-if="title" label="Project name">
                        <b-input @keyup.native.enter="createProject" v-model="projectData.title"></b-input>
                    </b-field>
                    <b-field
                        v-else
                        label="Project name"
                        type="is-danger"
                        message="Please enter project name"
                    >
                        <b-input @input="title = !title" v-model="projectData.title"></b-input>
                    </b-field>
                    <b-field label="Pick up a color">
                        <div class="form__input">
                            <v-swatches inline v-model="projectData.color"></v-swatches>
                        </div>
                    </b-field>
                </div>
            </div>
        </section>
        <footer class="modal-card-foot">
            <b-button label="Close" @click="$emit('close')" />
            <b-button
                
                @click="createProject"
                :label="projectID ? 'Update project' : 'Create project' "
                type="is-primary"
            />
        </footer>
    </div>
</template>

<script>
import { getAPI } from "../axios-base";
import 'vue-swatches/dist/vue-swatches.css';
import VSwatches from 'vue-swatches';
export default {
    props: ["projectID", "projectTitle", "projectColor"],
    components: {
        VSwatches
    },
    emits: ["close"],
    mounted() {
        if (this.projectID && this.projectTitle && this.projectColor) {
            this.projectData.title = this.projectTitle
            this.projectData.color = this.projectColor
        }
    },
    data() {
        return {
            projectData: {
                owner: null,
                title: "",
                color: "#000000",
            },
            title: true,
        };
    },
    methods: {
        createProject() {
            this.projectData.owner = this.$store.state.userID // set owner to current user
            if (!(this.projectData.title)) {    // if title input is empty show error message on input
                this.title = false
                return null
            }
            if (this.projectID) {
                // if ID passed as prop, update existing project
                getAPI
                    .post(`project-list/${this.projectID}/update/`, this.projectData, {
                        headers: {
                            Authorization: `Bearer ${this.$store.state.accessToken}`,
                        },
                    })
                    .then((response) => {
                        this.$emit("projectAdded", response.data);
                        this.$emit("close");
                        this.toast("Project has been updated");
                    });
            } else {
                // if no ID passed, just create project
                getAPI
                    .post("/project-create/", this.projectData, {
                        headers: {
                            Authorization: `Bearer ${this.$store.state.accessToken}`,
                        },
                    })
                    .then((response) => {
                        this.$emit("projectAdded", response.data);
                        this.$emit("close");
                        this.toast("Project has been created");
                    });
            }
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
</style>