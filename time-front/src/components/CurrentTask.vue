<template>
  <div class="panel is-warning mb-2 pt-2">
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
            :project="project"
          />
        </div>
        <div class="column is-1">
          <!-- TAGS -->
          <b-icon icon="tag-multiple" size="is-medium"> </b-icon>
        </div>
        <div class="column is-1">
          <!-- COUNTER -->
          <Counter />
        </div>
        <div class="column is-1">
          <!-- BUTTON -->
          <b-button @click="stopTimer" v-if="isStarted" type="is-primary">STOP</b-button>
          <b-button @click="startTimer" icon-left="progress-clock" v-else type="is-primary">START</b-button>
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
      project: 14,
      projectColor: "",
      searchTerm: "",
      // DURATION DROPDOWN
      duration: "",
      // DATA OBJ
      dataObj: {
        owner: 1,
        description: "",
        project: null,
        tags: [],
        start_date: 1644007667,
        end_date: 1645007667,
      },
    };
  },
  methods: {
    // COMMON
    startTimer() {
        this.isStarted = true;
    }, 
    stopTimer() {
        this.isStarted = false;
        this.saveData()
    },
    saveData(func, toastMessage) {
      this.axios
        .post("http://127.0.0.1:8000/time-entries/create/", this.dataObj)
        .then((response) => {
          if (func) {
            func();
          }
          this.toast(toastMessage);
          /*
          this.dataObj = response.data;
          this.getProject();
          this.getDescription();
          this.getDuration();
           */
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
      if (!(this.dataObj.project == id)) {
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