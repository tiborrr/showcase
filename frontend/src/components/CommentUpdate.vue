<template>
    <div>
        Form for updating a comment
    </div>
</template>
  
<script>
export default {
    name: 'CommentUpdate',
    props: ['commentId'],
    data() {
        return {
            form: {}, // fetch comment data using commentId prop and use it for form data
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
  