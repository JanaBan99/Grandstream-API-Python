import socket
import radius

# RADIUS server details
server_ip = '54.205.5.145'
secret = 'wibipaaatesting123'
#secret = 'testing123'
server_port = 1812
'''
username = 'E69D3B0EC63E202340000031'
password = 'E69D3B0EC63E202340000031'
'''
username = 'E69D3B0EC63E'
password = 'E69D3B0EC63E'

for x in range(1):
    try:
        radius.authenticate(username, password, secret, host=server_ip, port=1812)
    except:
        print("An exception occurred")