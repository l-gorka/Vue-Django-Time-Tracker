<template>
    <div class="panel is-warning mb-4 pt-2 mt-4 mx-2">
        <div class="panel-body">
            <div
                ref="tEntry"
                class="columns is-multiline p-1 m-0 is-flex is-align-items-center is-justify-content-between"
            >
                <div class="column is-12-mobile">
                    <!-- DESCRIPTION -->
                    <b-input
                        placeholder="What are you working on?"
                        v-on:keyup.native.enter="$event.target.blur()"
                        @focus="copyValue(description)"
                        @blur="setDescription"
                        v-model="description"
                    ></b-input>
                </div>
                <div class="column is-12-mobile is-2">
                    <!-- PROJECTS DROPDOWN -->
                    <ProjectDropdown @ProjectChanged="setProject($event)" :project="project" />
                </div>
                <div class="column is-2-fullhd is-2-desktop">
                    <!-- COUNTER -->
                    <Counter
                        @counterStopped="counterStopped"
                        :isCounterStarted="isStarted"
                        :counterTimeSeconds="counterSeconds"
                    />
                </div>
                <div class="column is-1 is-flex is-justify-content-end">
                    <!-- BUTTON -->
                    <b-button
                        @click="stopTimer"
                        v-if="isStarted"
                        icon-left="clock-outline"
                        type="is-primary"
                    >STOP</b-button>
                    <b-button
                        @click="startTimer"
                        v-else
                        icon-left="clock-outline"
                        type="is-primary"
                    >START</b-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from "../axios-base";
import ProjectDropdown from "../components/ProjectsDropdown.vue";
import Counter from "../components/Counter.vue";
export default {
    components: { ProjectDropdown, Counter },
    data() {
        return {
            // COMMON
            counterSeconds: 0,
            tempValue: null,
            addProjectActive: false,
            isStarted: false,
            // DESCRIPTION
            description: "",
            // TIME INPUTS
            // PROJECTS DROPDOWN
            projects: [],
            project: null,
            projectColor: "",
            searchTerm: "",
            // DURATION DROPDOWN
            duration: "",
            // DATA OBJ
            dataObj: {
                owner: this.$store.state.userID,
                description: "",
                project: null,
                tags: [],
                start_date: null,
                end_date: null,
            },
        };
    },
    // if cookie with start_date is present, set counter to this date
    mounted() {
        let cookie = this.$store.state.taskStarted
        if (cookie) {
            this.counterSeconds = (Date.parse(new Date()) / 1000) - cookie
            console.log('conter sec', this.counterSeconds)
            this.startTimer()
        }
    },
    computed: {
        // if updateContinueTask is called, return dataObj
        storeContinue() {
            return this.$store.state.continueTask
        }
    },
    watch: {
        // updateContinueTask is called, set description and project, then start timer
        storeContinue() {
            if (this.storeContinue && !(this.isStarted)) {
                this.description = this.storeContinue.description
                this.project = this.storeContinue.project
                this.dataObj.description = this.storeContinue.description
                this.dataObj.project = this.storeContinue.project
                this.startTimer()
                this.$store.commit('deleteContinueTask')    // delete dataObj from store
            }

        }
    },
    methods: {
        // COMMON
        startTimer() {
            let cookie = this.$store.state.taskStarted
            this.dataObj.start_date = Date.parse(new Date()) / 1000
            if (!(cookie)) {    // set new cookie if not present
                this.$store.commit('updateTaskStarted', this.dataObj.start_date)
            }

            if (this.counterSeconds) { // add seconds from cookie
                this.dataObj.start_date += this.counterSeconds
            }
            this.isStarted = true;
            this.toast('Timer has been started')

        },
        stopTimer() {
            this.isStarted = false;
        },
        // Called to save TimeEntry.
        counterStopped(e) {
            this.counterSeconds = 0
            this.$store.dispatch('removeTaskStarted')
            this.dataObj.end_date = this.dataObj.start_date + e;
            this.saveData(null, "Time entry has been created");
            this.project = null;
            this.description = null;
            this.dataObj = {  // Reset counter and all inputs.
                owner: this.$store.state.userID,
                description: "",
                project: null,
                tags: [],
                start_date: null,
                end_date: null,
            };
        },
        // Save data, emit signal to update TimeEntries.
        saveData(func, toastMessage) {
            getAPI
                .post("/time-entry-create/", this.dataObj, {
                    headers: {
                        Authorization: `Bearer ${this.$store.state.accessToken}`,
                    },
                })
                .then((response) => {
                    if (func) { // If function to update values is passed, call it.
                        func();
                    }
                    this.$emit("timeEntryCreated", response.data.id);
                    this.toast(toastMessage);
                });
        },
        // DESCRIPTION
        getDescription() {
            this.description = this.dataObj.description;
        },
        setDescription() {
            let toastMessage = "Description has been updated.";
            if (!(this.tempValue == this.description)) {
                this.dataObj.description = this.description;
            }
        },
        // PROJECT DROPDOWN
        setProject(id) {
            let toastMessage = "Project has been updated.";
            if (!(this.project == id)) {
                this.project = id;
                this.dataObj.project = id;
            }
        },
        // HELPERS
        copyValue(value) {
            this.tempValue = value;
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