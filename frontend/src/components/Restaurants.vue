<template>
    <div>
        <h1>My Vue App</h1>
        <button @click="fetchRestaurantList">Show me the restaurants list</button>
        <ul v-if="items.length">
            <li v-for="(item, index) in items" :key="index">{{ item.name }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';
const backendUrl = process.env.BACKEND_URL;

export default {
    name: 'App',
    data() {
        return {
            items: []
        };
    },
    methods: {
        async fetchRestaurantList() {
            try {
                const response = await axios.get(backendUrl+'/internal/restaurant/list');
                this.items = response.data;
            } catch (error) {
                console.error('Error fetching the list:', error);
            }
        }
    }
}
</script>

<style scoped>
.read-the-docs {
    color: #888;
}
</style>
