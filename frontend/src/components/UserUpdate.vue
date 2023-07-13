<template>
    <div>
        Form for updating a user
    </div>
</template>
  
<script>
export default {
    name: 'UserUpdate',
    props: ['userId'],
    data() {
        return {
            form: {}, // fetch user data using userId prop and use it for form data
        };
    },
    methods: {
        // method for submitting form goes here
    },
};
</script>
  
<style scoped>
/* CSS styles for this component go here */
</style>
  