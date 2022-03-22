<template>
    <b-dropdown aria-role="list">
        <template #trigger="{}">
            <b-button @click="copyValue" type="is-ghost" size="is-small">
                <b-icon icon="calendar" class="is-size-4"></b-icon>
            </b-button>
        </template>

        <b-dropdown-item custom aria-role="listitem">
            <b-datepicker
                @focus="copyValue"
                v-model="startDate"
                @input="changeDate"
                inline
                :first-day-of-week="1"
                nearby-selectable-month-days
            ></b-datepicker>
        </b-dropdown-item>
    </b-dropdown>
</template>

<script>
import { DateTime, Duration } from "luxon";
export default {
    props: ["timestamp"],
    mounted() {
        this.startDate = DateTime.fromSeconds(this.timestamp).toJSDate();
    },
    data() {
        return {
            startDate: null,
            tempValue: null,
            difference: null,
        };
    },
    methods: {
        copyValue() {
            this.tempValue = DateTime.fromJSDate(this.startDate);
        },
        changeDate() {
            let dateObj = DateTime.fromJSDate(this.startDate);
            let midnight = this.tempValue.startOf("day");
            let dateDifferenceSeconds = (dateObj.ts - midnight.ts) / 1000;
            this.$emit("dateChanged", dateDifferenceSeconds);
        },
    },
};
</script>

<style>
</style>