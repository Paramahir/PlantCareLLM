// Update the JavaScript code in script.js

window.onload = function() {
    console.log("Script is running...");

    fetchSensorData();
    loadCommonQuestions(); // Load common questions when the page loads
};

function loadCommonQuestions() {
    // Fetch common questions from your Flask route
    fetch('/get_common_responses')
        .then(response => response.json())
        .then(data => {
            const commonQuestionsList = document.getElementById('commonQuestionsList');
            commonQuestionsList.innerHTML = ''; // Clear any existing content

            // Loop through the common questions and add them to the list
            for (const question in data) {
                const listItem = document.createElement('li');
                listItem.textContent = question + ': ' + data[question];
                commonQuestionsList.appendChild(listItem);
            }
        })
        .catch(error => {
            console.error('Error fetching common questions:', error);
        });
}


function updateSensorData() {
    fetch('/get_simulated_sensor_data')
        .then(response => response.json())
        .then(data => {
            // Update the content of the sensor data display
            document.getElementById('soilMoisture').textContent = data.soil_moisture + '%';
            document.getElementById('temperature').textContent = data.temperature + '°C';
            document.getElementById('humidity').textContent = data.humidity + '%';
        })
        .catch(error => {
            console.error('Error fetching sensor data:', error);
        });
}

// Call the updateSensorData function periodically (e.g., every 5 seconds)
setInterval(updateSensorData, 5000); // 5000 milliseconds = 5 seconds

function fetchSensorData() {
    fetch('/get_sensor_data')
    .then(response => response.json())
    .then(data => {
        document.getElementById('dataDisplay').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error fetching sensor data:', error));
}


function askQuestion() {
    const query = document.getElementById('queryInput').value;
    fetch('/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query: query})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseText').innerText = data.response;
    })
    .catch(error => console.error('Error:', error));
}
