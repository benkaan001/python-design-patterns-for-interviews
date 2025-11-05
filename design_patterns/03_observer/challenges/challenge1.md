# Challenge: Weather Station Monitoring

## 📝 Scenario

You are building a weather monitoring system. A central `WeatherStation` collects real-time temperature, humidity, and pressure data. Multiple display units (e.g., a `CurrentConditionsDisplay`, a `StatisticsDisplay`, and a `ForecastDisplay`) need to update themselves whenever new weather data is available from the `WeatherStation`.

Your goal is to design this system such that the `WeatherStation` doesn't need to know the concrete types of display units. It should simply notify any interested display units about new data, and each display unit should update itself accordingly.

## 🚀 Your Task

Implement this weather monitoring system using the  **Observer Pattern** .

### Requirements:

1. **Subject (Publisher):**
   * Define a `WeatherStation` class that acts as the Concrete Subject.
   * It must maintain a list of registered observers.
   * It must have `register_observer(observer: Observer) -> None` and `remove_observer(observer: Observer) -> None` methods.
   * It must have a `notify_observers() -> None` method that calls the `update()` method on all registered observers.
   * It should have a `set_measurements(temperature: float, humidity: float, pressure: float) -> None` method. When new measurements are set, it should automatically call `notify_observers()`.
2. **Observer (Subscriber) Interface:**
   * Define an abstract class `Observer` with an abstract method `update(temperature: float, humidity: float, pressure: float) -> None`.
3. **Display Elements (Concrete Observers):**
   * Define a `CurrentConditionsDisplay` class that implements `Observer`. Its `update()` method should print the current temperature and humidity.
   * Define a `StatisticsDisplay` class that implements `Observer`. Its `update()` method should keep track of the min, max, and average temperature, and print these statistics.
   * Define a `ForecastDisplay` class that implements `Observer`. Its `update()` method should print a simple weather forecast based on temperature (e.g., "Warm weather expected!" if temp > 25, "Cooler weather coming!" if temp < 10).

## 💡 Hints:

* Remember to use `abc.ABC` and `@abstractmethod` where appropriate.
* The `WeatherStation` should store the current measurements internally so that observers can potentially pull them, but for this challenge, you can directly pass them in the `update` method as specified.
* Focus on the loose coupling: the `WeatherStation` should not import or know about `CurrentConditionsDisplay`, `StatisticsDisplay`, or `ForecastDisplay`.

Good luck!
