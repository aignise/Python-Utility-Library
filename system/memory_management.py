import os
import psutil

def get_total_memory():
    """
    Returns the total memory in bytes.
    """
    return psutil.virtual_memory().total

def get_used_memory():
    """
    Returns the used memory in bytes.
    """
    return psutil.virtual_memory().used

def get_free_memory():
    """
    Returns the free memory in bytes.
    """
    return psutil.virtual_memory().free

def get_memory_stats():
    """
    Returns a dictionary with details about memory usage.
    """
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "used": mem.used,
        "free": mem.free,
        "percent_used": mem.percent
    }
