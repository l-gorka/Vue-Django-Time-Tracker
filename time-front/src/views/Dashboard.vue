<template>
    <div class="container is-fullhd">
        <h1>Dashboard</h1>
        <div>
            <b-field label="Select a date">
                <b-datepicker
                    placeholder="Click to select..."
                    locale="pl-PL"
                    :range="range"
                    v-model="dates"
                ></b-datepicker>
            </b-field>
            <b-button @click="getJson" type="is-primary" label="get json" />
            <br />
            {{ dates }}
            <br />
            {{ json }}
            {{ date2[0] }}|{{  date2[1] }}
        </div>
    </div>
</template>


<script>
import { getAPI } from '@/axios-base.js'
import Chart from '@/components/dashboard/Chart.vue'
export default {
    components: {
        Chart
    },
    computed: {
        token() {
            return this.$store.state.accessToken
        },
        date2() {
            let start = new Date(this.dates[0])
            let end = new Date(this.dates[1])
            return [Date.parse(start) / 1000, Date.parse(end) / 1000] 
        }
    },
    data() {
        return {
            range: true,
            dates: [],
            json: {}
        }
    },
    methods: {
        getJson() {
            console.log('json')
            getAPI
                .get("/day-entries/", {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    },
                })
                .then((response) => {
                    this.json = response.data
                    console.log('json', this.json)
                });
        },


    },

}
</script>

<style>
</style>