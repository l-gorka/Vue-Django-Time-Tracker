<template>
  <div ref="tEntry" class="columns py-0 px-1 m-0 is-flex is-align-items-center">
    <div class="column is-4">
      <!-- DESCRIPTION -->
      <b-input
        placeholder="Add description."
        v-on:keyup.native.enter="$event.target.blur()"
        @focus="copyValue(description)"
        @blur="setDescription"
        v-model="description"
      ></b-input>
    </div>
    <div class="column is-3">
      <!-- PROJECTS DROPDOWN -->
      <ProjectDropdown
        @ProjectChanged="setProject($event)"
        :project="dataObj.project"
      />
    </div>
    <div class="column is-1">
      <!-- TAGS -->
      <b-icon icon="tag-multiple" size="is-medium"> </b-icon>
    </div>

    <!-- TIME STARTED -->
    <div class="column is-1">
      <TimeInput
        @timeChanged="setStartTime($event)"
        v-if="dataObj.start_date"
        :timestamp="dataObj.start_date"
      />
    </div>
    <!-- TIME ENDED -->
    <div class="column is-1">
      <TimeInput
        @timeChanged="setEndTime($event)"
        v-if="dataObj.end_date"
        :timestamp="dataObj.end_date"
      />
    </div>

    <div class="column is-1">
      <!-- DURATION DROPDOWN -->
      <b-dropdown ref="dropdown">
        <button class="button is-ghost has-text-black" slot="trigger">
          <span class="is-size-4">{{ duration }}</span>
        </button>
        <b-dropdown-item custom
          ><b-input
            @focus="focusOnDuration($event)"
            v-model="duration"
          ></b-input
        ></b-dropdown-item>
      </b-dropdown>
    </div>
    <div class="column level is-flex is-1">
      <!-- OPTIONS -->
      <b-icon icon="play" size="is-medium"></b-icon>
      <b-icon id="play" icon="dots-vertical" size="is-medium"> </b-icon>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-base";
import AddProject from "../components/AddProject.vue";
import TimeInput from "../components/TimeInput.vue";
import ProjectDropdown from "../components/ProjectsDropdown.vue";
export default {
  emits: ['dataChanged'],
  components: { AddProject, TimeInput, ProjectDropdown },
  props: ["canCancel", "timeEntryID"],
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
      getAPI
        .get(`time-entries/${this.timeEntryID}`, {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
        .then((response) => {
          
          this.dataObj = response.data;
          this.getDescription();
          this.getDuration();
        });
      
    },
    saveData(func, toastMessage) {
      console.log(this.dataObj)
      getAPI
        .post(`time-entries/${this.timeEntryID}/update/`, this.dataObj, {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          }
        })
        .then((response) => {
          if (func) {
            func();
          }
          this.toast(toastMessage);
          this.$emit('dataChanged')
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
      this.duration = dHours + ":" + ('00' + dMinutes).slice(-2) + ":" + ('00' + dSeconds).slice(-2);
    },
    // TIME INPUTS
    setStartTime(e) {
      this.dataObj.start_date = e;
      // If time entry passing the midnight, set end_date to the next day by adding 86400 seconds = 24 hours.
      if (this.dataObj.start_date > this.dataObj.end_date) {
        this.dataObj.end_date += 86400
      }
      // Check if there is more than 24h difference between dates, if so, set end_date to the day before by substraction 86400 seconds. 
      this.saveData(this.getDuration, "Start time has been updated");
      if (this.dataObj.end_date - this.dataObj.start_date > 86400) {
        this.dataObj.end_date -= 86400
      }
    },
    setEndTime(e) {
      this.dataObj.end_date = e;
      // If time entry passing the midnight, set end_date to the next day by adding 86400 seconds = 24 hours.
      if (this.dataObj.start_date > this.dataObj.end_date) {
        this.dataObj.end_date += 86400
      }
      // Check if there is more than 24h difference between dates, if so, set end_date to the day before by substraction 86400 seconds. 
      this.saveData(this.getDuration, "Start time has been updated");
      if (this.dataObj.end_date - this.dataObj.start_date > 86400) {
        this.dataObj.end_date -= 86400
      }
      this.saveData(this.getDuration, "End time has been updated");
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
#play {
  display: flex;
  justify-content: center;
}
</style>