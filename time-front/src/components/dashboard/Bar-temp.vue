<template>
    <div class="container is-fullhd">
        <h1>Dashboard</h1>
        <div>
            <b-field label="Select a date">
                <b-datepicker placeholder="Click to select..." :range="range" v-model="dates"></b-datepicker>
            </b-field>
            <b-button @click="getJson" type="is-primary" label="Filterdates" />
            <br />
            <br />
            <p v-if="thisWeek">thisWeek {{ thisWeek }}</p>

            <br />
            {{ date2[0] }}|{{ date2[1] }}
            <br />
            {{chartData.datasets[0].data}}
            <Bar
                v-if="barChartIsVisible"
                :chart-data="chartData"
                :options="options"
                :width="800"
                :height="300"
            />
        </div>
    </div>
</template>


<script>
import 'chartjs-adapter-luxon';
import { Duration, DateTime } from 'luxon'
import { getAPI } from '@/axios-base.js'
import Bar from '@/components/dashboard/Bar.js'
export default {
    components: {
        Bar
    },
    computed: {
        tWeek() {
            return this.thisWeek
        },
        token() {
            return this.$store.state.accessToken
        },
        date2() {
            let start = Date.parse(this.dates[0]) || null
            let end = Date.parse(this.dates[1]) || null
            return [start, end]
        }
    },
    mounted() {
        this.getJson()
    },
    data() {
        return {
            range: true,
            dates: [],
            barChartIsVisible: false,
            thisWeek: {},
            start: 0,
            end: 9999999999,
            chartData: {
                datasets: [
                    {
                        label: 'My First dataset',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: [],
                    }
                ]
            },
            options: {
                responsive: false,
                tooltips: {
                    enabled: true,
                    callbacks: {
                        title: (TooltipItem) => {
                            console.log(TooltipItem)
                            return Duration.fromMillis(TooltipItem[0].yLabel * 1000).toFormat('hh:mm:ss')
                        }

                    }
                },
                scales: {
                    xAxes: [{
                        adapters: {
                            date: {
                                zone: 'UTC',
                            },
                        },
                        offset: true,
                        type: 'time',

                        distribution: 'linear',
                        time: {
                            unit: 'day',
                        },
                        ticks: {
                            beginAtZero: true,
                            min: 1643735574000,
                            max: 1646584055000,

                        }
                    }],
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'Hours'
                        },
                        ticks: {
                            
                            stepSize: 3600,
                            callback: function (value, index, values) {
                                return Duration.fromMillis(value * 1000).toFormat('hh')
                            }
                        }
                    }]
                }
            }
        }
    },
    methods: {


        getWeek() {

            this.thisWeek['start'] = DateTime.now().startOf('week')
            this.thisWeek['end'] = DateTime.now().endOf('week')
        },
        getJson() {

            getAPI
                .get("/day-entries/", {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    },
                })
                .then((response) => {
                    this.chartData = null
                    this.chartData = {

                        datasets: [
                            {
                                label: 'My First dataset',
                                backgroundColor: 'rgb(255, 99, 132)',
                                borderColor: 'rgb(255, 99, 132)',
                                data: [],
                            }
                        ]


                    }
                    let json = response.data
                    let data = []
                    json.map((e) => {
                        let dict = {}
                        let timestamp = Date.parse(e.date)
                        dict['x'] = timestamp
                        dict['y'] = e.time_total
                        dict['color'] = 'red'
                        console.log(this.date2[0], timestamp, this.date2[1])
                        if (this.date2) {
                            if (this.date2[0] < timestamp && timestamp < this.date2[1]) {

                                data.push(dict)
                            }
                        }
                    })
                    this.chartData.datasets[0].data = data
                    console.log(this.chartData)
                    this.barChartIsVisible = true



                });
        },


    },

}
</script>

<style>
</style>