<template>
    <div>
        <h1>My Vue App</h1>
        <button @click="createRestaurant">Create a new restaurant</button>
        <button @click="fetchRestaurantList">Show me the restaurants list</button>
        <ul v-if="items.length">
            <li v-for="(item, index) in items" :key="index">{{ item.name }}</li>
        </ul>
        <p v-if="message">{{ message }}</p> <!-- User feedback for operations -->
        <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p> <!-- Error message -->
    </div>
</template>

<script>
import axios from 'axios';
const backendUrl = import.meta.env.VITE_APP_BACKEND_URL


export default {
    name: 'App',
    data() {
        return {
            items: [],
            message: '', // Message for successful operations
            errorMessage: '' // Message for errors
        };
    },
    methods: {
        async fetchRestaurantList() {
            try {
                const response = await axios.get(`${backendUrl}/internal/restaurant/list`);
                this.items = response.data;
                this.message = 'Fetched restaurant list successfully!'; // Success message
            } catch (error) {
                console.error('Error fetching the list:', error);
                this.errorMessage = 'Failed to fetch the restaurant list.'; // Error message
            }
        },

        async createRestaurant() {
            try {
                const response = await axios.post(`${backendUrl}/internal/restaurant/create`, {
                    name: "Güerrín",
                    latitude: "-34.6036844",
                    longitude: "-58.3815591",
                    address: "Av. Corrientes 1368",
                    phone_number: "011 4371-8141",
                    email: "guerrin@gmail.com",
                    instagram: "guerrinoficial",
                    timetable: {
                        timetable: {
                            Friday: [
                                {
                                    closing_time: "20:00",
                                    opening_time: "08:00"
                                }
                            ],
                            Monday: [
                                {
                                    closing_time: "20:00",
                                    opening_time: "12:00"
                                }
                            ],
                            Saturday: [
                                {
                                    closing_time: "20:00",
                                    opening_time: "08:00"
                                }
                            ],
                            Sunday: [
                                {
                                    closing_time: "20:00",
                                    opening_time: "08:00"
                                }
                            ],
                            Thursday: [
                                {
                                    closing_time: "15:00",
                                    opening_time: "08:00"
                                },
                                {
                                    closing_time: "20:00",
                                    opening_time: "16:00"
                                }
                            ],
                            Tuesday: [
                                {
                                    closing_time: "19:00",
                                    opening_time: "13:00"
                                }
                            ]
                        }
                    }
                });
                console.log('Restaurant created:', response.data);
                this.message = 'Restaurant created successfully!'; // Success message
                this.errorMessage = ''; // Clear error message if creation is successful
            } catch (error) {
                console.error('Error creating the restaurant:', error);
                this.errorMessage = 'Failed to create the restaurant.'; // Error message
                this.message = ''; // Clear success message if creation fails
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
