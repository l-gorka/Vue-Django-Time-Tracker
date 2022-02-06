<template>
  <div class="wrapper">
    <div class="panel is-success my-5">
      <div class="panel-heading level mb-0 py-1 px-3">
        <p class="m-0">{{ dayEntry.date }}</p>
        <p>Total: {{ time_total }}</p>
      </div>
      <div class="panel-body">
        <TimeEntry
          :timeEntryID="id"
          v-for="id in dayEntry.time_entries"
          :key="id"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TimeEntry from "../components/TimeEntry.vue";
export default {
  props: ["dayEntry"],
  components: { TimeEntry },
  data() {
    return {
      timeEntryIDS: [1,2,3],
    };
  },
  computed:{
    time_total: function() {
        let totalSeconds
        totalSeconds = this.dayEntry.time_total
        let hours, minutes, seconds
        hours =  + Math.floor(totalSeconds / 60 / 60)
        totalSeconds -=  hours * 60 * 60
        minutes = Math.floor(totalSeconds / 60)
        totalSeconds -= minutes * 60
        seconds = totalSeconds
        return  ('00' + hours).slice(-2) + ':' + ('00' + minutes).slice(-2) + ':' + ('00' + seconds).slice(-2)
    }
  }
};
</script>

<style>
</style>