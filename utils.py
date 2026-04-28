"""
MicroAether Utilities
Helper functions for timing, logging, and caching.
"""

import time
from functools import lru_cache
from typing import Any, Callable

def timer(func: Callable) -> Callable:
    """Simple timing decorator"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

def cached(maxsize: int = 128):
    """Simple caching decorator"""
    return lru_cache(maxsize=maxsize)

def log(msg: str, level: str = "INFO"):
    """Simple logger"""
    print(f"[{level}] {msg}")
