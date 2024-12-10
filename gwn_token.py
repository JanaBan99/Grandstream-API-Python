import requests
import json
import os
from dotenv import load_dotenv
import dotenv
load_dotenv()

dotenv_path = ".env"

url = "https://www.gwn.cloud/oauth/token?grant_type=client_credentials&client_id=102073&client_secret=w5l2awsV3yUHHJniY3zqMlsuWD1QpBaB"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# Parse the JSON response
response_json = response.json()
print(response_json)
# Extract the access_token
access_token = response_json.get("access_token")
expire_time = response_json.get("expires_in")
# Print the access_token
#print(access_token)
dotenv.set_key(dotenv_path, "access_token", access_token)
#dotenv.set_key(dotenv_path, "expires_in", expire_time)