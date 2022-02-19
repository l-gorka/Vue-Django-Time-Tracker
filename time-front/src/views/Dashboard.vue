<template>
    <div class="container is-fluid mt-5">
        <div class="level">
            <div class="level-left">
                <div class="level-item">
                    <div class="title is-danger">
                        <b-icon icon="view-dashboard" size="is-small"></b-icon>
                        <span>Dashboard <del>blue</del></span>
                    </div>
                </div>
            </div>
            <div class="level-right">
                <div class="level-item">
                    <div class="title">
                        <date-picker @setDate="setDate" />
                    </div>
                </div>
            </div>
        </div>
        <div class="columns is-multiline">
            <div class="column is-8">
                <div class="columns">
                    <div class="column is-half">
                        <div class="box notification is-danger">
                            <div class="heading">Total time</div>
                            <div class="title">14:01:46</div>
                            <div class="level">
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Billable</div>
                                        <div class="title is-5">100%</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Amount</div>
                                        <div class="title is-5">$ 56</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Success %</div>
                                        <div class="title is-5">+ 28,5%</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-half">
                        <div class="box notification is-info">
                            <div class="heading">Top project</div>
                            <div class="title">Some project here</div>
                            <div class="level">
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Orders $</div>
                                        <div class="title is-5">425K</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Returns $</div>
                                        <div class="title is-5">106K</div>
                                    </div>
                                </div>
                                <div class="level-item">
                                    <div class>
                                        <div class="heading">Success %</div>
                                        <div class="title is-5">+ 28,5%</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="message">
                    <div class="message-header">
                        <p>Chart</p>
                    </div>
                    <div class="message-body">
                        <bar />
                    </div>
                </div>
            </div>
            <div class="column is-4">
                <div class="message">
                    <div class="message-header">
                        <p>Chart</p>
                    </div>
                    <div class="message-body">
                        <doughnut />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Bar from '../components/dashboard/Bar.vue'
import Doughnut from '../components/dashboard/Doughnut.vue'
import DatePicker from '../components/dashboard/DatePicker.vue'
export default {
    components: { Bar, Doughnut, DatePicker },
    methods: {
        setDate(dateStart, dateEnd) {
            this.$buefy.toast.open(`${dateStart} | ${dateEnd}`)
        }
    }
}
</script>

<style>
</style>