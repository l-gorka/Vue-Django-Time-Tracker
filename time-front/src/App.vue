<template>
    <div class="" id="app">
        <div id="nav">
            <NavBar />
        </div>

        <div>
            <router-view />
        </div>
        
    </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
export default {
    components: { NavBar, Footer },
};
</script>

<style>
body,
html {
    display: flex;
    flex-direction: column;
}
.flex-wrapper {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
    justify-content: space-between;
}
</style>
