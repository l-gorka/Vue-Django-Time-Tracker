<template>
  <div>
    <b-input :value="counterStr" class="input-text-center"></b-input>
  </div>
</template>

<script>
export default {
  props: ["isCounterStarted"],
  data() {
    return {
      counter: null,
      counterSeconds: 0,
      counterStr: "00:00:00",
    };
  },
  watch: {
    isCounterStarted: function() {
      if (this.isCounterStarted) {
        this.startCounter();
      } else {
        this.stopCounter();
      }
    },
  },
  methods: {
    startCounter() {
      console.log("counter started");
      this.counter = setInterval(() => this.displayCounter(), 1000);
    },
    stopCounter() {
        this.$emit('counterStopped', this.counterSeconds)
      clearInterval(this.counter);
    },
    displayCounter() {
        this.counterSeconds += 1
        let totalSeconds
        totalSeconds = this.counterSeconds
        let hours, minutes, seconds
        hours = Math.floor(totalSeconds / 60 / 60)
        totalSeconds -=  hours * 60 * 60
        minutes = Math.floor(totalSeconds / 60)
        totalSeconds -= minutes * 60
        seconds = totalSeconds
        this.counterStr =  ('00' + hours).slice(-2) + ':' + ('00' + minutes).slice(-2) + ':' + ('00' + seconds).slice(-2)

    }
  },
};
</script>

<style>
</style>