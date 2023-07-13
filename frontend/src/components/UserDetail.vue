<template>
    <div>
        Details of a user
    </div>
</template>
  
<script>
export default {
    name: 'UserDetail',
    props: ['userId'],
    data() {
        return {
            user: null, // fetch user details using userId prop
        };
    },
    methods: {
        // methods for this component go here
    },
};
</script>
  
<style scoped>
/* CSS styles for this component go here */
</style>
  