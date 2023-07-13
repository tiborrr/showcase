<template>
  <div class="home-page">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-12 text-center">
          <h1>Home</h1>
        </div>
      </div>

      <!-- Form for creating a post -->
      <div class="row justify-content-center">
        <div class="col-md-8">
          <div class="card">
            <div class="card-header">
              <h2>Create a Post</h2>
            </div>
            <div class="card-body">
              <PostCreate @refresh-posts="refreshPosts" />
            </div>
          </div>
        </div>
      </div>

      <!-- List of posts -->
      <div class="row justify-content-center mt-4">
        <div class="col-md-8">
          <div class="card">
            <div class="card-header">
              <h2>Posts</h2>
            </div>
            <div class="card-body">
              <PostList :posts="posts" @refresh-posts="refreshPosts" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import PostCreate from '../components/PostCreate.vue';
import PostList from '../components/PostList.vue';
import axios from 'axios';
import router from '@/router';

export default {
  name: 'HomePage',
  components: {
    PostCreate,
    PostList,
  },
  setup() {
    const posts = ref([]);
    let intervalId = null;

    const refreshPosts = async () => {
      try {
        const response = await axios.get('/posts');
        posts.value = response.data;
        console.log('HomePage: refreshing posts');
      } catch (error) {
        console.error(error);
      }
    };

    const checkUserExists = async () => {
      try {
        const userId = localStorage.getItem('user_id');
        if (userId) {
          const response = await axios.get('/users/1');
          console.log('User exists:', response.data);
        } else {
          console.log('User is not logged in');
          router.push( { name: 'LoginPage'} )
        }
      } catch (error) {
        console.error('User not found:', error);
      }
    };

    onMounted(async () => {
      await checkUserExists();
      refreshPosts();
      intervalId = setInterval(refreshPosts, 100000);
    });

    onUnmounted(() => {
      if (intervalId) {
        clearInterval(intervalId);
      }
    });

    return {
      posts,
      refreshPosts,
    };
  },
};
</script>

<style scoped>
.home-page {
  padding-top: 20px;
}

.container {
  max-width: 1000px;
}
</style>
