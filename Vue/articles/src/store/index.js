import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    article_id: 3,
    articles: [
      {
        id: 1,
        title: "title1",
        content: "content1",
        createdAt: new Date().getTime(),
      },
      {
        id: 2,
        title: "title2",
        content: "content2",
        createdAt: new Date().getTime(),
      },
    ],
  },
  getters: {},
  mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article);
      state.article_id = state.article_id + 1;
    },
    DELETE_ARTICLE(state, id) {
      state.articles = state.articles.filter((article) => {
        return !(article.id === id);
      });
    },
  },
  actions: {
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      };
      context.commit("CREATE_ARTICLE", article);
    },
  },
  modules: {},
});
