<template>
    <div>
        <form @submit.prevent="submitForm">
            <div class="form-group mb-3">
                <label for="content">Content</label>
                <textarea id="content" v-model="form.content" class="form-control" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary mb-2">Update Comment</button>
        </form>
    </div>
</template>
  
<script>
import { reactive, watchEffect } from 'vue';
import axios from 'axios';

export default {
    name: 'CommentUpdate',
    props: {
        comment: {
            type: Object,
            required: true,
        },
    },
    setup(props, context) {
        const form = reactive({
            content: props.comment.content,
        });

        watchEffect(() => {
            form.content = props.comment.content;
        });

        const submitForm = async () => {
            try {
                await axios.put(`/comments/${props.comment.id}`, form);
                context.emit('refresh-posts');
            } catch (error) {
                console.error(error);
                // handle error, show user feedback, etc.
            }
        };

        // I'm assuming that these functions would be used elsewhere in your component.
        const updateComment = async (commentId, updatedContent) => {
            try {
                await axios.put(`/comments/${commentId}`, { content: updatedContent });
                context.emit('refresh-posts');
            } catch (error) {
                if (error.response && error.response.status === 404) {
                    console.error(error);
                    // Handle the 404 error, e.g., show an error message to the user
                } else {
                    console.error(error);
                    // Handle other types of errors
                }
            }
        };

        const deleteComment = async (commentId) => {
            try {
                await axios.delete(`/comments/${commentId}`);
                context.emit('refresh-posts');
            } catch (error) {
                if (error.response && error.response.status === 404) {
                    // Handle the 404 error, e.g., show an error message to the user
                    console.error(error);
                } else {
                    // Handle other types of errors
                    console.error(error);
                }
            }
        };

        // Return everything we need to use in our template
        return { form, submitForm, updateComment, deleteComment };
    },
};
</script>
  
<style scoped>
/* CSS styles for this component go here */
</style>
  