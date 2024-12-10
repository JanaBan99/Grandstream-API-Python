import requests
import hashlib
import time
import json

# Define the necessary variables
import os
from dotenv import load_dotenv

load_dotenv()

# Define the necessary variables
gwn_domain = os.getenv('gwn_domain')
access_token = os.getenv('access_token')
appID = os.getenv('appID')
secretKey = os.getenv('secretKey')
network_id = 188112 # Replace with your actual network group ID
page_num = 1  # Page number
page_size = 5  # Number of items per page

# Generate the timestamp in milliseconds
timestamp = str(int(time.time() * 1000))

# Body of the request
body = json.dumps({
    "networkId": network_id,
    "pageNum": page_num,
    "pageSize": page_size
})

# Compute sha256 of the body
sha256_body = hashlib.sha256(body.encode()).hexdigest()

# Prepare the params for signature computation
params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"

# Compute the final signature
signature_base = f"&{params}&{sha256_body}&"
signature = hashlib.sha256(signature_base.encode()).hexdigest()

# Prepare the URL with parameters
url = f"https://{gwn_domain}/oapi/v1.0.0/radius/list?access_token={access_token}&appID={appID}&timestamp={timestamp}&signature={signature}"

# Set headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=body)

# Print the response
print(response.json())
