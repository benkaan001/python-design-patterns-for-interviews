# 01. Singleton Pattern

## 🎯 Type

Creational Design Pattern

## 🤔 The "Why": Problem Solved

The Singleton pattern addresses the need to ensure that a class has **only one instance** throughout the entire application's lifetime. This is crucial when you have a single, centralized resource or service that all parts of your application must share and access consistently.

**Common Scenarios:**

* **Configuration Manager:** Loading application settings once and providing global access.
* **Logger:** Directing all log messages to a single log file or service.
* **Database Connection Pool:** Managing a limited set of database connections efficiently.
* **Print Spooler:** Controlling access to a single printer resource.

Without Singleton, multiple instances could lead to:

* Resource wastage (e.g., multiple database connections).
* Inconsistent state (e.g., different configuration instances holding different values).
* Race conditions or synchronization issues when multiple threads try to access/modify the same logical resource.

## 💡 The "What": Pattern Explanation

The Singleton pattern restricts the instantiation of a class to a single object. It provides a global point of access to that single instance.

### Key Components:

1. **Private Constructor (simulated in Python):** Prevents direct instantiation of the class from outside. In Python, this is typically achieved by overriding `__new__` and controlling instance creation.
2. **Static Method/Class Method to Get Instance:** A method (often named `instance()` or by just calling the class `ClassName()`) that is responsible for creating the single instance if it doesn't exist, and returning the existing instance otherwise.
3. **Static Variable/Class Attribute to Hold Instance:** A class-level variable (e.g., `_instance`) that stores the one and only instance of the class.
4. **Initialization Flag (Optional but Recommended):** A flag (e.g., `_initialized`) within `__init__` to ensure that any setup logic runs only once, as `__init__` is called every time the class is "instantiated" (even if `__new__` returns an existing object).

### Benefits:

* **Controlled Access to Sole Instance:** Guarantees that only one instance exists and provides a well-defined global access point.
* **Reduced Resource Consumption:** Prevents the creation of multiple expensive objects, saving resources like memory or database connections.
* **Centralized Management:** Offers a central point for managing a specific resource or state, simplifying control and modification.
* **Lazy Initialization:** The instance is created only when it's first needed.

### When to Use / Avoid:

* **Use when:** Exactly one instance of a class is needed to coordinate actions across the system.
* **Avoid when:** You need multiple instances, or when the global state introduced by Singleton makes testing difficult or introduces hidden dependencies. Overuse can lead to tightly coupled code.

## 🐍 Initial Example (Python)

Here's a conceptual example of a `ConfigurationManager` using the Singleton pattern. This code is for illustrative purposes within this `README.md` and not part of the challenge.

```py
import time

class ConfigurationManager:
    _instance = None       # Class attribute to hold the single instance
    _initialized = False   # Flag to ensure __init__ runs only once
    _settings = {}         # To store configuration settings

    def __new__(cls):
        if cls._instance is None:
            print("Creating a new ConfigurationManager instance...")
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
        else:
            print("Using existing ConfigurationManager instance...")
        return cls._instance

    def __init__(self):
        if not self._initialized:
            print("ConfigurationManager initializing settings (first time only)...")
            # Simulate heavy initialization, e.g., loading from a file
            time.sleep(0.5)
            self._settings = {
                "database_url": "sqlite://my_database.db",
                "log_level": "INFO",
                "api_key": "YOUR_SUPER_SECRET_KEY"
            }
            self._initialized = True
        else:
            print("ConfigurationManager already initialized.")

    def get_setting(self, key: str):
        return self._settings.get(key)

    def set_setting(self, key: str, value: str):
        self._settings[key] = value

    def get_all_settings(self) -> dict:
        return self._settings.copy() # Return a copy to prevent external modification

# --- Usage ---
if __name__ == "__main__":
    print("--- First access ---")
    config1 = ConfigurationManager()
    print(f"Config 1 DB URL: {config1.get_setting('database_url')}")
    config1.set_setting("log_level", "DEBUG")

    print("\n--- Second access ---")
    config2 = ConfigurationManager()
    print(f"Config 2 Log Level: {config2.get_setting('log_level')}")
    print(f"Are config1 and config2 the same instance? {config1 is config2}")

    print("\n--- Third access ---")
    config3 = ConfigurationManager()
    print(f"Are config1 and config3 the same instance? {config1 is config3}")

    print("\n--- All settings from any instance ---")
    print(config1.get_all_settings())

```
