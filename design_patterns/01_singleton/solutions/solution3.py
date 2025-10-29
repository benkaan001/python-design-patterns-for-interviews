import threading
from typing import List, Optional

class ThreadSafeResourcePool:
    _instance: Optional['ThreadSafeResourcePool'] = None
    _lock = threading.Lock() # Lock for thread-safe instantiation and resource operations

    def __new__(cls, size: int = 3, *args, **kwargs) -> 'ThreadSafeResourcePool':
        """Ensures single instance creation using double-checked locking."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    # Create and initialize the instance under the lock
                    cls._instance = super().__new__(cls)
                    cls._instance.available_resources: List[str] = [f"Res-{i+1}" for i in range(size)]
                    cls._instance.resources_in_use: List[str] = []
        return cls._instance

    def __init__(self, size: int = 3) -> None:
        # Pass (Initialization handled in __new__)
        pass

    def acquire_resource(self) -> str:
        """Acquires a resource from the pool (thread-safe)."""
        with self._lock:
            if not self.available_resources:
                raise ValueError("Pool empty!")
            resource = self.available_resources.pop(0)
            self.resources_in_use.append(resource)
            return resource

    def release_resource(self, resource: str) -> None:
        """Releases a resource back to the pool (thread-safe)."""
        with self._lock:
            if resource not in self.resources_in_use:
                return # Fail silently or raise error, keeping it minimal here

            self.resources_in_use.remove(resource)
            self.available_resources.append(resource)

    def get_pool_status(self) -> str:
        """Returns current pool status (thread-safe read)."""
        # Lock is necessary to ensure consistent reading of both lists
        with self._lock:
            return (f"Avail: {len(self.available_resources)}. "
                    f"In Use: {len(self.resources_in_use)}.")

# --- Multi-threaded Test Harness (Interview Demo Focus) ---
def worker_function(thread_id: int, results: List[str]):
    """Function run by each thread to test the singleton and resource pool."""
    thread_name = f"T-{thread_id}"
    pool = ThreadSafeResourcePool(size=3) # All threads get the same instance
    acquired_res = None

    try:
        acquired_res = pool.acquire_resource()
        results.append(f"{thread_name} Acquired {acquired_res}")
    except ValueError:
        results.append(f"{thread_name} Failed (Pool Empty)")
    finally:
        if acquired_res:
            pool.release_resource(acquired_res)

if __name__ == "__main__":
    print("--- Starting Multi-threaded Singleton Test ---")

    num_threads = 5
    threads = []
    thread_results: List[str] = []

    # Start threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker_function, args=(i, thread_results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("\n--- All threads finished. Final Status ---")
    final_pool = ThreadSafeResourcePool()

    # Display Results
    for result in thread_results:
        print(f"  {result}")

    # Verification
    print(f"\nFinal Pool Status: {final_pool.get_pool_status()}")

    initial_size = 3
    if len(final_pool.available_resources) == initial_size and len(final_pool.resources_in_use) == 0:
        print("Verification: SUCCESS - All resources returned and pool size is correct.")
    else:
        print("Verification: FAILURE - Resource count error.")
