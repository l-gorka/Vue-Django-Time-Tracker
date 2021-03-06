<template>
    <div>
        <b-dropdown ref="dropdown" mobile-modal position="is-bottom-left" aria-role="list">
            <template #trigger="{}">
                <b-button
                class="cy-date-picker"
                    v-if="largeIcon"
                    :label="dateOptionSelected"
                    type="is-primary"
                    icon-left="calendar"
                />
                <b-button v-else class="has-text-white" type="is-ghost" size="is-small">
                    <b-icon icon="calendar" class="is-size-4"></b-icon>
                </b-button>
            </template>

            <b-dropdown-item class="dropdown-container p-0" custom aria-role="listitem">
                <div class="columns cy-date-options">
                    <div
                        class="column is-flex is-flex-direction-column is-align-self-baseline is-align-content-stretch"
                    >
                        <div class="mb-3 px-2" v-for="option in dateOptions" :key="option.id">
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

                    <div class="column p-0">
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
    props: ['largeIcon'],
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
                this.$emit('setDate', this.dateStart, this.dateEnd, this.dateOptionSelected)
            });
        },
        setDateOption(option) {

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

            this.$emit('setDate', this.dateStart, this.dateEnd, this.dateOptionSelected)
        },
    },
    mounted() {
        this.setDateOption("This week");
    },
};
</script>

<style>
.dropdown-content {
    width: 100%;
}
</style>