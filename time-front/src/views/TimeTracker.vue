<template>
  <div class="container">
    <DayEntry
      :dayEntry="timeEntry"
      v-for="timeEntry in timeEntries"
      :key="timeEntry"
    />
  </div>
</template>

<script>
import DayEntry from "../components/DayEntry.vue";
export default {
  components: { DayEntry },
  data() {
    return {
      timeEntries: [
        {
          date: "28 Feb 2022",
          total: "03:16:21",
          entries: [
            {
              info: {
                date: "Wed, Jan 26",
                description: "Some description",
                timeStarted: '12:11',
                timeEnded: '13:34',
                project: "Vue learning",
                duration: "1:23:21"
              },
            },
          ],
        },
      ],
      projects: ["Wyprowadzanie kota", "Jedzenie", "Pranie", "Czesanie", "Inne", "Czynności"],
    };
  },
};
</script>

<style>
</style>