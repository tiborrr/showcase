<template>
  <div>
    <ul class="list-group">
      <li v-for="post in posts" :key="post.id" class="list-group-item">
        <div class="d-flex justify-content-between align-items-start">
          <h3>{{ post.title }}</h3>
          <div>
            <font-awesome-icon @click="togglePostEditing(post.id)" icon="edit" class="btn-icon" />
            <font-awesome-icon @click="deletePost(post.id)" icon="trash" class="btn-icon" />
          </div>
        </div>
        <p>{{ post.content }}</p>
        <PostUpdate v-if="isEditingPost(post.id)" :post="post" @refresh-posts="refreshPosts" />
        <div class="mt-3">
          <CommentList :comments="post.comments" :postId="post.id" @refresh-posts="refreshPosts" />
        </div>
        <div class="mt-3">
          <button @click="togglePostCommenting(post.id)" class="btn btn-primary mb-3">
            {{ isCommentingOnPost(post.id) ? 'Cancel' : 'Comment' }}
          </button>
          <CommentCreate v-if="isCommentingOnPost(post.id)" :postId="post.id" @refresh-posts="refreshPosts" class="mb-3" />
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import PostUpdate from './PostUpdate.vue';
import CommentList from './CommentList.vue';
import CommentCreate from './CommentCreate.vue';

export default {
  name: 'PostList',
  components: {
    PostUpdate,
    CommentList,
    CommentCreate,
  },
  props: {
    posts: {
      type: Array,
      required: true,
    },
  },
  setup(props, context) {
    const editingPostId = ref(null);
    const commentingPostId = ref(null);

    const togglePostEditing = (id) => {
      editingPostId.value = editingPostId.value === id ? null : id;
      commentingPostId.value = null; // clear commenting post if any
    };

    const isEditingPost = (id) => {
      return editingPostId.value === id;
    };

    const togglePostCommenting = (id) => {
      commentingPostId.value = commentingPostId.value === id ? null : id;
      editingPostId.value = null; // clear editing post if any
    };

    const isCommentingOnPost = (id) => {
      return commentingPostId.value === id;
    };

    const refreshPosts = () => {
      editingPostId.value = null;
      console.log('PostList: Emitting refresh-posts event');
      context.emit('refresh-posts');
    };

    const deletePost = async (id) => {
      try {
        await axios.delete(`/posts/${id}`);
        context.emit('refresh-posts');
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(() => {
      context.emit('refresh-posts');
    });

    watch(() => props.posts, () => {
      editingPostId.value = null;
      commentingPostId.value = null;
    });

    return {
      togglePostEditing,
      isEditingPost,
      refreshPosts,
      deletePost,
      togglePostCommenting,
      isCommentingOnPost,
    };
  },
};
</script>
  