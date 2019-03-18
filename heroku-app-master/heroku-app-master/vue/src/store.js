import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const axs = axios.create({
  headers: { 'X-CSRFToken': window.csrftoken },
});

export default new Vuex.Store({
  state: {
    frameworks: ['Django', 'Vue.js'],
    greetings: [],
  },
  mutations: {
    updateGreetings(state, payload) {
      state.greetings = payload;
    },
  },
  actions: {
    async getGreetings(context, params={}) {
      const response = await axs.get('../hello/');
      const { data } = response;
      context.commit('updateGreetings', data);
    },
  },
  getters: {
    csrfToken(state) {
      return window.csrftoken;
    },
  },
});
