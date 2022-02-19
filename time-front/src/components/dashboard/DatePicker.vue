<template>
    <div>
        <b-dropdown ref="dropdown" mobile-modal position="is-bottom-left" aria-role="list">
            <template #trigger="{}">
                <b-button :label="dateOptionSelected" type="is-primary" icon-left="calendar" />
            </template>

            <b-dropdown-item custom aria-role="listitem">
                <div class="columns">
                    <div
                        class="column is-flex is-flex-direction-column is-align-self-baseline is-align-content-stretch"
                    >
                        <div class="mb-3" v-for="option in dateOptions" :key="option.id">
                            <b-button
                                class="is-fullwidth"
                                v-if="option == dateOptionSelected"
                                type="is-primary"
                            >{{ option }}</b-button>
                            <b-button
                                @click="setDateOption(option)"
                                class="is-fullwidth"
                                v-else
                                type="is-primary is-light"
                            >{{ option }}</b-button>
                        </div>
                    </div>

                    <div class="column">
                        <b-datepicker
                            @range-end="setDateFromCalendar"
                            :first-day-of-week="1"
                            v-model="dateSelected"
                            inline
                            range
                            nearby-selectable-month-days
                        ></b-datepicker>
                    </div>
                </div>
            </b-dropdown-item>
        </b-dropdown>
    </div>
</template>

<script>
import { DateTime, Duration } from "luxon";
export default {
    components: {},
    data() {
        return {
            dateStart: null,
            dateEnd: null,
            dateRange: null,
            dateSelected: [],
            dateOptionSelected: "This week",
            dateOptions: ["This week", "Last week", "This month", "Last month"],
        };
    },
    methods: {
        setDateFromCalendar() {
            // update dateStart and dateEnd
            this.$nextTick(() => {
                this.dateStart = DateTime.fromJSDate(this.dateSelected[0]);
                this.dateEnd = DateTime.fromJSDate(this.dateSelected[1]);
                let pickerLabel = `${this.dateStart.toISODate()} | ${this.dateEnd.toISODate()}`;

                this.dateOptionSelected = pickerLabel; // update button label
                this.$refs.dropdown.isActive = false; // close dropdown
                // emit array with new date
                this.$emit('setDate', this.dateStart, this.dateEnd)
            });
        },
        setDateOption(option) {
            console.log(option);
            // select option and close dropdown
            this.dateOptionSelected = option;
            this.$refs.dropdown.isActive = false;
            // if range selected by buttons, pass date to calendar component
            if (option == "This week") {
                this.dateStart = DateTime.now().startOf("week");
                this.dateEnd = DateTime.now().endOf("week");
            } else if (option == "Last week") {
                let lastWeek = DateTime.now().minus(
                    Duration.fromObject({ weeks: 1 })
                );
                this.dateStart = lastWeek.startOf("week");
                this.dateEnd = lastWeek.endOf("week");
            } else if (option == "This month") {
                this.dateStart = DateTime.now().startOf("month");
                this.dateEnd = DateTime.now().endOf("month");
            } else if (option == "Last month") {
                let lastMonth = DateTime.now().minus(
                    Duration.fromObject({ months: 1 })
                );
                this.dateStart = lastMonth.startOf("month");
                this.dateEnd = lastMonth.endOf("month");
            }
            // pass data to calendar component
            this.dateSelected = [
                new Date(this.dateStart),
                new Date(this.dateEnd),
            ];

            this.$emit('setDate', this.dateStart, this.dateEnd)
        },
    },
    mounted() {
        this.setDateOption("This week");
    },
};
</script>

<style>
</style>