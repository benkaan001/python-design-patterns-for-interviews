from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        """Simulate sending a notification and return a confirmation string."""
        pass

class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending email: {message}"

class SMSNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending SMS: {message}"

class PushNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending push notification: {message}"


class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        """Factory method to create a Notification object."""
        pass

    def dispatch_notification(self, message: str) -> str:
        notification = self.create_notification()
        return notification.send(message)  # Return only the send result for clarity

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()

class PushNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return PushNotification()


if __name__ == "__main__":
    creators = [
        EmailNotificationCreator(),
        SMSNotificationCreator(),
        PushNotificationCreator()
    ]
    messages = [
        "Welcome to our platform!",
        "Your code is 123456.",
        "You have a new follower!"
    ]
    for creator, msg in zip(creators, messages):
        print(creator.dispatch_notification(msg))