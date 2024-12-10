import hashlib
import json
import requests
import time

def compute_signature(appID, secretKey, access_token, timestamp, body=None):
    # Step 1: Combine the public parameters and secretKey into params
    params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"
    
    # Step 2: Compute sha256 of the body if it exists
    if body:
        body_sha256 = hashlib.sha256(json.dumps(body).encode()).hexdigest()
    else:
        body_sha256 = ""

    # Step 3: Add '&' at the beginning and end, then compute the final sha256
    signature_base_string = f"&{params}&{body_sha256}&"
    signature = hashlib.sha256(signature_base_string.encode()).hexdigest()
    
    return signature

def get_ssid_configuration(gwn_domain, appID, secretKey, access_token, ssid_id):
    # Step 4: Generate the timestamp
    timestamp = int(time.time() * 1000)

    # Step 5: Prepare the request body
    body = {
        "id": ssid_id
    }
    
    # Step 6: Compute the signature
    signature = compute_signature(appID, secretKey, access_token, timestamp, body)
    
    # Step 7: Prepare the headers and URL
    url = f"https://{gwn_domain}/oapi/v1.0.0/ssid/configuration?access_token={access_token}&appID={appID}&timestamp={timestamp}&signature={signature}"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    # Step 8: Send the request
    response = requests.get(url, headers=headers, json=body)
    
    # Step 9: Return or print the response
    return response.json()

# Example usage
import os
from dotenv import load_dotenv

load_dotenv()

# Define the necessary variables
gwn_domain = os.getenv('gwn_domain')
access_token = os.getenv('access_token')
appID = os.getenv('appID')
secretKey = os.getenv('secretKey')
ssid_id = 369169

response = get_ssid_configuration(gwn_domain, appID, secretKey, access_token, ssid_id)
print(json.dumps(response, indent=4))
