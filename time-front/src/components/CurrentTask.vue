<template>
  <div class="panel is-warning mb-4 pt-2 mt-4">
    <div class="panel-body">
      <div
        ref="tEntry"
        class="
          columns
          p-1
          m-0
          is-flex is-align-items-center is-justify-content-between
        "
      >
        <div class="column">
          <!-- DESCRIPTION -->
          <b-input
            placeholder="What are you working on?"
            v-on:keyup.native.enter="$event.target.blur()"
            @focus="copyValue(description)"
            @blur="setDescription"
            v-model="description"
          ></b-input>
        </div>
        <div class="column is-2">
          <!-- PROJECTS DROPDOWN -->
          <ProjectDropdown
            @ProjectChanged="setProject($event)"
            :project="project"
          />
        </div>
        <div class="column is-1">
          <!-- TAGS -->
          <b-icon icon="tag-multiple" size="is-medium"> </b-icon>
        </div>
        <div class="column is-2-fullhd is-6-mobile is-2-desktop">
          <!-- COUNTER -->
          <Counter
            @counterStopped="counterStopped"
            :isCounterStarted="isStarted"
          />
        </div>
        <div class="column is-1 is-flex is-justify-content-end">
          <!-- BUTTON -->
          <b-button
            @click="stopTimer"
            v-if="isStarted"
            icon-left="clock-outline"
            type="is-primary"
            >STOP</b-button
          >
          <b-button
            @click="startTimer"
            v-else
            icon-left="clock-outline"
            type="is-primary"
            >START</b-button
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProjectDropdown from "../components/ProjectsDropdown.vue";
import Counter from "../components/Counter.vue";
export default {
  components: { ProjectDropdown, Counter },
  data() {
    return {
      // COMMON
      tempValue: null,
      addProjectActive: false,
      isStarted: false,
      // DESCRIPTIONganularity
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
        owner: 1,
        description: "",
        project: null,
        tags: [2],
        start_date: null,
        end_date: null,
      },
    };
  },
  methods: {
    // COMMON
    startTimer() {
      this.dataObj.start_date = Date.parse(new Date()) / 1000;

      this.isStarted = true;
    },
    stopTimer() {
      this.isStarted = false;
    },
    counterStopped(e) {
      this.dataObj.end_date = this.dataObj.start_date + e;
      this.saveData(null, "Time entry has been created");
      
    },
    saveData(func, toastMessage) {
      this.axios
        .post("http://127.0.0.1:8000/time-entry-create/", this.dataObj)
        .then((response) => {
          if (func) {
            func();
          }
          console.log(response.data)
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