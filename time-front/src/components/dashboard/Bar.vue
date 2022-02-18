<template>
    <Bar :chart-data="chartData" :options="options"/>
</template>

<script>
import Bar from '@/components/dashboard/Bar.js'
export default {
    components: { Bar },
    data() {
        return {
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
                responsive: true,
                resizeDelay: 1000,
                maintainAspectRatio: false,
                    tooltips: {
                    enabled: true,
                        callbacks: {
                            /*
                        title: (TooltipItem) => {
                            console.log(TooltipItem)
                            return Duration.fromMillis(TooltipItem[0].yLabel * 1000).toFormat('hh:mm:ss')
                        }
                        */

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
                            /*
                            ticks: {
                                stepSize: 3600,
                                callback: function (value, index, values) {
                                    return Duration.fromMillis(value * 1000).toFormat('hh')
                                }
                               
                            }
                             */
                        }]
                }
            }
        }
    }
}
</script>

<style>
</style>