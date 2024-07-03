import json
from eth_keyfile import extract_key_from_keyfile

keystore_path = '/root/.ethereum/keystore/UTC--2024-07-03T12-55-12.000023938Z--618b418c30e0a15a640608e77830588ebc5c7377'
password = '${PASS}'

with open(keystore_path) as keyfile:
    encrypted_key = json.load(keyfile)
    private_key = extract_key_from_keyfile(encrypted_key, password.encode('utf-8'))
    print(f'Your private key: {private_key.hex()}')