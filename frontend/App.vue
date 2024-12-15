<template>
  <div id="app">
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <button @click="fetchData">Fetch Data from Backend</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "App",
  setup() {
    const title = ref("GET IN THE POOL!");
    const message = ref(
      "Welcome to your Flask-powered Vue.js application with TypeScript!"
    );

    const fetchData = async (): Promise<void> => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/api/data");
        message.value = response.data.message;
      } catch (error) {
        console.error("Error fetching data:", error);
        message.value = "Error fetching data from the backend";
      }
    };

    return {
      title,
      message,
      fetchData,
    };
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
