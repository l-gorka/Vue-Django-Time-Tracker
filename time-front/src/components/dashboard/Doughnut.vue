<template>
    <div>
        <Doughnut v-if="chartData" :options="chartOptions" :chartData="chartData" />
    </div>
</template>

<script>
import { DateTime, Duration } from "luxon";
import Doughnut from "./Doughnut.js";
export default {
    props: ["entries", "projects"],
    components: { Doughnut },
    watch: {
        entries: function () {
            this.getData();
        },
    },
    methods: {
        getData() {
            let totalSeconds = 0;
            let data = [];
            let labels = [];
            let backgroundColor = [];
            let noProject = { title: "No project", color: "#808080", time: 0 }; //create object to store entries without project
            this.projects.map((object) => (object.time = 0)); // add time field to projects object
            // iterate over entries and add time to projects
            for (let entry of this.entries) {
                if (entry.project) {
                    for (let project of this.projects) {
                        if (entry.project === project.id) {
                            totalSeconds += entry.end_date - entry.start_date
                            project["time"] +=
                                entry.end_date - entry.start_date;
                        }
                    }
                } else {
                    totalSeconds += entry.end_date - entry.start_date
                    noProject.time += entry.end_date - entry.start_date; // add time to antries without project
                }
            }
            // add noProject to projects
            this.projects.push(noProject)            
            this.projects.sort((a, b) => (a.time > b.time) ? -1 : 1) // sort projects by time in seconds
            // push data to arrays before send to chart            
            for (let project of this.projects) {
                if (project.time > 0) {
                    data.push(project.time);
                    labels.push(project.title);
                    backgroundColor.push(project.color);
                }
            }
            console.log('before emit',totalSeconds, this.projects)
            this.$emit('projectsData', totalSeconds, this.projects)
            console.log("projects", this.projects, noProject);
            this.chartData = {
                hoverBackgroundColor: "red",
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
                    display: false,
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