<template>
    <Bar v-if="chartData" :height="350" :width="900" :chart-data="chartData" :options="options" />
</template>

<script>
import { Duration, DateTime, Info } from "luxon";
import Bar from "@/components/charts/Bar.js";
export default {
    props: ['entries', 'color', "project"],
    components: { Bar },
    mounted() {
        this.weekdays = Info.weekdays();
        this.setData()
        this.setChartData()
    },
    methods: {
        setData() {
            let labels = this.entries.map((entry) => entry.start_date)
            let values = this.entries.map((entry) => entry.end_date - entry.start_date)
            let dateStart = DateTime.fromMillis(labels[0] * 1000).startOf('day')
            let dateEnd = DateTime.fromMillis(labels[labels.length - 1] * 1000).endOf('day')

            let timeline = [];
            let timelineRanges = [];
            let cursor = dateStart;
            // iterates through given date range with 1 day step
            while (cursor <= dateEnd) {
                timeline.push(cursor.startOf("day").ts); // create array with days to be displayed as xLabel
                timelineRanges.push({
                    // ceate array of date ranges to filter entries
                    start: cursor.startOf("day").ts / 1000,
                    end: cursor.endOf("day").ts / 1000,
                });
                cursor = cursor.plus({ days: 1 });
            }
            let data = []
            for (let x = 0; x < timeline.length; x++) {
                data[x] = 0
            }
            for (let x = 0; x < timelineRanges.length; x++) {
                for (let entry of this.entries) {
                    if (entry.start_date > timelineRanges[x].start && entry.start_date < timelineRanges[x].end) {
                        data[x] += (entry.end_date - entry.start_date)
                    }
                }
            }
            let datasets = [{
                data: data,
                backgroundColor: this.color
            }]
            this.datasets = datasets
            this.labels = timeline


        },
        setChartData() {
            this.$nextTick(() => {
                this.chartData = {
                    labels: this.labels,
                    datasets: this.datasets,
                };
            })

        },
    },
    watch: {
        entries: function () {
            this.setData();
            this.setChartData()
        }
    },
    data() {
        return {
            labels: [],
            datasets: [],
            chartData: {},
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
                            // get date and weekday
                            let titleDate = DateTime.fromMillis(
                                object.labels[TooltipItem[0].index]
                            );
                            let day = titleDate.weekday - 1;
                            console.log('tooltip', titleDate.day, titleDate.month)
                            titleDate = titleDate.toFormat("dd-MM-yyyy");
                            // add total day duration
                            return `${this.weekdays[day]}, ${titleDate}`;
                        },

                        label: (tooltipItem, object) => {
                            let project =
                                this.project;
                            let duration =
                                object.datasets[tooltipItem.datasetIndex].data[
                                tooltipItem.index
                                ];
                            if (duration > 0) {
                                duration = Duration.fromMillis(
                                    duration * 1000
                                ).toFormat("hh:mm:ss");
                                return `${project}: ${duration}`;
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

        }
    }
}


</script>

<style>
</style>