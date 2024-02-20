import random
from datetime import datetime

class SimulatedSensor:
    def __init__(self):
        self.base_moisture = None  # Initialize to None
        self.base_temperature = None  # Initialize to None
        self.base_humidity = None  # Initialize to None
        self.moisture_fluctuation = 5
        self.temperature_fluctuation = 3
        self.humidity_fluctuation = 10
        self.last_read_time = None  # Initialize to None

    def _simulate_realistic_variation(self, base_value, fluctuation):
        current_time = datetime.now()
        if self.last_read_time is None:
            # Handle the case where last_read_time is None
            self.last_read_time = current_time
            return base_value

        time_diff = (current_time - self.last_read_time).total_seconds() / 3600
        variation = random.uniform(-fluctuation, fluctuation) * (time_diff / 2)
        new_value = base_value + variation
        return new_value

    def read_soil_moisture(self):
        if self.base_moisture is None:
            # Initialize base_moisture with a default value when None
            self.base_moisture = 30
        self.base_moisture = self._simulate_realistic_variation(self.base_moisture, self.moisture_fluctuation)
        return max(0, min(100, self.base_moisture))

    def read_temperature(self):
        if self.base_temperature is None:
            # Initialize base_temperature with a default value when None
            self.base_temperature = 20
        self.base_temperature = self._simulate_realistic_variation(self.base_temperature, self.temperature_fluctuation)
        return self.base_temperature

    def read_humidity(self):
        if self.base_humidity is None:
            # Initialize base_humidity with a default value when None
            self.base_humidity = 50
        if self.base_temperature is not None:
            if self.base_temperature > 25:
                self.base_humidity -= 0.5
            else:
                self.base_humidity += 0.5
        self.base_humidity = self._simulate_realistic_variation(self.base_humidity, self.humidity_fluctuation)
        return max(0, min(100, self.base_humidity))

    def get_sensor_data(self):
        current_time = datetime.now()
        if self.last_read_time is None:
            # Initialize last_read_time when None
            self.last_read_time = current_time
        return {
            "timestamp": current_time.isoformat(),
            "soil_moisture": self.read_soil_moisture(),
            "temperature": self.read_temperature(),
            "humidity": self.read_humidity()
        }

# Global instance of SimulatedSensor
sensor = SimulatedSensor()

def collect_and_process_data():
    """
    Collects and returns the simulated sensor data.
    """
    return sensor.get_sensor_data()
