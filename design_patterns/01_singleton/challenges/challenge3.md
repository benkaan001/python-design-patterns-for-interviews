# Challenge: Thread-Safe Singleton for a Resource Pool

## 📝 Scenario

You are developing a high-performance backend service that needs to manage a limited pool of expensive resources, such as database connections or network sockets. To optimize performance and prevent resource exhaustion, you decide to implement a `ResourcePool` class that ensures **only one instance** of the pool exists throughout the application.

However, your service is multi-threaded, meaning multiple parts of your application might try to access or initialize this `ResourcePool` concurrently from different threads. If not handled carefully, this can lead to race conditions where multiple `ResourcePool` instances are inadvertently created, violating the Singleton principle.

## 🚀 Your Task

Implement a `ThreadSafeResourcePool` class using the  **Singleton pattern** , ensuring it is robust against concurrent instantiation attempts from multiple threads.

### Requirements:

1. **Singleton Enforcement:** Ensure that only one instance of the `ThreadSafeResourcePool` class can ever be created, even under heavy concurrent access.
2. **Thread-Safety:** The `__new__` method (or any part of the instance creation logic) must be thread-safe to prevent multiple instances from being created simultaneously.
3. **Delayed Initialization:** The `__init__` method should perform a "heavy" initialization (e.g., simulating resource allocation with `time.sleep(0.1)`) *only the first time* the instance is truly initialized. Use a flag to prevent re-initialization.
4. **Resource Management (Simulated):**
   * The pool should internally manage a fixed number of "resources" (e.g., a list of strings like `["Resource-1", "Resource-2"]`).
   * Implement a method `acquire_resource() -> str` that simulates acquiring a resource from the pool. It should return the resource string. For simplicity, you can just pop from the list.
   * Implement a method `release_resource(resource: str) -> None` that simulates returning a resource to the pool. It should add the resource back to the list.
   * Add a method `get_pool_status() -> str` that returns a string indicating the current number of available resources.

## 💡 Hints:

* For thread-safety in Python, you'll typically use `threading.Lock`.
* The lock should be acquired *before* checking if the instance exists in `__new__` and released after the instance is set.
* Remember the `_initialized` flag in `__init__` for one-time setup.
* You can use `time.sleep()` to simulate delays.
* To test concurrency, you'll need to create multiple threads that attempt to get the `ThreadSafeResourcePool` instance and acquire/release resources.

Good luck, this is a more challenging one!
