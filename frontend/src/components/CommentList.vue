<template>
  <div>
    <ul class="list-group">
      <li v-for="comment in comments" :key="comment.id" class="list-group-item">
        <p>{{ comment.content }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'CommentList',
  props: {
    comments: {
      type: Array,
      required: true
    },
    postId: {
      type: Number,
      required: true
    }
  },
};
</script>

<style scoped>
/* CSS styles for this component go here */
</style>
