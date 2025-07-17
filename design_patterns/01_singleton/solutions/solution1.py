from typing import List
import time

class Logger:
    _instance = None
    _initialized = False
    _logs = []

    def __new__(cls) -> 'Logger':
        if cls._instance is None:
            print("Creating a new Logger instance...")
            cls._instance = super(Logger, cls).__new__(cls)
        else:
            print("Using the existing Logger instance...")
        return cls._instance

    def __init__(self):
        if not self._initialized:
            print("Logger initialized (first time only).")
            time.sleep(0.5)
            self._initialized = True

    def _add_log(self, level: str, message: str) -> None:
        """Helper method to append log messages to the internal list"""
        log_entry = f"{level.upper()}: {message}"
        self._logs.append(log_entry)
        print(f"Logged: {log_entry}")

    def info(self, message: str) -> None:
        self._add_log(level="INFO", message=message)

    def warning(self, message: str) -> None:
        self._add_log(level="WARNING", message=message)

    def error(self, message: str) -> None:
        self._add_log(level="ERROR", message=message)

    def get_logs(self) -> List[str]:
        return self._logs


print("\n--- Test 1: First Logger Instance ---")
logger1 = Logger()
logger1.info("Application started.")
logger1.warning("Potential configuration issue detected.")

print("\n--- Test 2: Second Logger Instance ---")
logger2 = Logger()
logger2.error("Critical error: Database connection lost!")
logger2.info("User logged in successfully.")

print("\n--- Test 3: Third Logger Instance ---")
logger3 = Logger()
logger3.warning("Low disk space.")

print("\n--- Verifying Singleton Behavior ---")
print(f"Are logger1 and logger2 the same object? {logger1 is logger2}")
print(f"Are logger1 and logger3 the same object? {logger1 is logger3}")

print("\n--- All Accumulated Logs (from logger1's perspective) ---")
for log in logger1.get_logs():
    print(log)

print("\n--- All Accumulated Logs (from logger2's perspective) ---")
for log in logger2.get_logs():
    print(log)

\
print(f"\nNumber of logs from logger1: {len(logger1.get_logs())}")
print(f"Number of logs from logger2: {len(logger2.get_logs())}")
