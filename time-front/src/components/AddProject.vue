<template>
  <div class="modal-card" style="">
    <header class="modal-card-head">
      <h2 class="modal-card-title">Create new project</h2>
      <button type="button" class="delete" @click="$emit('close')" />
    </header>
    <section class="modal-card-body">
      <div class="columns">
        <div class="column">
          <b-field v-if="title" label="Project name">
            <b-input v-model="projectData.title"></b-input>
          </b-field>
          <b-field
            v-else
            label="Project name"
            type="is-danger"
            message="Please enter project name"
          >
            <b-input @input="title = !title" v-model="projectData.title">
            </b-input>
          </b-field>
          <b-field label="Project color">
            <compact-picker v-model="color" />
          </b-field>
        </div>
        <div class="column">
          <b-field label="Client">
            <b-input v-model="projectData.client"></b-input>
          </b-field>
          <b-field label="Billable">
            <b-switch
              @click="this.projectData.billable = !this.projectData.billable"
              v-model="projectData.billable"
            ></b-switch>
          </b-field>
          <b-field v-if="projectData.billable" label="Billable rate">
            <b-numberinput
              v-model="projectData.billable_rate"
              controls-alignment="left"
              controls-position="compact"
            ></b-numberinput>
          </b-field>
        </div>
      </div>
    </section>
    <footer class="modal-card-foot">
      <b-button label="Close" @click="$emit('close')" />
      <b-button @click="createProject" label="Create" type="is-primary" />
    </footer>
  </div>
</template>

<script>
import { getAPI } from "../axios-base";
import { Compact } from "vue-color";
export default {
  components: {
    "compact-picker": Compact,
  },
  emits: ["close"],
  data() {
    return {
      projectData: {
        owner: 1,
        title: "",
        client: "",
        billable: false,
        billable_rate: null,
        color: "#000000",
      },
      color: "#000000",
      title: true,
    };
  },
  methods: {
    createProject() {
      if (!(this.color == "#000000" )) {
        this.projectData.color = this.color.hex;
      }
      
      console.log(this.projectData);
      if (this.projectData.title) {
        getAPI
          .post("/project-create/", this.projectData, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then((response) => {
            this.$emit("projectAdded", response.data.id);
            this.$emit("close");
            this.toast("Project has been created");
          });
      } else {
        this.title = false;
      }
    },
    setColor() {
      console.log("setcolor");
      this.colorStyle = `color: ${this.color.hex.hex}`;
    },
    toast(toastMessage) {
      this.$buefy.toast.open({
        duration: 5000,
        message: toastMessage,
        position: "is-bottom",
        type: "is-success",
      });
    },
  },
  computed: {
    colorStyle: function () {
      return `color: ${this.color.hex.hex}`;
    },
  },
};
</script>

<style>
</style>