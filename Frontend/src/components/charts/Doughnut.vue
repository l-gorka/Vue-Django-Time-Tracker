<template>
    <div>
        <Doughnut v-if="chartData" :options="chartOptions" :chartData="chartData" />
    </div>
</template>

<script>
import { DateTime, Duration } from "luxon";
import Doughnut from "../charts/Doughnut.js";
export default {
    props: ["projects"],
    components: { Doughnut },
    watch: {
        projects: function () {
            this.getData();
        },
    },
    methods: {
        getData() {
            let data = [];
            let labels = [];
            let backgroundColor = [];
            for (let project of this.projects) {
                if (project.time > 0) {
                    data.push(project.time);
                    labels.push(project.title);
                    backgroundColor.push(project.color);
                }
            }
            this.chartData = {
                hoverBorderWidth: 10,
                labels: labels,
                datasets: [
                    {
                        backgroundColor: backgroundColor,
                        data: data,
                    },
                ],
            };
        },
    },
    data() {
        return {
            projectEntries: [],
            chartData: {},
            chartOptions: {
                legend: {
                    display: true,
                    position: 'bottom',
                    align: 'start',
                },
                tooltips: {
                    titleFontSize: 16,
                    enabled: true,
                    callbacks: {
                        title: (TooltipItem, object) => {
                            let time =
                                object.datasets[0].data[TooltipItem[0].index];
                            let title = object.labels[TooltipItem[0].index];
                            time = Duration.fromMillis(time * 1000).toFormat(
                                "hh:mm:ss"
                            );
                            return `${title}: ${time}`;
                        },
                        label: () => "",
                    },
                },
                hoverBorderWidth: 20,
                responsive: true,
            },
        };
    },
};
</script>

<style>
</style>