import requests
import json
import time
import hashlib

import os
from dotenv import load_dotenv

load_dotenv()

# Define the necessary variables
gwn_domain = os.getenv('gwn_domain')
access_token = os.getenv('access_token')
appID = os.getenv('appID')
secretKey = os.getenv('secretKey')


body = json.dumps({
"id":4118,
"name":"RadiusServer",
"radiusNasId":"202340000048",
"radiusAttempts":5,
"radiusTimeout":1,
"acctUpdateInterval":120,
"radiusDynamicVlan":0,
"networkId":188112,
"radiusServerConfigList":[
    {
        "server":"3.15.254.99",
        "port":1812.0,
        "secret":"testing123"
    }
],
"radiusAcctServerConfigList":[
    {
        "server":"3.15.254.99",
        "port":1813.0,
        "secret":"testing123"
    }
]
})



timestamp = str(int(time.time() * 1000))

# Compute sha256 of the body
sha256_body = hashlib.sha256(body.encode()).hexdigest()

# Prepare the params for signature computation
params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"

# Compute the final signature
signature_base = f"&{params}&{sha256_body}&"
signature = hashlib.sha256(signature_base.encode()).hexdigest()

#/oapi/v1.0.0/radius/edit
url = f"https://{gwn_domain}/oapi/v1.0.0/radius/edit?access_token={access_token}&appID=102073&timestamp={timestamp}&signature={signature}"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=body)

print(response.text)
