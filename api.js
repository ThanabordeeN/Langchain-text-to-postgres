// FILEPATH: /h:/automation_agent/Project/textoSQL/apitest.jsx
const axios = require('axios');

const fetchData = async () => {
    try {
        // Define the API endpoint URL
        const url = 'http://localhost:5000/query';

        // Define the data to be sent in the request body
        const data = {
            question: 'What is the average salary of employees?',
        };

        // Send the POST request to the API endpoint
        const response = await axios.post(url, data);

        // Check if the response is not empty and is in JSON format
        if (response.data) {
            try {
                // Get the response data
                const resultData = response.data.result;

                // Log the result
                console.log('Result:', resultData);
            } catch (error) {
                console.log('Response is not in JSON format');
            }
        } else {
            console.log('Empty Response');
        }
    } catch (error) {
        console.log('Error:', error);
    }
};

fetchData();
