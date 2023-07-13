<template>
    <div class="login container">
      <UserCreate @user-created="onUserCreated" />
    </div>
  </template>
  
<script>
import { useRouter } from 'vue-router';
import UserCreate from '../components/UserCreate.vue';

export default {
    name: 'UserLogin',
    components: {
        UserCreate,
    },
    setup() {
        const router = useRouter();

        const onUserCreated = () => {
            router.push({ name: 'Home' });
        };

        return {
            onUserCreated,
        };
    },
};
</script>
  
<style scoped>
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
  