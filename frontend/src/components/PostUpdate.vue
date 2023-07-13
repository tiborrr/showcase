<template>
  <div>
    <form @submit.prevent="submitForm" class="container">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" id="title" v-model="form.title" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="content">Content</label>
        <textarea id="content" v-model="form.content" class="form-control" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Update Post</button>
    </form>
  </div>
</template>

<script>
import { reactive, watchEffect } from 'vue';
import axios from 'axios';

export default {
  name: 'PostUpdate',
  props: {
      post: {
          type: Object,
          required: true,
      },
  },
  setup(props, context) {
      const form = reactive({
          title: props.post.title,
          content: props.post.content,
      });

      watchEffect(() => {
          form.title = props.post.title;
          form.content = props.post.content;
      });

      const submitForm = async () => {
          try {
              await axios.put(`/posts/${props.post.id}`, form);
              context.emit('post-updated');
          } catch (error) {
              console.error(error);
              // handle error, show user feedback, etc.
          }
      };

      return { form, submitForm };
  },
};
</script>

<style scoped>
/* CSS styles for this component go here */
</style>
