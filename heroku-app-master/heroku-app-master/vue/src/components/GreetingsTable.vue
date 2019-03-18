<template>
  <div class="greetings-table">
    <h3>Greetings</h3>
    <table align="center">
      <thead>
        <tr>
          <th>ID</th>
          <th>When</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="greeting of greetings" :key="greeting.id">
          <td>{{ greeting.id }}</td>
          <td>{{ new Date(greeting.when).toLocaleDateString() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'GreetingsTable',
  computed: {
    greetings() {
      return this.$store.state.greetings;
    },
  },
  mounted() {
    this.$store.dispatch('getGreetings');
  },
};
</script>

<style lang="scss" scoped>
  table {
    th {
      border-bottom: 1px solid gainsboro;
    }
    td, th {
      display: inline-block;
      margin: 5px;
    }
  }
</style>
