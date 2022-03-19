<template>
    <div
        ref="tEntry"
        class="time-entry has-background-white panel-block columns is-multiline py-0 px-1 m-0 is-flex is-align-items-center"
    >
        <div class="column is-12-mobile">
            <!-- DESCRIPTION -->
            <b-input
                class="desc-input"
                placeholder="Add description."
                v-on:keyup.native.enter="$event.target.blur()"
                @focus="copyValue(description)"
                @blur="setDescription"
                v-model="description"
            ></b-input>
        </div>
        <div
            class="column is-12-mobile is-3-desktop is-flex is-justify-content-space-between is-align-items-center"
        >
            <!-- PROJECTS DROPDOWN AND CALENDAR DROPDOWN -->
            <ProjectDropdown @ProjectChanged="setProject($event)" :project="dataObj.project" />
            <b-tooltip position="is-top" :delay="200" label="Set date">
                <CalendarDropdown
                    @dateChanged="dateChanged"
                    v-if="dataObj.start_date"
                    :timestamp="dataObj.start_date"
                />
            </b-tooltip>
        </div>

        <!-- TIME STARTED -->
        <div class="column is-6-mobile is-2-tablet is-1-widescreen">
            <TimeInput
                class="time-input-start"
                @timeChanged="setStartTime($event)"
                v-if="dataObj.start_date"
                :timestamp="dataObj.start_date"
            />
        </div>
        <!-- TIME ENDED -->
        <div class="column is-6-mobile is-2-tablet is-1-widescreen">
            <TimeInput
                class="time-input-end"
                @timeChanged="setEndTime($event)"
                v-if="dataObj.end_date"
                :timestamp="dataObj.end_date"
            />
        </div>

        <div class="column is-2-tablet is-1-widescreen">
            <!-- DURATION DROPDOWN -->
            <button class="button is-ghost has-text-black" slot="trigger">
                <span class="is-size-4">{{ duration }}</span>
            </button>
        </div>
        <div
            class="options column level is-flex is-justify-content-space-evenly is-justify-content-center-desktop is-1"
        >
            <!-- OPTIONS -->
            <b-tooltip position="is-left" :delay="200" label="Continue timer for this activity">
                <b-button
                    class="btn-continue"
                    @click="continueActivity"
                    type="is-ghost"
                    size="is-small"
                >
                    <b-icon icon="play-circle" class="is-size-4"></b-icon>
                </b-button>
            </b-tooltip>
            <b-tooltip position="is-left" :delay="200" label="Delete time entry">
                <b-button
                    class="btn-delete"
                    @click="deleteTimeEntry"
                    type="is-ghost"
                    size="is-small"
                >
                    <b-icon icon="delete" class="is-size-4"></b-icon>
                </b-button>
            </b-tooltip>
        </div>
    </div>
</template>

