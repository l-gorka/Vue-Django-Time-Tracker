<template>
  <b-dropdown ref="dropdown">
    <button class="button is-ghost has-text-black" slot="trigger">
      <span class="is-size-4">{{ counterStr }}</span>
    </button>
    <b-dropdown-item custom><b-input></b-input></b-dropdown-item>
  </b-dropdown>
</template>

<script>
export default {
  props: ["isCounterStarted", "counterTimeSeconds"],
  data() {
    return {
      counter: null,
      counterSeconds: 0,
      counterStr: "00:00:00",
    };
  },
  watch: {
    isCounterStarted: function () {
      if (this.isCounterStarted) {
        this.startCounter();
      } else {
        this.stopCounter();
      }
    },
  },
  methods: {
    startCounter() {
      this.counterSeconds += this.counterTimeSeconds
      this.counter = setInterval(() => this.displayCounter(), 1000);
    },
    stopCounter() {
      this.$emit("counterStopped", this.counterSeconds);
      this.counterSeconds = 0;
      this.counterStr = "00:00:00"
      clearInterval(this.counter);
    },
    displayCounter() {
      this.counterSeconds += 1;
      let totalSeconds;
      totalSeconds = this.counterSeconds;
      let hours, minutes, seconds;
      hours = +Math.floor(totalSeconds / 60 / 60);
      totalSeconds -= hours * 60 * 60;
      minutes = Math.floor(totalSeconds / 60);
      totalSeconds -= minutes * 60;
      seconds = totalSeconds;
      this.counterStr =
        ("00" + hours).slice(-2) +
        ":" +
        ("00" + minutes).slice(-2) +
        ":" +
        ("00" + seconds).slice(-2);
    },
  },
};
</script>

<style>
.counter input {
  font-size: rem;
}
</style>