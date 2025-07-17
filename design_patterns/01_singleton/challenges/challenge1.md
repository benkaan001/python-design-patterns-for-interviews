# Challenge: The Logger System

## 📝 Scenario

You are tasked with building a simple logging system for an application. This logger should allow different parts of the application to write log messages (e.g., `info`, `warning`, `error`).

Crucially,  **all log messages must go to a single, shared log (simulated as an in-memory list for this exercise)** , and there should only ever be one instance of the logger class managing this process. This ensures consistency and avoids potential issues with multiple loggers trying to write to the same resource.

## 🚀 Your Task

Implement a `Logger` class using the  **Singleton pattern** .

### Requirements:

1. The `Logger` class must ensure **only one instance** of itself exists throughout the application's runtime.
2. The `__init__` method should perform a "heavy" initialization (e.g., simulating a setup process with `time.sleep(0.5)`) *only the first time* the instance is truly initialized. Use a flag to prevent re-initialization on subsequent calls to `Logger()`.
3. All log messages should be appended to an internal **in-memory list** (e.g., `_logs: list[str]`).
4. The `Logger` class should have the following methods:
   * `info(message: str) -> None`: Appends an informational log message.
   * `warning(message: str) -> None`: Appends a warning log message.
   * `error(message: str) -> None`: Appends an error log message.
5. Add a method `get_logs() -> list[str]` that returns a **copy** of all accumulated log messages.

## 💡 Hints:

* Remember to use `__new__` for controlling instance creation.
* Use a flag (e.g., `_initialized`) within `__init__` to prevent re-running setup logic.
* For the "heavy" initialization, you can import `time` and use `time.sleep()`.

Good luck!
