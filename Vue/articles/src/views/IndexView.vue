<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{ name: 'create' }">게시글 작성</router-link>
    <hr />
    <ArticleItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script>
import ArticleItem from "@/components/ArticleItem";

export default {
  name: "IndexView",
  components: {
    ArticleItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
};
</script>

<style></style>
