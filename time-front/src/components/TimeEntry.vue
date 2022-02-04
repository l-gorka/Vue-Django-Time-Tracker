<template>
  <div ref="tEntry" class="columns p-1 m-0 is-flex is-align-items-center">
    <div class="column is-4">
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
            @click="copyValue()"
            class="navbar-item"
            role="button"
          >
            <span>{{ project }}</span>
            <b-icon icon="menu-down"></b-icon>
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
              <AddProject @close="props.close"></AddProject>
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
    </div>
    <div class="column is-1">
      <!-- TAGS -->
      <b-icon icon="tag-multiple" size="is-medium"> </b-icon>
    </div>
    <div class="column is-1">
      <!-- TIME STARTED -->
      <b-input
        ref="timeStartRef"
        @blur="setTime(startTime)"
        @focus="timeInputFocus(startTime, $refs.timeStartRef)"
        v-model="startTime"
      ></b-input>
    </div>
    <div class="column is-1">
      <!-- TIME ENDED -->
      <b-input
      ref="timeEndRef"
        @blur="setTime(endTime)"
        @focus="timeInputFocus(endTime, $refs.timeEndRef)"
        v-model="endTime"
      ></b-input>
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
import AddProject from "../components/AddProject.vue";
export default {
  components: { AddProject },
  props: ["canCancel"],
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
      tempDescription: "",
      // TIME INPUTS
      startTime: "",
      endTime: "",
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
      this.axios
        .get("http://127.0.0.1:8000/time-entries/1/")
        .then((response) => {
          this.dataObj = response.data;
          this.loadProjects();
          this.getProject();
          this.getDescription();
          this.getTime();
          this.getDuration();
        });
    },
    saveData(toastMessage) {
      this.axios
        .post("http://127.0.0.1:8000/time-entries/1/update/", this.dataObj)
        .then((response) => {
          this.dataObj = response.data;
          this.getProject();
          this.getDescription();
          this.getTime();
          this.getDuration();
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
        this.saveData(toastMessage);
      }
    },

    // PROJECTS DROPDOWN
    getProject() {
      let url = "http://127.0.0.1:8000/project-list/" + this.dataObj.project;
      this.axios.get(url).then((response) => {
        this.project = response.data.title;
        this.projectColor = `color: ${response.data.color}`;
      });
    },
    setProject(id) {
      let toastMessage = "Project has been updated.";
      if (!(this.dataObj.project == id)) {
        this.dataObj.project = id;
        this.saveData(toastMessage);
      }
    },
    loadProjects() {
      this.axios.get("http://127.0.0.1:8000/project-list/").then((response) => {
        this.projects = response.data;
      });
    },
    filteredProjects() {
      return this.projects.filter((project) => {
        return project.title
          .toLowerCase()
          .includes(this.searchTerm.toLowerCase());
      });
    },
    createProject() {},
    // DURATION DROPDOWN
    focusOnDuration(event) {
      this.tempValue = this.duration;
      event.target.select();
    },
    getDuration() {
      let timeDiff = this.dataObj.end_date - this.dataObj.start_date;
      let dHours = Math.floor(timeDiff / 60 / 60);
      timeDiff -= dHours * 60 * 60;
      let dMinutes = Math.floor(timeDiff / 60);
      timeDiff -= dMinutes * 60;
      let dSeconds = timeDiff;
      this.duration = dHours + ":" + dMinutes + ":" + dSeconds;
    },
    // TIME INPUTS
    timeInputFocus(instance, ref) {
      this.copyValue(instance);
      if (instance == this.startTime) {
        this.startTime = this.startTime.replace(':', '')
      } else {
        this.endTime =  this.endTime.replace(':', '')
      }
      
      this.$nextTick(() => {
        ref.$refs.input.select()
      })
      
    },
    getTime() {
      let startHours = new Date(this.dataObj.start_date * 1000).getHours();
      let startMinutes = new Date(this.dataObj.start_date * 1000).getMinutes();
      this.startTime = startHours + ":" + startMinutes;

      let endHours = new Date(this.dataObj.end_date * 1000).getHours();
      let endMinutes = new Date(this.dataObj.end_date * 1000).getMinutes();
      this.endTime = endHours + ":" + endMinutes;
    },
    setTime(timeInstance) {
      if (!(this.tempValue == timeInstance)) {
        let [startHours, startMinutes] = this.timeValid(this.startTime);
        if (startHours == false && startMinutes == false) {
          this.startTime = this.tempValue;

          return false;
        }
        let start = this.zeroHours(this.dataObj.start_date).setHours(
          startHours,
          startMinutes
        );
        start = new Date(start).getTime() / 1000;
        this.dataObj.start_date = start;

        let [endHours, endMinutes] = this.timeValid(this.endTime);
        if (endHours == false && sendinutes == false) {
          this.endTime = this.tempValue;

          return false;
        }
        let end = this.zeroHours(this.dataObj.end_date).setHours(
          endHours,
          endMinutes
        );
        end = new Date(end).getTime() / 1000;
        if (start > end) {
          end = this.zeroNextDay(this.dataObj.end_date).setHours(
            endHours,
            endMinutes
          );
          end = new Date(end).getTime() / 1000;

        }
        this.dataObj.end_date = end;
        this.saveData("date updated");
      } else {
        this.getTime()
        
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
    zeroHours(timestamp) {
      
      let date = new Date(timestamp * 1000).setHours(0, 0);
      return new Date(date);
    },
    zeroNextDay(timestamp) {
      let day = new Date(timestamp * 1000).setHours(0, 0);
      day = new Date(day);
      day.setDate(day.getDate() + 1);
      return new Date(day);
    },
    timeValid(timeStr) {
      if (timeStr.length === 3) {
        timeStr = "0" + timeStr;
      }
      if (timeStr.length === 4) {
        timeStr = timeStr.slice(0, 2) + ":" + timeStr.slice(2, 4);
      }
      let re = /^[0-9]{2}[:][0-9]{2}$/;
      if (!re.test(timeStr)) {
        return [false, false];
      }
      let hour = timeStr.slice(0, 2);
      let minute = timeStr.slice(3, 5);
      if (hour > 23 || minute > 59) {
        return [false, false];
      }
      return [hour, minute];
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