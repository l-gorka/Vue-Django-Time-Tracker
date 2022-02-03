<template>
  <div class="wrapper">
    <div class="panel is-success">
      <div class="panel-heading level mb-0">
        <p class="m-0">{{ dayEntry.date }}</p>
        <p>Total: {{ dayEntry.total }}</p>
      </div>
      <div class="">
        <TimeEntry :timeEntry="item" v-for="item in dayEntry.entries" :key="item" />
      </div>
    </div>
  </div>
</template>

<script>
import TimeEntry from '../components/TimeEntry.vue'
export default {
  props: ["dayEntry"],
  components: { TimeEntry },
  data() {
    return {};
  },
};
</script>

<style>
</style>