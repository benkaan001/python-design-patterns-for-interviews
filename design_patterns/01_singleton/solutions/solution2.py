import time
from typing import Any

class ApplicationSettings:
    _instance: 'ApplicationSettings' = None
    _initialized: bool = False

    def __new__(cls) -> 'ApplicationSettings':
        if not cls._instance:
            print("Creating a new ApplicationSettings instance...")
            instance = super().__new__(cls)
            cls._instance = instance
        else:
            print("Using existing ApplicationSettings instance...")
        return cls._instance

    def __init__(self) -> None:
        default_settings: dict[str, Any] = {
            "theme": "dark",
            "default_path": "/home/user/documents",
            "recent_files": []}
        if not self._initialized:
            print(f"Intializing a new instance with default settings..")
            time.sleep(1)
            self._settings = default_settings
            self._initialized = True
            print("Initialization complete")
        else:
            print("Object already initialized")

    def get_setting(self, key: str) -> Any:
        return self._settings[key]

    def set_setting(self, key: str, value: Any):
        if key in self._settings:
            print(f"Updating exiting setting for {key} from {self._settings.get(key)} to new setting value: {value}")
        else:
            print("Setting update complete")
        self._settings[key] = value

    def get_all_settings(self) -> dict[str, Any]:
        return self._settings.copy()

app1 = ApplicationSettings()
app2 = ApplicationSettings()
app3 = ApplicationSettings()

app1.set_setting(key='theme', value="light_modern")

print("\n--- Verifying Singleton Behavior ---")
print(f"Are app1 and app2 the same object? {app1 is app2}")
print(f"Are app1 and app3 the same object? {app1 is app3}")

print("\n--- All Settings (from app1's perspective) ---")
for key, value in app1.get_all_settings().items():
    print(f"{key}: {value}")

print("\n--- All Settings (from app2's perspective) ---")
for key, value in app2.get_all_settings().items():
    print(f"{key}: {value}")

print("\n--- All Settings (from app3's perspective) ---")
for key, value in app3.get_all_settings().items():
    print(f"{key}: {value}")
