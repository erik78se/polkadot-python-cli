#!/usr/bin/env python3

import requests
import json
import re

SERVER_ADDRESS = 'http://localhost:9933'
HEADERS = {'Content-Type': 'application/json'}


def get_session_key():
    data = '{"id":1, "jsonrpc":"2.0", "method": "author_rotateKeys", "params": []}'
    response = requests.post(url=SERVER_ADDRESS, headers=HEADERS, data=data)
    response_json = json.loads(response.text)
    return response_json['result']


def is_syncing():
    data = '{"id":1, "jsonrpc":"2.0", "method": "system_health", "params": []}'
    response = requests.post(url=SERVER_ADDRESS, headers=HEADERS, data=data)
    response_json = json.loads(response.text)
    return response_json['result']['isSyncing']


def is_validating():
    data = '{"id":1, "jsonrpc":"2.0", "method": "system_nodeRoles", "params": []}'
    response = requests.post(url=SERVER_ADDRESS, headers=HEADERS, data=data)
    response_json = json.loads(response.text)
    if response_json['result'][0] == 'Authority':
        return True
    else:
        return False


def get_version():
    data = '{"id":1, "jsonrpc":"2.0", "method": "system_version", "params": []}'
    response = requests.post(url=SERVER_ADDRESS, headers=HEADERS, data=data)
    response_json = json.loads(response.text)
    result = response_json['result']
    version_number = re.search(r'([\d.]+)', result).group(1)
    return version_number
