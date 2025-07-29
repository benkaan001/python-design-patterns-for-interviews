import threading

class ThreadSafeResourcePool:
    _instance: 'ThreadSafeResourcePool' = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls, *arg, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, size=3):
        if not self._initialized:
            with self._lock:
                if not self._initialized:
                    self.available_resources = [f"Res-{i+1}" for i in range(size)]
                    self.resources_in_use = []
                    self._initialized = True

    def acquire_resource(self):
        with self._lock:
            if not self.available_resources:
                print(f"[{threading.current_thread().name}] Pool empty!")
                return None
            resource = self.available_resources.pop(0)
            self.resources_in_use.append(resource)
            print(f"[{threading.current_thread().name}] Acquired: {resource}")
            return resource

    def release_resource(self, resource):
        with self._lock:
            if resource not in self.resources_in_use:
                print(f"[{threading.current_thread().name}] Warning: Resource {resource} not in use.")
                return
            self.resources_in_use.remove(resource)
            self.available_resources.append(resource)
            print(f"[{threading.current_thread().name}] Released: {resource}")

    def get_pool_status(self):
        with self._lock:
            return f"Avail: {len(self.available_resources)}. In Use: {len(self.resources_in_use)}."

def worker_function(thread_id):
    threading.current_thread().name = f"Thread-{thread_id}"
    pool = ThreadSafeResourcePool(size=3)
    res = pool.acquire_resource()
    if res:
        pool.release_resource(res)

num_threads = 5
threads = [threading.Thread(target=worker_function, args=(i,)) for i in range(num_threads)]
for t in threads:
    t.start()
for t in threads:
    t.join()

pool = ThreadSafeResourcePool()
print("\n--- Final Pool Status ---")
print(pool.get_pool_status())