# System Utility Library

The `system` directory provides a suite of functions tailored for managing and interacting with various system-level operations. This library is designed to offer utilities that help in memory management, process control, and networking tasks, making it easier to monitor and control system resources and connections.

## Table of Contents

1. [Memory Management (`memory_management.py`)](#memory-management)
2. [Process Control (`process_control.py`)](#process-control)
3. [Networking (`networking.py`)](#networking)

---

### Memory Management (`memory_management.py`)

Memory management is crucial for ensuring the efficient use of system resources. This module offers functions to interact with and manage system memory.

**Functions**:

- **`get_total_memory()`**: 
  - Returns the total memory in bytes of the system.
  
- **`get_used_memory()`**: 
  - Provides the amount of memory currently being used.

- **`get_free_memory()`**: 
  - Details the available free memory in the system.

- **`get_memory_stats()`**: 
  - Returns a dictionary with detailed statistics about memory usage, including total, used, free, and the percentage of used memory.

---

### Process Control (`process_control.py`)

This module aids in managing and monitoring system processes, allowing for better control over running applications and services.

**Functions**:

- **`list_all_processes()`**: 
  - Returns a list of all currently running processes, detailing their process ID (pid) and name.

- **`kill_process(pid)`**: 
  - Terminates the process with the provided process ID (pid). Returns a status message indicating success or failure.

---

### Networking (`networking.py`)

Networking is a cornerstone of modern computing. This module offers utilities related to network operations, helping in tasks like retrieving system IP or checking port status.

**Functions**:

- **`get_hostname()`**: 
  - Returns the host name of the current system, providing insights into the system's network identity.

- **`get_ip_address()`**: 
  - Fetches the IP address associated with the current system.

- **`check_port_open(port)`**: 
  - Checks if a specific port is open on the current system, useful for ensuring network services are running or available.

---

For each function, refer to the respective file for more detailed documentation, usage examples, and further insights. This library serves as a foundational toolkit for various system-related tasks and can be expanded upon as needed. Whether you're looking to monitor system health, control processes, or handle network operations, this library offers a robust set of tools to assist you.