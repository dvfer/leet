import time
import functools

def measure_time(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        
        end = time.perf_counter()
        ms = (end - start) * 1000
        print(f"[{func.__name__}] took {ms:.4f} ms")
        return result
        
    return wrapper 