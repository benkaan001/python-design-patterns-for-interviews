# Challenge: Topic-Based Subscription Service

## 📝 Scenario

You are building a dynamic content subscription service (like a newsletter platform or a blog) where users only want to receive updates about specific categories (e.g., "Tech," "Finance," "Gaming").

The standard Observer Pattern needs modification because the **Publisher (Subject)** must not notify *all* observers; it must only notify those observers that are subscribed to the specific **topic** being published.

## 🚀 Your Task

Implement a topic-based notification system using the Observer Pattern to ensure subscribers only receive relevant content.

### Requirements:

1. **Product/Event:** The publisher must send two pieces of information: the `topic` (string) and the `content` (string).
2. **Subscriber Interface (`TopicSubscriber`):**
   * Define an abstract class `TopicSubscriber` with an abstract method `receive_update(topic: str, content: str) -> None`.
3. **Publisher (`TopicPublisher`):**
   * This class must act as the Subject.
   * It must manage subscriptions using a dictionary where the **key is the topic name** (e.g., "Tech") and the  **value is a list of `TopicSubscriber` objects** .
   * Implement `subscribe(observer: TopicSubscriber, topic: str) -> None`.
   * Implement `unsubscribe(observer: TopicSubscriber, topic: str) -> None`.
4. **Publishing Method:**
   * Implement `publish_article(topic: str, content: str) -> None`. This method must iterate only over the list of observers associated with the given `topic` and call `receive_update` on them.
5. **Concrete Subscribers:**
   * `TopicLogger`: Prints a simple log message for every update it receives, including the `topic` and a snippet of `content`.
   * `PriorityNotifier`: Only prints a notification if the `content` contains the keyword "URGENT" or "BREAKING" (case-insensitive).
6. **Test Harness:**
   * Demonstrate that you can subscribe `TopicLogger` to "Tech" and `PriorityNotifier` to "Finance".
   * Publish a "Tech" article (should only notify `TopicLogger`).
   * Publish a "Finance" article with "BREAKING" content (should only notify `PriorityNotifier` and trigger its conditional logic).

## 💡 Hints:

* For managing subscriptions, initialize your publisher with `self._subscriptions: Dict[str, List[TopicSubscriber]] = {}`.
* Ensure your `publish_article` method handles the case where a topic might exist but have no subscribers.

Good luck!
