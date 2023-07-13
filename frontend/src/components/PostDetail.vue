<template>
    <div>
        Details of a post
    </div>
</template>
  
<script>
export default {
    name: 'PostDetail',
    props: ['postId'],
    data() {
        return {
            post: null, // fetch post details using postId prop
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
  