<template>
  <div class="user-create card bg-dark p-4 mx-auto" style="max-width: 400px;">
    <form @submit.prevent="submitForm">
      <div class="form-group mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" id="name" v-model="form.name" class="form-control" required/>
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios'; // assuming you're using axios for http requests
import router from '../router'; // import your router

export default {
  name: 'UserCreate',
  setup() {
      const form = ref({
          name: '',
      }); // object for holding form data

      const submitForm = async () => {
          try {
              const response = await axios.post('/users', form.value);
              localStorage.setItem('user_id', response.data.id); // save user id in local storage
              router.push({ name: 'HomePage' }); // navigate to HomePage
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
