<template>
    <div class="pt-0 mt-0" id="app">
        <NavBar />
        <router-view />
        <Footer id="footer"/>
    </div>
</template>

<script>
import NavBar from "./components/common/NavBar.vue";
import Footer from "./components/common/Footer.vue";
export default {
    components: { NavBar, Footer },
};
</script>

<style>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
#footer {
  margin-top: auto;
}
.page-wrapper {
  width: 100%;
  justify-self: center;
  max-width: 1400px;
  padding: 0 2rem;
  margin: 0 auto;
}
@media screen and (max-width: 1024px) {
.page-wrapper {
  padding: 0.5rem;
  }
}
</style>
