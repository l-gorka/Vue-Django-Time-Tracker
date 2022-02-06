<template>
  <div class="container is-fullhd">
    <div>
      <CurrentTask />
    </div>
    <div v-if="dayEntries">
      <DayEntry
        :dayEntry="dayEntry"
        v-for="dayEntry in dayEntries"
        :key="dayEntry.id"
      />
    </div>
  </div>
</template>

<script>
import TimeEntry from "../components/TimeEntry.vue"
import DayEntry from "../components/DayEntry.vue";
import CurrentTask from "../components/CurrentTask.vue";
export default {
  components: { DayEntry, TimeEntry, CurrentTask },
  data() {
    return {
      dayEntries: []
    };
  },
  mounted() {
    this.getDayEntries()
  },
  methods: {
    getDayEntries() {
      this.axios.get('http://127.0.0.1:8000/day-entries/').then((response) => this.dayEntries = response.data)
      console.log(this.dayEntries)
    }
  }
};
</script>

<style>
.input-text-center input {
    text-align: center;
}
</style>