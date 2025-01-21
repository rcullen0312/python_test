import time
import random

def is_server_working():
    """
    Simulates a check for server availability.
    Returns True for this example.
    """
    return True  # Replace with actual logic if needed

def retrieve_phone_code():
    """
    Simulates retrieving a phone confirmation code.
    """
    time.sleep(1)  # Simulate delay
    return str(random.randint(1000, 9999))  # Return a mock 4-digit code
