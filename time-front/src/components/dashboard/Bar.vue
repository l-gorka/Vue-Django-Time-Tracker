<template>
    <Bar v-if="chartData" :height="400" :width="900" :chart-data="chartData" :options="options" />
</template>

<script>
import { Duration, DateTime, Info } from "luxon";
import Bar from "@/components/dashboard/Bar.js";
export default {
    props: ["entries", "projects", "dateStart", "dateEnd"],
    components: { Bar },
    mounted() {
        this.weekdays = Info.weekdays();
    },
    watch: {
        entries: function () {
            this.timeline = this.setTimeline();

            this.setData();
        },
    },
    methods: {
        setTimeline() {
            let timeline = [];
            let timelineRanges = [];
            let cursor = this.dateStart;
            // iterates through given date range with 1 day step
            while (cursor < this.dateEnd) {
                timeline.push(cursor.startOf("day").ts); // create array with days to be displayed as xLabel
                timelineRanges.push({
                    // ceate array of date ranges to filter entries
                    start: cursor.startOf("day").ts / 1000,
                    end: cursor.endOf("day").ts / 1000,
                });
                cursor = cursor.plus({ days: 1 });
            }

            let datasets = [];
            // create dataset for each day and fill with project data
            for (let project of this.projects) {
                let dataset = {};
                dataset["label"] = project.title;
                dataset["backgroundColor"] = project.color;
                dataset["data"] = Array(timeline.length).fill(0);
                dataset["id"] = project.id || null;
                datasets.push(dataset);
            }
            // add time from entries to datasets
            for (let dataset of datasets) {
                for (let entry of this.entries) {
                    if (entry.project == dataset.id) {
                        for (let x = 0; x < timelineRanges.length; x++) {
                            if (
                                entry.start_date > timelineRanges[x].start &&
                                entry.start_date < timelineRanges[x].end
                            ) {
                                dataset.data[x] +=
                                    entry.end_date - entry.start_date;
                            }
                        }
                    }
                }
            }
            this.labels = timeline;
            this.datasets = datasets;
        },
        setData() {
            this.chartData = {
                labels: this.labels,
                datasets: this.datasets,
            };
        },
    },
    data() {
        return {
            labels: [],
            datasets: [],
            chartData: {},
            weekdays: [],
            options: {
                responsive: true,
                legend: {
                    display: false,
                },
                tooltips: {
                    titleFontSize: 16,
                    bodyFontSize: 16,
                    mode: "index",
                    callbacks: {
                        title: (TooltipItem, object) => {
                            console.log(
                                "tooltip",
                                TooltipItem,
                                object,
                                this.weekdays
                            );
                            // get date and weekday
                            let titleDate = DateTime.fromMillis(
                                object.labels[TooltipItem[0].index]
                            );
                            let day = titleDate.weekday - 1;
                            titleDate = titleDate.toFormat("dd-mm-yyyy");
                            // add total day duration
                            let total = 0;
                            for (let dataset of object.datasets) {
                                total += dataset.data[TooltipItem[0].index];
                            }
                            total = Duration.fromMillis(total * 1000).toFormat(
                                "hh:mm:ss"
                            );
                            return `${this.weekdays[day]}, ${titleDate}: ${total}`;
                        },

                        label: (tooltipItem, object) => {
                            let project =
                                object.datasets[tooltipItem.datasetIndex].label;
                            let duration =
                                object.datasets[tooltipItem.datasetIndex].data[
                                    tooltipItem.index
                                ];
                            if (duration > 0) {
                                duration = Duration.fromMillis(
                                    duration * 1000
                                ).toFormat("hh:mm:ss");
                                return ` ${project}: ${duration}`;
                            } else {
                                return "";
                            }
                        },
                    },
                },
                scales: {
                    xAxes: [
                        {
                            offset: true,
                            type: "time",
                            stacked: true, // this should be set to make the bars stacked
                            distribution: "linear",
                            time: {
                                unit: "day",
                                tooltipFormat: "D MM",
                                displayFormats: {
                                    day: "D MMM",
                                },
                            },
                        },
                    ],
                    yAxes: [
                        {
                            stacked: true, // this also..
                            ticks: {
                                stepSize: 3600,
                                callback: function (value, index, values) {
                                    return Duration.fromMillis(
                                        value * 1000
                                    ).toFormat("hh");
                                },
                            },
                        },
                    ],
                },
            },
        };
    },
};
</script>

<style>
</style>