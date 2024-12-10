import requests
import hashlib
import time

# Define the necessary variables
import os
from dotenv import load_dotenv

load_dotenv()

# Define the necessary variables
gwn_domain = os.getenv('gwn_domain')
access_token = os.getenv('access_token')
appID = os.getenv('appID')
secretKey = os.getenv('secretKey')
ssid_id = 369169 # Replace with the actual SSID ID

# Generate the timestamp in milliseconds
timestamp = str(int(time.time() * 1000))

# Prepare the params for signature computation
params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"

# Compute the final signature
signature_base = f"&{params}&"
signature = hashlib.sha256(signature_base.encode()).hexdigest()

# Prepare the URL with parameters
url = f"https://{gwn_domain}/oapi/v1.0.0/ssid/configuration?access_token={access_token}&appID={appID}&timestamp={timestamp}&signature={signature}&id={ssid_id}"

# Send the GET request
response = requests.get(url)

# Print the response
print(response.json())
