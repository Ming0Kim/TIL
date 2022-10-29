<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title" /><br />
      <label for="content">내용 : </label>
      <textarea
        id="content"
        cols="30"
        rows="10"
        v-model.trim="content"
      ></textarea
      ><br />
      <input type="submit" />
    </form>
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    };
  },
  methods: {
    createArticle() {
      const title = this.title;
      const content = this.content;
      if (!title) {
        alert("제목을 입력해주세요");
      } else if (!content) {
        alert("내용을 입력해주세요");
      } else {
        const payload = {
          title,
          content,
        };
        this.$store.dispatch("createArticle", payload);
        this.$router.push({ name: "index" });
      }
    },
  },
};
</script>

<style></style>
