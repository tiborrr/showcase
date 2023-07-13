<template>
  <div>
    <ul class="list-group">
      <li v-for="comment in comments" :key="comment.id" class="list-group-item">
        <div class="d-flex justify-content-between align-items-start">
          <p>{{ comment.content }}</p>
          <div>
            <font-awesome-icon @click="toggleCommentEditing(comment.id)" icon="edit" class="btn-icon" />
            <font-awesome-icon @click="deleteComment(comment.id)" icon="trash" class="btn-icon" />
          </div>
        </div>
        <CommentUpdate v-if="isEditingComment(comment.id)" :comment="comment" @refresh-comments="refreshComments" />
      </li>
    </ul>
  </div>
</template>

<script>
import { ref } from 'vue';
import CommentUpdate from './CommentUpdate.vue';
import axios from 'axios';

export default {
  name: 'CommentList',
  components: {
    CommentUpdate,
  },
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
  setup(props, { emit }) {
    const editingCommentId = ref(null);

    const toggleCommentEditing = (commentId) => {
      editingCommentId.value = editingCommentId.value === commentId ? null : commentId;
    };

    const isEditingComment = (commentId) => {
      return editingCommentId.value === commentId;
    };

    const deleteComment = async (commentId) => {
      try {
        await axios.delete(`/comments/${commentId}`);
        emit('refresh-posts');
      } catch (error) {
        console.error(error);
        // handle error, show user feedback, etc.
      }
    };

    const refreshComments = () => {
      // Refresh your comments list here
      // Reset editingCommentId
      editingCommentId.value = null;
      emit('refresh-posts');
    };

    return { toggleCommentEditing, isEditingComment, deleteComment, refreshComments };
  },
};
</script>

<style scoped>

</style>