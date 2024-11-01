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
                const response = await axios.get('http://localhost:8000/internal/restaurant/list'); // !TODO: Move to .env
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
