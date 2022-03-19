<template>
  <div class="wrapper">
    <div class="panel is-success my-5 mx-2 ">
      <div class="panel-heading level mb-0 py-1 px-3">
        <p class="m-0">{{ dayEntry.date }}</p>
        <p>Total: {{ time_total }}</p>
      </div>
      <div class="panel-body">
        <TimeEntry
          :class="`time-entry-${index}`"
          @dataChanged="dataChanged"
          :timeEntryID="id"
          v-for="(id, index) in timeEntries"
          :key="id"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TimeEntry from "./TimeEntry.vue";
export default {
  props: ["dayEntry"],
  components: { TimeEntry },
  methods: {
    dataChanged() {
      this.$emit("dataChanged");
    },
  },
  data() {
    return {
      entries: [],
    };
  },
  computed: {
    // Convert time in seconds to be displayed in HH:MM:SS format.
    time_total: function() {
      let totalSeconds;
      totalSeconds = this.dayEntry.time_total;
      let hours, minutes, seconds;
      hours = +Math.floor(totalSeconds / 60 / 60);
      totalSeconds -= hours * 60 * 60;
      minutes = Math.floor(totalSeconds / 60);
      totalSeconds -= minutes * 60;
      seconds = totalSeconds;
      // If value has 1 digit, add preceding 0 to it.
      return (
        ("00" + hours).slice(-2) +
        ":" +
        ("00" + minutes).slice(-2) +
        ":" +
        ("00" + seconds).slice(-2)
      );
    },
    timeEntries() {
      return this.dayEntry.time_entries;
    },
  },
};
</script>

<style>
</style>