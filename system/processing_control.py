import psutil

def list_all_processes():
    """
    Returns a list of all currently running processes.
    """
    return [proc.info for proc in psutil.process_iter(attrs=["pid", "name"])]

def kill_process(pid):
    """
    Kills the process with the provided process ID (pid).

    Args:
    - pid (int): Process ID.

    Returns:
    - str: Status message.
    """
    try:
        psutil.Process(pid).terminate()
        return f"Process {pid} terminated successfully."
    except psutil.NoSuchProcess:
        return f"Process {pid} not found."
