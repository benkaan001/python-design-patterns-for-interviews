# 03. Observer Pattern

## 🎯 Type

Behavioral Design Pattern

## 🤔 The "Why": Problem Solved

Imagine you have an object (let's call it the "Subject") whose state changes frequently, and many other objects (the "Observers") are interested in these changes. For instance:

* **News Feed:** A news agency (Subject) publishes new articles, and many subscribers (Observers) need to be notified instantly.
* **Stock Market:** A stock price (Subject) changes, and various trading algorithms or UI widgets (Observers) need to react to the new price.

The naive approach would be for the Subject to know about and directly call methods on all its interested Observers. This leads to  **tight coupling** ,  **lack of flexibility** , and  **scalability issues** .

The Observer pattern solves this by defining a **one-to-many dependency** between objects. When the Subject's state changes, all its dependents are notified and updated automatically, without the Subject needing to know their concrete classes.

## 💡 The "What": Pattern Explanation

The Observer pattern defines a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.

### Key Components:

1. **Subject (Publisher):**
   * Maintains a list of its dependents (observers).
   * Provides methods for attaching (`attach()`) and detaching (`detach()`) Observer objects.
   * Notifies its observers of state changes by calling their `update()` method.
2. **Observer (Subscriber):**
   * Defines an updating interface (`update()`) for objects that should be notified of changes in a Subject.
   * Concrete Observers implement this interface to perform specific actions when notified.
3. **Concrete Subject:**
   * Stores the state of interest to Concrete Observers.
   * Sends a notification to its observers when its state changes.
4. **Concrete Observer:**
   * Implements the Observer updating interface and reacts to notifications.

### Benefits:

* **Loose Coupling:** Subject and Observer only need to know about each other's abstract interfaces.
* **Extensibility:** You can add new Concrete Observers without modifying the Subject.
* **Runtime Flexibility:** Observers can be attached and detached dynamically at runtime.

### When to Use / Avoid:

* **Use when:** A change to one object requires changing others, and you want to avoid tight coupling between the sender and receiver of notifications.
* **Avoid when:** The update logic is very simple and direct coupling is acceptable, or you need strict control over the order of notifications.

## 🐍 Initial Example (Python): Simple Stock Price Monitor (Push Model)

```py
from abc import ABC, abstractmethod
from typing import List

# 1. Observer (Subscriber) Interface (PUSH MODEL)
class Observer(ABC):
    """
    The Observer interface declares the update method, receiving data directly.
    """
    @abstractmethod
    def update(self, symbol: str, price: float, volume: int) -> None:
        """
        Receives updated stock data from the subject (Push Model).
        """
        pass

# 2. Subject (Publisher) Interface
class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about an event."""
        pass

# 3. Concrete Subject
class StockMarket(Subject):
    """
    The Concrete Subject owns some state (stock price) and notifies its observers.
    """
    _observers: List[Observer] = []
    _symbol: str = "XYZ"
    _price: float = 0.0
    _volume: int = 0

    def attach(self, observer: Observer) -> None:
        print(f"Subject: Attached an observer: {observer.__class__.__name__}")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"Subject: Detached an observer: {observer.__class__.__name__}")

    def notify(self) -> None:
        """
        Trigger an update on each subscribed observer by PUSHING the data.
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            # PUSHING all necessary data to the observer
            observer.update(self._symbol, self._price, self._volume)

    def set_price_update(self, new_price: float, new_volume: int) -> None:
        """
        When the price changes, update state and notify observers.
        """
        print(f"\nSubject: Price update received for {self._symbol}: ${new_price:.2f} (Volume: {new_volume})")
        self._price = new_price
        self._volume = new_volume
        self.notify()

# 4. Concrete Observers
class TradingAlgorithm(Observer):
    """
    Reacts to price changes to make trading decisions.
    """
    def update(self, symbol: str, price: float, volume: int) -> None:
        if price > 105.0 and volume > 1000:
            print(f"TradingAlgorithm: SELL Alert for {symbol} (High Price/Volume).")
        elif price < 95.0:
            print(f"TradingAlgorithm: BUY Alert for {symbol} (Low Price).")
        else:
            print(f"TradingAlgorithm: Holding {symbol} ({price}).")

class UIWidget(Observer):
    """
    Updates a UI display with the new price.
    """
    def update(self, symbol: str, price: float, volume: int) -> None:
        print(f"UIWidget: Displaying new price for {symbol}: ${price:.2f} (Volume: {volume})")

# --- Usage ---
if __name__ == "__main__":
    stock_market = StockMarket()

    trading_algo = TradingAlgorithm()
    ui_widget = UIWidget()

    stock_market.attach(trading_algo)
    stock_market.attach(ui_widget)

    stock_market.set_price_update(100.0, 500)
    stock_market.set_price_update(90.0, 1500)

    stock_market.detach(ui_widget) # UI widget no longer receives updates
    stock_market.set_price_update(110.0, 1200)

    # Add another observer dynamically
    class VolumeAlert(Observer):
        def update(self, symbol: str, price: float, volume: int) -> None:
            if volume > 1150:
                print(f"VolumeAlert: High trading volume ({volume}) detected for {symbol}.")

    alert_system = VolumeAlert()
    stock_market.attach(alert_system)
    stock_market.set_price_update(109.5, 1300)

```
