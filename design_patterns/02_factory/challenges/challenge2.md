# Challenge: Notification System

## 📝 Scenario

You're designing a notification service for a large online platform (like an e-commerce site or social media). Users need to receive various types of alerts (e.g., order confirmations, password reset links, marketing promotions). These notifications can be sent via different channels:  **Email** ,  **SMS** , or  **Push Notifications** .

Your task is to build a flexible system where the core logic that *dispatches* a notification doesn't need to know the specifics of *how* an email is sent versus an SMS or a push notification. The system should be easily extensible to support new notification channels (e.g., in-app notifications, voice calls) in the future without modifying the existing dispatching code.

## 🚀 Your Task

Implement this notification system using the  **Factory Method Pattern** .

### Requirements:

1. **Product (Abstract):**
   * Define an abstract class `Notification` with an abstract method `send(message: str) -> str`. This method should simulate sending a notification and return a string confirming the action.
2. **Concrete Products:**
   * `EmailNotification`: Implements `send()`, returning `f"Sending email: {message}"`.
   * `SMSNotification`: Implements `send()`, returning `f"Sending SMS: {message}"`.
   * `PushNotification`: Implements `send()`, returning `f"Sending push notification: {message}"`.
3. **Creator (Abstract):**
   * Define an abstract class `NotificationCreator` with:
     * An abstract **factory method** `create_notification() -> Notification`. This method will be overridden by subclasses to create specific notification types.
     * A concrete (non-abstract) method `dispatch_notification(message: str) -> str`. This method should encapsulate the client-side logic: it calls `create_notification()` to get a `Notification` object and then calls `send(message)` on that object. This method should return the result of the `send` call.
4. **Concrete Creators:**
   * `EmailNotificationCreator`: Overrides `create_notification()` to return an `EmailNotification`.
   * `SMSNotificationCreator`: Overrides `create_notification()` to return an `SMSNotification`.
   * `PushNotificationCreator`: Overrides `create_notification()` to return a `PushNotification`.

## 💡 Hints:

* Remember the  **Open/Closed Principle** . Your `dispatch_notification` method (the client-facing logic) should remain *closed for modification* even if you later introduce a `VoiceCallNotification` channel. The Factory Method allows you to achieve this by being *open for extension* (you just add new Concrete Products and Concrete Creators).
* Use `abc.ABC` and `@abstractmethod` for your abstract classes and methods.

Good luck!
