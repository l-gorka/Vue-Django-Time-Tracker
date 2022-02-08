<template>
  <div class="container is-fullhd">
    <div>

      <CurrentTask @timeEntryCreated="getDayEntries" />
    </div>
    <div v-if="dayEntries">
      <DayEntry
        @dataChanged="getDayEntries"
        :dayEntry="dayEntry"
        v-for="dayEntry in dayEntries"
        :key="dayEntry.id"
      />
    </div>
  </div>
</template>

<script>
import TimeEntry from "../components/TimeEntry.vue";
import DayEntry from "../components/DayEntry.vue";
import CurrentTask from "../components/CurrentTask.vue";
export default {
  components: { DayEntry, TimeEntry, CurrentTask },
  data() {
    return {
      dayEntries: [],
    };
  },
  mounted() {
    this.getDayEntries();
  },
  methods: {
    alert() {
      alert("changed");
    },
    getDayEntries() {
      this.axios.get("http://127.0.0.1:8000/day-entries/").then((response) => {
        this.dayEntries = response.data;
        for (let item of this.dayEntries) {
          item.time_entries.reverse()
        }
      });
    },
  },
};
</script>

<style>
.input-text-center input {
  text-align: center;
}
</style>