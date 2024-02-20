import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate sensor data for 30 days
dates = pd.date_range(start="2023-12-12", periods=30)
soil_moisture = np.random.uniform(20, 60, size=30)  # Simulated soil moisture levels
temperature = np.random.uniform(10, 30, size=30)  # Simulated temperature values
humidity = np.random.uniform(30, 80, size=30)  # Simulated humidity levels

# Create a DataFrame
sensor_data = pd.DataFrame({
    "Date": dates,
    "Soil Moisture (%)": soil_moisture,
    "Temperature (°C)": temperature,
    "Humidity (%)": humidity
}).set_index("Date")

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(sensor_data.index, sensor_data["Soil Moisture (%)"], label="Soil Moisture", marker='o')
plt.plot(sensor_data.index, sensor_data["Temperature (°C)"], label="Temperature", marker='s')
plt.plot(sensor_data.index, sensor_data["Humidity (%)"], label="Humidity", marker='^')
plt.title("Sensor Data Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Hypothetical accuracy scores
conditions = ['Without Sensor Data', 'With Sensor Data']
accuracy_scores = [0.75, 0.90]  # Example accuracy scores

# Plotting
plt.figure(figsize=(6, 4))
plt.bar(conditions, accuracy_scores, color=['skyblue', 'lightgreen'])
plt.title("Response Accuracy Comparison")
plt.xlabel("Condition")
plt.ylabel("Accuracy Score")
plt.ylim(0, 1)  # Accuracy ranges from 0 to 1
plt.tight_layout()
plt.show()

# Example data
metrics = ['Response Time (s)', 'User Satisfaction Score']
values = [1.2, 4.5]  # Example response time in seconds and user satisfaction score out of 5

# Plotting
plt.figure(figsize=(6, 4))
plt.bar(metrics, values, color=['orange', 'purple'])
plt.title("System Usability Metrics")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
