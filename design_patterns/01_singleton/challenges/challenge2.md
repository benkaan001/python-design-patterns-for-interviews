# Challenge: Application Settings Manager

## 📝 Scenario

You are building a desktop application, and it needs a central way to manage user preferences and application settings (e.g., theme preference, default save directory, recent files list). These settings need to be loaded once at application startup and be accessible from various UI components and backend services throughout the application's lifecycle. There should only ever be **one instance** of this settings manager.

## 🚀 Your Task

Implement an `ApplicationSettings` class using the  **Singleton pattern** .

### Requirements:

1. **Singleton Enforcement:** Ensure that only one instance of the `ApplicationSettings` class can ever be created.
2. **Delayed Initialization (Simulated):** The `__init__` method should perform a "heavy" initialization (e.g., simulating loading from a file or a network call with `time.sleep(1)`) *only the first time* the instance is truly initialized. Use a flag to prevent re-initialization on subsequent calls to `ApplicationSettings()`.
3. **Setting Storage:** The settings should be stored in an internal dictionary (e.g., `_settings: dict[str, Any]`).
4. **Methods for Interaction:**
   * `get_setting(key: str) -> Any`: Retrieves a setting by its key. If the key is not found, it should raise a `KeyError`.
   * `set_setting(key: str, value: Any) -> None`: Updates an existing setting or adds a new one.
   * `get_all_settings() -> dict[str, Any]`: Returns a **copy** of the internal settings dictionary to prevent external direct modification.

## 💡 Hints:

* Recall the use of `__new__` for controlling instance creation.
* Remember the `_initialized` flag in `__init__` to ensure one-time setup.
* For the "heavy" initialization, you can import `time` and use `time.sleep()`.
* For initial settings, you can populate the `_settings` dictionary with some dummy data like `{"theme": "dark", "default_path": "/home/user/documents", "recent_files": []}`.

Good luck!
