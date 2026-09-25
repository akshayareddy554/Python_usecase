import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def timing(func):
    """Decorator to measure execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIMING] {func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

def log_call(func):
    """Decorator to log function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}")
        return func(*args, **kwargs)
    return wrapper

def read_large_file(path):
    """Generator: yields one line at a time (memory-efficient)"""
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

@timing
@log_call
def parse_errors(path):
    """Uses the generator to filter ERROR lines without loading full file"""
    error_count = 0
    for line in read_large_file(path):
        if "ERROR" in line:
            error_count += 1
    return error_count


if __name__ == "__main__":
    total_errors = parse_errors("app.log")
    print(f"Total ERROR lines found: {total_errors}")