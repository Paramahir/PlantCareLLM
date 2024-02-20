import openai

def get_model_response(api_key, query, sensor_data):
    """
    Queries the GPT-3.5-turbo model with a given query and sensor data, and returns the response.
    """
    openai.api_key = api_key

    try:
        # Include relevant sensor data in the query prompt
        prompt = f"Sensor Data: Soil Moisture: {sensor_data['soil_moisture']}%, Temperature: {sensor_data['temperature']}°C, Humidity: {sensor_data['humidity']}%. {query}"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"An error occurred: {str(e)}"

common_questions = [
    "What is the current soil moisture level?",
    "What is the current temperature?",
    "What is the current humidity?",
    "How often should I water plants based on the sensor data?",
    "How does the current humidity affect plant growth?"
]

def get_common_responses(api_key, sensor_data):
    """
    Generates responses for a set of predefined common questions based on the sensor data.
    """
    responses = {}
    for question in common_questions:
        responses[question] = get_model_response(api_key, question, sensor_data)
    return responses
