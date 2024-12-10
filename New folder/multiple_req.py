import socket
import radius
import concurrent.futures
import random

# RADIUS server details
server_ip = '54.205.5.145'
secret = 'wibipaaatesting123'
server_port = 1812

def generate_random_mac():
    # Generate a random MAC address
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    # Ensure the second least significant bit of the first byte is 0 (unicast)
    mac[0] = mac[0] & 0xFE
    # Format the MAC address in the standard format (XX:XX:XX:XX:XX:XX)
    mac_address = ':'.join(f'{byte:02X}' for byte in mac)
    return mac_address


username = generate_random_mac()
password = username




# Function to send a RADIUS authentication request
def send_radius_request():
    try:
        radius.authenticate(username, password, secret, host=server_ip, port=server_port)
        print("Request sent successfully")
    except Exception as e:
        print(f"An exception occurred: {e}")

# Number of requests to send
num_requests = 100  # Change this to however many requests you want to send

# Use ThreadPoolExecutor to send requests concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit multiple tasks to the thread pool
    futures = [executor.submit(send_radius_request) for _ in range(num_requests)]
    
    # Optional: Wait for all the tasks to complete
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()  # You can process the result if needed
        except Exception as e:
            print(f"Exception: {e}")
