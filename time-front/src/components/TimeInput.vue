<template>
    <b-input
		id="input"
        class="input-text-center"
        ref="inputRef"
        @keyup.native.enter="$event.target.blur()"
        @focus="inputFocus"
        @blur="inputBlur"
        v-model="timeStr"
    ></b-input>
</template>

<script>
export default {
    emits: ["timeChanged"],
    props: ["timestamp"],
    data() {
        return {
            tempValue: null,
            timeStr: "",
            zeroTime: null,
        };
    },
    mounted() {
        this.timeStr = this.timestampToStr(this.timestamp);
    },
    methods: {
        inputFocus() {
            this.timeStr = this.timeStr.replace(":", "");
            this.tempValue = this.timeStr;
            this.$nextTick(() => {
                this.$refs.inputRef.$refs.input.select();
            });
        },
        inputBlur() {
            // check if input value changed
            if (!(this.timeStr == this.tempValue)) {
                // check if input value is valid
                let [hours, minutes] = this.timeValid(this.timeStr);
                if (hours && minutes) {
                    // if valid, emit 'changed'
                    let newTimestamp = this.timeStrToTimestamp(hours, minutes);
                    this.$emit("timeChanged", newTimestamp);
                    // display new time
                    this.timeStr = this.displayTime(this.timeStr);
                } else {
                    // if not valid, restore value from tempValue
                    this.timeStr = this.displayTime(this.tempValue);
                }
            } else {
                //if input value not changed, just display it
                this.timeStr = this.displayTime(this.timeStr);
            }
        },
        timestampToStr(timestamp) {
            let hours, minutes;
            hours = new Date(timestamp * 1000).getHours();
            minutes = new Date(timestamp * 1000).getMinutes();
            return ("00" + hours).slice(-2) + ":" + ("00" + minutes).slice(-2);
        },
        timeStrToTimestamp(hours, minutes) {
            if (hours && minutes) {
                let zero =
                    new Date(this.timestamp * 1000).setHours(0, 0) / 1000;
                let timestamp =
                    new Date(zero * 1000).setHours(hours, minutes) / 1000;
                return timestamp;
            } else {
                return false;
            }
        },
        displayTime(timeStr) {
            if (timeStr.length === 3) {
                timeStr = "0" + timeStr;
            }
            if (timeStr.length === 4) {
                timeStr = timeStr.slice(0, 2) + ":" + timeStr.slice(2, 4);
            }
            return timeStr;
        },
        timeValid(timeStr) {
            if (timeStr.length === 3) {
                timeStr = "0" + timeStr;
            }
            if (timeStr.length === 4) {
                timeStr = timeStr.slice(0, 2) + ":" + timeStr.slice(2, 4);
            }
            let re = /^[0-9]{2}[:][0-9]{2}$/;
            if (!re.test(timeStr)) {
                return [false, false];
            }
            let hours = timeStr.slice(0, 2);
            let minutes = timeStr.slice(3, 5);
            if (hours > 23 || minutes > 59) {
                return [false, false];
            }
            return [hours, minutes];
        },
    },
};
</script>

<style>
</style>