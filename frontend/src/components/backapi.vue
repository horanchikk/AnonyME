<template></template>

<script>
export default {
    api_url: "http://109.248.133.17:8000/",

    async newUser(username) {
        const req = await fetch(
            `${this.api_url}users/new?name=${username}`
        );
        return await req.json();
    },
    async removeUser(token) {
        await fetch(`${this.api_url}users/remove?token=${token}`);
    },
}
</script>

<style></style>