<template>
  <div class="post-create">
    <form @submit.prevent="submitForm" class="container">
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" id="title" v-model="form.title" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="content">Content</label>
        <textarea id="content" v-model="form.content" class="form-control" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Create Post</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
name: 'PostCreate',
setup(_, context) {
  const form = ref({
    title: '',
    content: '',
  });

  const submitForm = async () => {
    try {
      const userId = localStorage.getItem('user_id');
      if (userId) {
        await axios.post('/posts', { ...form.value, user_id: userId });
        context.emit('refresh-posts');
        console.log('PostCreate: refresh-posts')
        form.value.title = '';
        form.value.content = '';
      } else {
        console.error('User not logged in');
      }
    } catch (error) {
      console.error(error);
    }
  };

  return {
    form,
    submitForm,
  };
},
};
</script>

<style scoped>
/* CSS styles for this component go here */
</style>