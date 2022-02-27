<template>
  <div class="container is-fullhd">
    <div>
      <CurrentTask @timeEntryCreated="getDayEntries" />
    </div>
    <div class="mb-5" v-if="dayEntries">
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
import { getAPI } from "../axios-base";
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
    
    this.$store.dispatch('getProjects')
    this.$store.dispatch('getTimeEntries').then(() => {
                this.getDayEntries();
            })
        
  },
  computed: {
    token() {
      return this.$store.state.accessToken
    }
  },
  methods: {
    getDayEntries() {
      getAPI
        .get("/day-entries/", {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((response) => {
          this.dayEntries = response.data;
          for (let item of this.dayEntries) {
            item.time_entries.reverse();
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