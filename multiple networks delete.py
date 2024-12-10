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

# List of network IDs to delete
network_ids = [
    117328, 117338, 117339, 117345, 117364, 117382, 118044, 118068, 118091, 118093, 
    118114, 118457, 118458, 121682, 122319, 122323, 122567, 122896, 124141, 125307, 
    125311, 125855, 126115, 126121, 126869, 129213, 129698, 129713, 132258, 132292, 
    133559, 133569, 133570, 133574, 133575, 133578, 133744, 134245, 134256, 134291, 
    134292, 134293, 134294, 134298, 134302, 134303, 134304, 134309, 134313, 135695, 
    138032, 138035, 138038, 138061, 139976, 139977, 140211, 140217, 140218, 140222, 
    140242, 140246, 140249
]

# Loop through each network ID and send the delete request
for network_id in network_ids:
    # Generate the timestamp in milliseconds
    timestamp = str(int(time.time() * 1000))
    
    # Body of the request
    body = json.dumps({"id": network_id})
    
    # Compute sha256 of the body
    sha256_body = hashlib.sha256(body.encode()).hexdigest()
    
    # Prepare the params for signature computation
    params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"
    
    # Compute the final signature
    signature_base = f"&{params}&{sha256_body}&"
    signature = hashlib.sha256(signature_base.encode()).hexdigest()
    
    # Prepare the URL with parameters
    url = f"https://{gwn_domain}/oapi/v1.0.0/network/delete?access_token={access_token}&appID={appID}&timestamp={timestamp}&signature={signature}"
    
    # Set headers
    headers = {
        "Content-Type": "application/json"
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, data=body)
    
    # Print the response
    print(f"Network ID: {network_id}, Response: {response.json()}")
