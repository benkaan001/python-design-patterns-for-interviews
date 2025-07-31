# 03. Observer Pattern

## 🎯 Type

Behavioral Design Pattern

## 🤔 The "Why": Problem Solved

Imagine you have an object (let's call it the "Subject") whose state changes frequently, and many other objects (the "Observers") are interested in these changes. For instance:

* **News Feed:** A news agency (Subject) publishes new articles, and many subscribers (Observers) need to be notified instantly.
* **Stock Market:** A stock price (Subject) changes, and various trading algorithms or UI widgets (Observers) need to react to the new price.
* **UI Elements:** A button (Subject) is clicked, and multiple listeners (Observers) need to perform actions (e.g., update text, play sound, open a new window).

The naive approach would be for the Subject to know about and directly call methods on all its interested Observers. This leads to:

* **Tight Coupling:** The Subject becomes tightly coupled to concrete Observer classes. Adding, removing, or changing an Observer requires modifying the Subject.
* **Lack of Flexibility:** It's hard to dynamically add or remove Observers at runtime.
* **Scalability Issues:** As the number of Observers grows, managing direct dependencies becomes unwieldy.

The Observer pattern solves this by defining a **one-to-many dependency** between objects. When the Subject's state changes, all its dependents are notified and updated automatically, without the Subject needing to know their concrete classes.

## 💡 The "What": Pattern Explanation

The Observer pattern defines a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.

### Key Components:

1. **Subject (Publisher):**
   * Maintains a list of its dependents (observers).
   * Provides methods for attaching (`attach()`) and detaching (`detach()`) Observer objects.
   * Notifies its observers of state changes by calling their `update()` method.
2. **Observer (Subscriber):**
   * Defines an updating interface for objects that should be notified of changes in a Subject.
   * Concrete Observers implement this interface to perform specific actions when notified.
3. **Concrete Subject:**
   * Stores the state of interest to Concrete Observers.
   * Sends a notification to its observers when its state changes.
4. **Concrete Observer:**
   * Stores a reference to the Concrete Subject.
   * Implements the Observer updating interface.
   * Reacts to notifications from the Subject.

### Benefits:

* **Loose Coupling:** Subject and Observer are loosely coupled. They only need to know about each other's abstract interfaces, not concrete implementations.
* **Extensibility:** You can add new Concrete Observers without modifying the Subject.
* **Reusability:** Observers can be reused with different Subjects.
* **Runtime Flexibility:** Observers can be attached and detached dynamically at runtime.

### When to Use / Avoid:

* **Use when:**
  * A change to one object requires changing others, and you don't know how many objects need to be changed.
  * An object should be able to notify other objects without making assumptions about who these objects are.
  * You want to avoid tight coupling between the sender and receiver of notifications.
* **Avoid when:**
  * The update logic is very simple and direct coupling is acceptable.
  * The overhead of managing subscriptions is too high for the benefit.
  * You need strict control over the order of notifications (Observer pattern doesn't guarantee order).

## 🐍 Initial Example (Python): Simple Stock Price Monitor

```py
from abc import ABC, abstractmethod
from typing import List

# 1. Observer (Subscriber) Interface
class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        """
        Receive update from subject.
        """
        pass

# 2. Subject (Publisher) Interface
class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

# 3. Concrete Subject
class StockMarket(Subject):
    """
    The Concrete Subject owns some state and notifies its observers when its
    state changes.
    """
    _observers: List[Observer] = []
    _price: float = 0.0

    def attach(self, observer: Observer) -> None:
        print(f"Subject: Attached an observer: {observer.__class__.__name__}")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"Subject: Detached an observer: {observer.__class__.__name__}")

    def notify(self) -> None:
        """
        Trigger an update on each subscribed observer.
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    @property
    def price(self) -> float:
        """
        For observers to pull the state from the subject.
        """
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        When the price changes, notify observers.
        """
        print(f"\nSubject: Price changed from {self._price} to {new_price}")
        self._price = new_price
        self.notify()

# 4. Concrete Observers
class TradingAlgorithm(Observer):
    """
    Reacts to price changes to make trading decisions.
    """
    def update(self, subject: Subject) -> None:
        if isinstance(subject, StockMarket):
            if subject.price > 105.0:
                print(f"TradingAlgorithm: Price is high ({subject.price}), considering selling.")
            elif subject.price < 95.0:
                print(f"TradingAlgorithm: Price is low ({subject.price}), considering buying.")
            else:
                print(f"TradingAlgorithm: Price is stable ({subject.price}), holding.")

class UIWidget(Observer):
    """
    Updates a UI display with the new price.
    """
    def update(self, subject: Subject) -> None:
        if isinstance(subject, StockMarket):
            print(f"UIWidget: Displaying new price: ${subject.price:.2f}")

# --- Usage ---
if __name__ == "__main__":
    stock_market = StockMarket()

    trading_algo = TradingAlgorithm()
    ui_widget = UIWidget()

    stock_market.attach(trading_algo)
    stock_market.attach(ui_widget)

    stock_market.price = 100.0
    stock_market.price = 90.0

    stock_market.detach(ui_widget) # UI widget no longer receives updates
    stock_market.price = 110.0

    # Add another observer dynamically
    class AlertSystem(Observer):
        def update(self, subject: Subject) -> None:
            if isinstance(subject, StockMarket) and subject.price > 108.0:
                print(f"AlertSystem: HIGH PRICE ALERT! Current price: {subject.price}")

    alert_system = AlertSystem()
    stock_market.attach(alert_system)
    stock_market.price = 109.5

```
