import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, message) {
      state.message = message
    },
  },
  actions: {
    changeMessage(context, message) {
      context.commit('CHANGE_MESSAGE', message)
    },
  },
  modules: {
  }
})
