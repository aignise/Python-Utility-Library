import socket

def get_hostname():
    """
    Returns the host name of the current system.
    """
    return socket.gethostname()

def get_ip_address():
    """
    Returns the IP address of the current system.
    """
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def check_port_open(port):
    """
    Checks if a port is open on the current system.

    Args:
    - port (int): Port number.

    Returns:
    - bool: True if open, False otherwise.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0
