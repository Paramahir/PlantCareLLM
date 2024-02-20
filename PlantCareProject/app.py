from flask import Flask, request, render_template, jsonify
import data_Collection
import model_integration

app = Flask(__name__, static_url_path='/static')

# Define the route for the root URL ("/") and render the HTML template
@app.route('/')
def home():
    # You can pass data to your HTML template if needed
    data = data_Collection.collect_and_process_data()
    
    # Render the "home.html" template and return it as a response
    return render_template('index.html', data=data)

@app.route('/get_simulated_sensor_data', methods=['GET'])
def get_simulated_sensor_data():
    # Call collect_and_process_data to get the simulated sensor data
    sensor_data = data_Collection.collect_and_process_data()
    
    # Return the sensor data as a JSON response
    return jsonify(sensor_data)

# Define other routes
@app.route('/get_sensor_data', methods=['GET'])
def get_sensor_data():
    # Call collect_and_process_data to get the simulated sensor data
    sensor_data = data_Collection.collect_and_process_data()
    
    # Return the sensor data as a JSON response
    return jsonify(sensor_data)

@app.route('/get_common_responses', methods=['GET'])
def get_common_responses():
    api_key = "00000000000"  # Replace with your OpenAI API key
    sensor_data = data_Collection.collect_and_process_data()
    responses = model_integration.get_common_responses(api_key,sensor_data)
    return jsonify(responses)

@app.route('/ask', methods=['POST'])
def ask():
    api_key = "00000000"  # Replace with your OpenAI API key
    user_query = request.json.get('query')
    
    # Get the simulated sensor data
    sensor_data = data_Collection.collect_and_process_data()
    
    # Pass the sensor data to the model_integration function
    response = model_integration.get_model_response(api_key, user_query, sensor_data)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
