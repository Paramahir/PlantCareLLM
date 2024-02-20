# PlantCareLLM

Welcome to PlantCareLLM, a Flask-based web application designed to assist in the care and monitoring of plants through sensor data analysis. This application simulates sensor data to provide insights into soil moisture, temperature, and humidity, and integrates with a model to offer guidance and answers to common plant care questions.

## Features

- **Sensor Data Simulation**: Utilizes simulated sensor data to mimic real-time soil moisture, temperature, and humidity readings.
- **Data Visualization**: Offers visual representation of sensor data trends over time, helping users understand environmental conditions.
- **Interactive Q&A**: Users can ask questions related to plant care, and the system provides responses based on the simulated sensor data, leveraging the GPT-3.5-turbo model for generating answers.
- **Responsive Web Interface**: A user-friendly web interface that displays sensor data and allows users to interact with the system by asking questions and receiving guidance.

## Technologies Used

- **Flask**: A micro web framework written in Python, used for building the web application.
- **OpenAI GPT-3.5-turbo**: Integrated for generating intelligent responses to user queries based on sensor data.
- **JavaScript**: Enhances the web interface with dynamic content and interactivity.
- **HTML/CSS**: Structures and styles the web application's interface.

## Getting Started

To get started with PlantCareLLM, clone the repository and ensure you have Python installed on your system. Install the required dependencies, and run the Flask application to start the web server.

## Requirement - For Running this project after cloning you have to include OPENAI API Key in the app.py file. Please check official openai document to know how to get that file.

```bash
git clone https://github.com/Paramahir/PlantCareLLM.git
cd PlantCareLLM
pip install -r requirements.txt  
python PlantCareProject/app.py
```

## Navigate to http://localhost:5000 in your web browser to access the application.

## Contributing
Contributions to PlantCareLLM are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.
