import requests
import hashlib
import time
import json

import os
from dotenv import load_dotenv

load_dotenv()

# Define the necessary variables
gwn_domain = os.getenv('gwn_domain')
access_token = os.getenv('access_token')
appID = os.getenv('appID')
secretKey = os.getenv('secretKey')

# Generate the timestamp in milliseconds
timestamp = str(int(time.time() * 1000))

# Body of the request
body = json.dumps({
  "id": 166665,
  "networkName": "202340000039",
  "country": "LK",
  "timezone": "Asia/Colombo",
  "networkAdministrators": [
    40400,
    45523,
    77845
  ],
  "cloneNetworkId": 116986
})

# Compute sha256 of the body
sha256_body = hashlib.sha256(body.encode()).hexdigest()

# Prepare the params for signature computation
params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"

# Compute the final signature
signature_base = f"&{params}&{sha256_body}&"
signature = hashlib.sha256(signature_base.encode()).hexdigest()

# Prepare the URL with parameters
url = f"https://{gwn_domain}/oapi/v1.0.0/network/update?access_token={access_token}&appID={appID}&timestamp={timestamp}&signature={signature}"

# Set headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=body)

# Print the response
print(response.json())
