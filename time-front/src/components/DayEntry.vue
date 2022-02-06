<template>
  <div class="wrapper">
    <div class="panel is-success my-5">
      <div class="panel-heading level mb-0 py-1 px-3">
        <p class="m-0">{{ dayEntry.date }}</p>
        <p>Total: {{ dayEntry.total }}</p>
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
};
</script>

<style>
</style>