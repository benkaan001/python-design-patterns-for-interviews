from abc import ABC, abstractmethod
from typing import List

# --- 1. Observer (Subscriber) Interface ---
class Observer(ABC):
    """
    The Observer interface declares the update method, which concrete observers
    must implement to receive data from the subject.
    """
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        """
        Receives updated weather measurements from the subject.
        """
        pass

# --- Subject (Publisher) Interface ---
# (Optional, but good practice to define abstract Subject for consistency)
class Subject(ABC):
    """
    The Subject interface declares methods for managing observers.
    """
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        """Registers an observer to receive updates."""
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        """Removes an observer from the subscription list."""
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """Notifies all registered observers about a state change."""
        pass

# --- 2. Subject (Publisher) - Concrete Implementation ---
class WeatherStation(Subject):
    """
    The Concrete Subject that collects weather data and notifies its observers.
    It stores the current measurements internally.
    """
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    def register_observer(self, observer: Observer) -> None:
        """Adds an observer to the list of subscribers."""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"WeatherStation: Registered {observer.__class__.__name__}.")

    def remove_observer(self, observer: Observer) -> None:
        """Removes an observer from the list of subscribers."""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"WeatherStation: Removed {observer.__class__.__name__}.")

    def notify_observers(self) -> None:
        """
        Notifies all registered observers by pushing the current measurements.
        """
        print(f"\nWeatherStation: Notifying observers about new measurements...")
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        """
        Updates the weather measurements and triggers notification to observers.
        """
        print(f"\nWeatherStation: New measurements received - Temp: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure}hPa")
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

# --- 3. Display Elements (Concrete Observers) ---
class CurrentConditionsDisplay(Observer):
    """
    Displays the current temperature and humidity.
    """
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        """Updates and prints the current conditions."""
        print(f"  CurrentConditionsDisplay: Temp: {temperature:.1f}°C, Humidity: {humidity:.1f}%.")

class StatisticsDisplay(Observer):
    """
    Calculates and displays min, max, and average temperature.
    """
    def __init__(self) -> None:
        self._temperatures: List[float] = []
        self._min_temp: float = float('inf')
        self._max_temp: float = float('-inf')
        self._sum_temp: float = 0.0
        self._num_readings: int = 0

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        """Updates statistics and prints them."""
        self._temperatures.append(temperature) # Keep for simple average calculation

        # Update min/max
        if temperature < self._min_temp:
            self._min_temp = temperature
        if temperature > self._max_temp:
            self._max_temp = temperature

        # Update for average using sum/count for robustness
        self._sum_temp += temperature
        self._num_readings += 1
        avg_temp = self._sum_temp / self._num_readings if self._num_readings > 0 else 0.0

        print(f"  StatisticsDisplay: Avg Temp: {avg_temp:.1f}°C, Min Temp: {self._min_temp:.1f}°C, Max Temp: {self._max_temp:.1f}°C.")

class ForecastDisplay(Observer):
    """
    Provides a simple weather forecast based on temperature.
    """
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        """Updates and prints the forecast."""
        forecast = "No forecast available."
        if temperature > 25:
            forecast = "Warm weather expected!"
        elif temperature < 10:
            forecast = "Cooler weather coming!"
        else:
            forecast = "Mild weather ahead."
        print(f"  ForecastDisplay: {forecast}")

# --- Usage Example ---
if __name__ == "__main__":
    # Create the Weather Station (Subject)
    weather_station = WeatherStation()

    # Create the display units (Observers)
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()

    # Register the observers with the subject
    print("--- Registering Observers ---")
    weather_station.register_observer(current_display)
    weather_station.register_observer(stats_display)
    weather_station.register_observer(forecast_display)

    # Simulate new weather measurements (triggers notifications)
    print("\n--- First Measurement Update ---")
    weather_station.set_measurements(24.5, 65.0, 1013.1)

    print("\n--- Second Measurement Update (Warm Weather) ---")
    weather_station.set_measurements(28.0, 70.0, 1012.8)

    # Remove an observer
    print("\n--- Removing Statistics Display ---")
    weather_station.remove_observer(stats_display)

    print("\n--- Third Measurement Update (Cool Weather) ---")
    weather_station.set_measurements(8.2, 85.5, 1015.0)

    # Add back an observer
    print("\n--- Re-registering Statistics Display ---")
    weather_station.register_observer(stats_display)

    print("\n--- Fourth Measurement Update (Mild Weather) ---")
    weather_station.set_measurements(18.0, 60.0, 1014.5)

"""
--- Registering Observers ---
WeatherStation: Registered CurrentConditionsDisplay.
WeatherStation: Registered StatisticsDisplay.
WeatherStation: Registered ForecastDisplay.

--- First Measurement Update ---

WeatherStation: New measurements received - Temp: 24.5°C, Humidity: 65.0%, Pressure: 1013.1hPa

WeatherStation: Notifying observers about new measurements...
  CurrentConditionsDisplay: Temp: 24.5°C, Humidity: 65.0%.
  StatisticsDisplay: Avg Temp: 24.5°C, Min Temp: 24.5°C, Max Temp: 24.5°C.
  ForecastDisplay: Mild weather ahead.

--- Second Measurement Update (Warm Weather) ---

WeatherStation: New measurements received - Temp: 28.0°C, Humidity: 70.0%, Pressure: 1012.8hPa

WeatherStation: Notifying observers about new measurements...
  CurrentConditionsDisplay: Temp: 28.0°C, Humidity: 70.0%.
  StatisticsDisplay: Avg Temp: 26.2°C, Min Temp: 24.5°C, Max Temp: 28.0°C.
  ForecastDisplay: Warm weather expected!

--- Removing Statistics Display ---
WeatherStation: Removed StatisticsDisplay.

--- Third Measurement Update (Cool Weather) ---

WeatherStation: New measurements received - Temp: 8.2°C, Humidity: 85.5%, Pressure: 1015.0hPa

WeatherStation: Notifying observers about new measurements...
  CurrentConditionsDisplay: Temp: 8.2°C, Humidity: 85.5%.
  ForecastDisplay: Cooler weather coming!

--- Re-registering Statistics Display ---
WeatherStation: Registered StatisticsDisplay.

--- Fourth Measurement Update (Mild Weather) ---

WeatherStation: New measurements received - Temp: 18.0°C, Humidity: 60.0%, Pressure: 1014.5hPa

WeatherStation: Notifying observers about new measurements...
  CurrentConditionsDisplay: Temp: 18.0°C, Humidity: 60.0%.
  ForecastDisplay: Mild weather ahead.
  StatisticsDisplay: Avg Temp: 23.5°C, Min Temp: 18.0°C, Max Temp: 28.0°C.
"""