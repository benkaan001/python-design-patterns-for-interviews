# Challenge: Thread-Safe Singleton for a Resource Pool

## 📝 Scenario

You are developing a high-performance backend service that needs to manage a limited pool of expensive resources, such as database connections or network sockets. To optimize performance and prevent resource exhaustion, you decide to implement a `ResourcePool` class that ensures **only one instance** of the pool exists throughout the application.

However, your service is multi-threaded, meaning multiple parts of your application might try to access or initialize this `ResourcePool` concurrently from different threads. If not handled carefully, this can lead to race conditions where multiple `ResourcePool` instances are inadvertently created, violating the Singleton principle.

## 🚀 Your Task

Implement a `ThreadSafeResourcePool` class using the  **Singleton pattern** , ensuring it is robust against concurrent instantiation attempts from multiple threads.

### Requirements:

1. **Singleton Enforcement:** Ensure that only one instance of the `ThreadSafeResourcePool` class can ever be created, even under heavy concurrent access.
2. **Thread-Safety:** The `__new__` method must be thread-safe to prevent multiple instances from being created simultaneously.
3. **One-Time Initialization (Crucial Nuance):** The critical, one-time initialization of the pool's internal state (`available_resources`, etc.) **must occur atomically** and **immediately after** the instance is created.
4. **Resource Management (Thread-Safe):**
   * The pool should internally manage a list of simulated resources (e.g., strings like `"Res-1"`).
   * Implement a method `acquire_resource() -> str` that safely takes a resource from the pool's list. If the pool is empty, it must raise a `ValueError`.
   * Implement a method `release_resource(resource: str) -> None` that safely returns a resource to the pool's list.
   * Implement a method `get_pool_status() -> str` that returns a string indicating the current number of available resources and resources in use.

### Test Harness Requirement:

5. **Test Concurrency:** Write a multi-threaded test harness (`if __name__ == "__main__":` block) that:
   * Defines a `worker_function` for threads to run.
   * Creates at least 5 separate threads that **simultaneously attempt to get the `ThreadSafeResourcePool` instance** and immediately try to  **acquire and release a resource** .
   * Uses `thread.join()` to ensure the main program waits for all worker threads to complete before verifying the final state.

## 💡 Hints (Addressing Interview Nuances):

* **Synchronization:** Use a **`threading.Lock`** as a class attribute to protect the critical sections.
* **Double-Checked Locking (DCL):** For performance and safety, your `__new__` method **must check the instance variable twice** (once outside the lock, and once inside) before creation.
* **Atomic Initialization:** For the most robust solution, combine instance creation and one-time initialization:  **Place the resource setup logic inside the DCL's inner lock block in `__new__`** , not in `__init__`.
* **The `__init__` Method:** In this specific thread-safe pattern, you should  **leave `__init__` empty (`pass`)** . Attempting to use the `__init__` method for complex, one-time setup risks subtle race conditions between checking the `_initialized` flag and setting it.
* **Resource Methods:** Ensure that `acquire_resource` and `release_resource` also use the instance's lock to protect the resource lists from concurrent modification.

Good luck, this is a more challenging one!
