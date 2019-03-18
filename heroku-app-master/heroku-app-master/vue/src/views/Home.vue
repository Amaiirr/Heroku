<template>
  <div class="home">
    <!-- Always use images from a CDN such as picsum.photos, pixabay, etc. -->
    <img src="https://picsum.photos/500/400/?random"
         alt="A nice picture"
    >
    <HelloWorld :msg="`Welcome to a ${frameworks.join(' + ')} App!`" />
    <GreetingsTable />
  </div>
</template>

<script>
import HelloWorld from '../components/HelloWorld.vue';
import GreetingsTable from '../components/GreetingsTable.vue';

export default {
  name: 'Home',
  components: { HelloWorld, GreetingsTable },
  computed: {
    frameworks() {
      return this.$store.state.frameworks;
    },
  },
};
</script>