<script>
import { getAPI } from "../../axios-base";
import AddProject from "../common/AddProject.vue";
import TimeInput from "./TimeInput.vue";
import ProjectDropdown from "../common/ProjectsDropdown.vue";
import CalendarDropdown from "./CalendarDropdown.vue";
export default {
    emits: ["dataChanged"],
    components: { AddProject, TimeInput, ProjectDropdown, CalendarDropdown },
    props: ["timeEntryID"],
    created() {},
    mounted() {
        this.loadData();
    },

    data() {
        return {
            // COMMON
            dataObj: {},
            tempValue: null,
            addProjectActive: false,
            // DESCRIPTION
            description: "",
            // TIME INPUTS
            // PROJECTS DROPDOWN
            projects: [],
            project: "",
            projectColor: "",
            searchTerm: "",
            // DURATION DROPDOWN
            duration: "",
        };
    },
    methods: {
        // COMMON
        loadData() {
            let storeEntries = this.$store.state.timeEntries;
            for (let entry of storeEntries) {
                if (entry.id == this.timeEntryID) {
                    this.dataObj = entry;
                }
                this.getDescription();
                this.getDuration();
            }
        },
        saveData(func, toastMessage) {
            getAPI
                .post(
                    `time-entries/${this.timeEntryID}/update/`,
                    this.dataObj,
                    {
                        headers: {
                            Authorization: `Bearer ${this.$store.state.accessToken}`,
                        },
                    }
                )
                .then((response) => {
                    if (func) {
                        func();
                    }
                    this.toast(toastMessage);
                    this.$emit("dataChanged");
                })
                .catch((error) => {
                    console.log(error.data);
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
                this.saveData(this.getDescription, toastMessage);
            }
        },

        // PROJECTS DROPDOWN
        setProject(id) {
            let toastMessage = "Project has been updated.";
            if (!(this.dataObj.project == id)) {
                this.dataObj.project = id;
                this.saveData(null, toastMessage);
            }
        },
        // CALENDAR DROPDOWN
        dateChanged(dateDifferenceSeconds) {
            this.dataObj.start_date += dateDifferenceSeconds;
            this.dataObj.end_date += dateDifferenceSeconds;
            this.saveData(this.getDuration, "Entry date has been updated");
        },
        // DURATION DROPDOWN
        focusOnDuration(event) {
            this.tempValue = this.duration;
        },
        getDuration() {
            let timeDiff = this.dataObj.end_date - this.dataObj.start_date;
            let dHours = Math.floor(timeDiff / 60 / 60);
            timeDiff -= dHours * 60 * 60;
            let dMinutes = Math.floor(timeDiff / 60);
            timeDiff -= dMinutes * 60;
            let dSeconds = timeDiff;
            this.duration =
                dHours +
                ":" +
                ("00" + dMinutes).slice(-2) +
                ":" +
                ("00" + dSeconds).slice(-2);
        },
        // TIME INPUTS
        setStartTime(e) {
            this.dataObj.start_date = e;
            // If time entry passing the midnight, set end_date to the next day by adding 86400 seconds = 24 hours.
            if (this.dataObj.start_date > this.dataObj.end_date) {
                console.log(
                    "set start time",
                    this.dataObj.start_date,
                    this.dataObj.end_date
                );
                this.dataObj.end_date += 86400;
            }
            // Check if there is more than 24h difference between dates, if so, set end_date to the day before by substraction 86400 seconds.
            if (this.dataObj.end_date - this.dataObj.start_date > 86400) {
                console.log(
                    "set start time2",
                    this.dataObj.start_date,
                    this.dataObj.end_date
                );
                this.dataObj.end_date -= 86400;
            }
            this.saveData(this.getDuration, "Start time has been updated");
        },
        setEndTime(e) {
            this.dataObj.end_date = e;
            // If time entry passing the midnight, set end_date to the next day by adding 86400 seconds = 24 hours.
            if (this.dataObj.start_date > this.dataObj.end_date) {
                console.log(
                    "set start time3",
                    this.dataObj.start_date,
                    this.dataObj.end_date
                );
                this.dataObj.end_date += 86400;
            }
            // Check if there is more than 24h difference between dates, if so, set end_date to the day before by substraction 86400 seconds.
            //this.saveData(this.getDuration, "Start time has been updated");
            if (this.dataObj.end_date - this.dataObj.start_date > 86400) {
                console.log(
                    "set start time4",
                    this.dataObj.start_date,
                    this.dataObj.end_date
                );
                this.dataObj.end_date -= 86400;
            }
            this.saveData(this.getDuration, "End time has been updated");
        },
        // HELPERS
        continueActivity() {
            this.$store.commit("updateContinueTask", this.dataObj);
        },
        deleteTimeEntry() {
            this.$buefy.dialog.confirm({
                title: "Deleting entry",
                message:
                    "Are you sure you want to <b>delete</b> this entry? This action cannot be undone.",
                confirmText: "Delete Entry",
                type: "is-danger",
                hasIcon: true,
                onConfirm: () => {
                    getAPI
                        .post(
                            `time-entries/${this.timeEntryID}/delete/`,
                            null,
                            {
                                headers: {
                                    Authorization: `Bearer ${this.$store.state.accessToken}`,
                                },
                            }
                        )
                        .then((response) => {
                            this.toast("Time entry has been deleted");
                            this.$emit("dataChanged");
                        })
                        .catch((error) => {
                            console.log(error.data);
                        });
                },
            });
        },
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
#play {
    display: flex;
    justify-content: center;
}
</style>