import hashlib
import json
import time
import requests

# Replace these with your actual values
import os
from dotenv import load_dotenv

load_dotenv()

# Define the necessary variables
gwn_domain = os.getenv('gwn_domain')
access_token = os.getenv('access_token')
appID = os.getenv('appID')
secretKey = os.getenv('secretKey')
ssid_id = 369168  # Replace with the actual SSID ID
ssid_name = "Guest-Wifi1213"  # Replace with the desired SSID name
ssid_enable = 1  # 1 to enable, 0 to disable
timestamp = str(int(time.time() * 1000))

# Body of the request
body = json.dumps({
    "id": ssid_id,
    "networkId": 165590,
    "ssidSsid": ssid_name,
    "ssidEnable": ssid_enable,
    "ssidVlan": 0,
    "ssidVlanid": None,
    "ssidRadiusDynamicVlan": None,
    "ssidSsidBand": "",
    "ssidNewSsidBand": "2,5",
    "ssidSsidHidden": 0,
    "ssidWifiClientLimit": None,
    "ssidPortalEnable": 1,
    "ssidEncryption": 4,
    "ssidWepKey": None,
    "ssidWpaKeyMode": None,
    "ssidWpaEncryption": None,
    "ssidWpaKey": None,
    "ssidRadiusServer": None,
    "ssidRadiusPort": None,
    "ssidRadiusSecret": None,
    "ssidRadiusAcctServer": None,
    "ssidRadiusAcctPort": None,
    "ssidRadiusAcctSecret": None,
    "ssidRadiusNasId": None,
    "ssidBridgeEnable": 0,
    "ssidMacFiltering": 0,
    "ssidIsolation": 0,
    "ssidIsolationMode": None,
    "ssidGatewayMac": None,
    "ssidVoiceEnterprise": 0,
    "ssid11V": 0,
    "ssid11R": 0,
    "ssid11K": 0,
    "ssidDtimPeriod": 1,
    "ssidMcastToUcast": 0,
    "ssidProxyarp": 0,
    "ssidUapsd": 1,
    "ssidStaIdleTimeout": 300,
    "ssid11W": None,
    "ssidBms": 0,
    "ssidClientIPAssignment": 0,
    "ssidHs20Profile": None,
    "ssidHs20": None,
    "ssidSecondaryRadiusEnable": None,
    "ssidSecondaryRadiusServer": None,
    "ssidSecondaryRadiusPort": None,
    "ssidSecondaryRadiusSecret": None,
    "ssidSecondaryRadiusAcctEnable": None,
    "ssidSecondaryRadiusAcctServer": None,
    "ssidSecondaryRadiusAcctPort": None,
    "ssidSecondaryRadiusAcctSecret": None,
    "ssidBonjourForward": "0",
    "ssidDvlanServices": "[\" \"]",
    "ssidSecurityType": 0,
    "radiusProfile": 3671,
    "ppskProfile": None,
    "hsRelease": None,
    "bandwidthType": None,
    "bandwidthRules": None,
    "osFiltering": None,
    "osWhitelist": None,
    "osBlacklist": None,
    "ssidPortalPolicy": 23707,
    "ssidGatewayMacList": None
})


# Compute sha256 of the body
sha256_body = hashlib.sha256(body.encode()).hexdigest()

# Prepare the params for signature computation
params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"

# Compute the final signature
signature_base = f"&{params}&{sha256_body}&"
signature = hashlib.sha256(signature_base.encode()).hexdigest()

# Prepare the URL with parameters
url = f"https://{gwn_domain}/oapi/v1.0.0/ssid/update?access_token={access_token}&appID={appID}&timestamp={timestamp}&signature={signature}"

# Set headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=body)

# Print the response
print(response.json())
