<template>
    <div>
      <form @submit.prevent="submitForm" class="container">
        <div class="form-group">
          <textarea v-model="form.content" class="form-control" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </template>
  
  
<script>
import { ref, toRefs } from 'vue';
import axios from 'axios';

export default {
    name: 'CommentCreate',
    props: {
        postId: {
            type: Number,
            required: true
        },
    },
    setup(props, context) {
        const { postId } = toRefs(props);
        const form = ref({
            content: '',
        });

        const submitForm = async () => {
            try {
                const userId = localStorage.getItem('user_id');
                if (userId) {
                    await axios.post(`/posts/${postId.value}/comments`, { ...form.value, author_id: userId });
                    console.log('CommentCreate: Emitting refresh-posts event');
                    context.emit('refresh-posts');
                    form.value.content = '';
                } else {
                    console.error('User not logged in');
                }
            } catch (error) {
                console.error(error);
                // handle error, show user feedback, etc.
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
