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
  "id": 428748,
  "networkId": 165590,
  "ssidSsid": "Nvision",
  "ssidEnable": 1,
  "ssidVlan": 0,
  "ssidVlanid": None,
  "ssidRadiusDynamicVlan": None,
  "ssidSsidBand": "",
  "ssidSsidHidden": 0,
  "ssidWifiClientLimit": None,
  "ssidPortalEnable": 1,
  "ssidEncryption": 4,
  "ssidWepKey": "",
  "ssidWpaKeyMode": 0,
  "ssidWpaEncryption": 0,
  "ssidWpaKey": "12345678",
  "ssidRadiusServer": "3.15.254.99",
  "ssidRadiusPort": 1812,
  "ssidRadiusSecret": "testing123",
  "ssidRadiusAcctServer": "3.15.254.99",
  "ssidRadiusAcctPort": 1813,
  "ssidRadiusAcctSecret": "testing123",
  "ssidRadiusNasId": 990110000036,
  "ssidBridgeEnable": 0,
  "ssidMacFiltering": 0,
  "ssidIsolation": 0,
  "ssidIsolationMode": "",
  "ssidGatewayMac": None,
  "ssidVoiceEnterprise": 0,
  "ssid11V": 0,
  "ssid11R": 0,
  "ssid11K": 0,
  "ssidDtimPeriod": None,
  "ssidMcastToUcast": None,
  "ssidProxyarp": None,
  "ssidUapsd": 1,
  "ssidStaIdleTimeout": None,
  "ssid11W": None,
  "ssidBms": None,
  "ssidClientIPAssignment": None,
  "ssidHs20Profile": None,
  "ssidHs20": None,
  "ssidSecondaryRadiusEnable": None,
  "ssidSecondaryRadiusServer": None,
  "ssidSecondaryRadiusPort": None,
  "ssidSecondaryRadiusSecret": None,
  "ssidSecondaryRadiusAcctEnable": None,
  "ssidSecondaryRadiusAcctServer": None,
  "ssidSecondaryRadiusAcctPort": 1813,
  "ssidSecondaryRadiusAcctSecret": None,
  "ssidBonjourForward": None,
  "ssidDvlanServices": "[]",
  "ssidSecurityType": 1,
  "radiusProfile": None,
  "ppskProfile": None,
  "hsRelease": None,
  "bandwidthType": None,
  "bandwidthRules": None
})



timestamp = str(int(time.time() * 1000))

# Compute sha256 of the body
sha256_body = hashlib.sha256(body.encode()).hexdigest()

# Prepare the params for signature computation
params = f"access_token={access_token}&appID={appID}&secretKey={secretKey}&timestamp={timestamp}"

# Compute the final signature
signature_base = f"&{params}&{sha256_body}&"
signature = hashlib.sha256(signature_base.encode()).hexdigest()


url = f"https://www.gwn.cloud/oapi/v1.0.0/ssid/update?access_token={access_token}&appID=102073&timestamp={timestamp}&signature={signature}"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=body)

print(response.text)
