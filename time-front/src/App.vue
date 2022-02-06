<template>
  <div class="" id="app">
    <div id="nav">
      <NavBar />
    </div>
    <div class="content">
      <div>
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  components: { NavBar },
};
</script>

<style>

</style>
