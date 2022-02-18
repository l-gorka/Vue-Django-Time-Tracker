<template>
    <Doughnut :chartData="chartData" />
</template>

<script>
import Doughnut from './Doughnut.js'
export default {
    components: { Doughnut },
    data() {
        return {
            chartOptions: {
                hoverBorderWidth: 20,
                responsive: true,
            },
            chartData: {
                hoverBackgroundColor: "red",
                hoverBorderWidth: 10,
                labels: ["Green", "Red", "Blue"],
                datasets: [
                    {
                        label: "Data One",
                        backgroundColor: ["#41B883", "#E46651", "#00D8FF"],
                        data: [1, 10, 5]
                    }
                ]
            }
        };
    }
}
</script>

<style>
</style>