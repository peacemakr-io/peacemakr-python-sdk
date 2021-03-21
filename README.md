<p align="center">
  <br>
    <img src="https://admin.peacemakr.io/images/PeacemakrP-Golden.png" width="150"/>
  <br>
</p>

# Peacemakr E2E-Encryption-as-a-Service Python SDK

![Build Status](https://github.com/peacemakr-io/peacemakr-python-sdk/workflows/Build%20%26%20Test/badge.svg)

Peacemakr's E2E-Encryption-as-a-Service SDK solves all the hard problem of E2E-Encryption, and provides consistent solution with a simple interface.

We take security and trust very seriously. If you believe you have found a security issue, please responsibly disclose by [contacting us](mailto:security@peacemakr.io).

## Documentation

See the [API docs](https://github.com/peacemakr-io/peacemakr-python-sdk/tree/master/docs)

## Installation
Install from pip
```sh
pip install --upgrade peacemakr
```
Install from pip3 on mac,
```sh
python3 -m pip install peacemakr
```

Install from source
```sh
python setup.py install
```

### FAQ
1. In Linux, peacemakr-core-crypto-cpp.so is not found but the file is there.
  - Solution: "export LD_LIBRARY_PATH=:/usr/local/lib" >> ~/.bashrc
 


### Requirements
Python 3.6+

## Usage
The library requires your API key from the dashboard which is available at https://admin.peacemakr.io/.

Set the API key and initialize the persister to start using the SDK.
```python
import peacemakr as p
import peacemakr.factory as factory

api_key = "api-key"
persister = p.InMemoryPersister()
sdk = factory.get_crypto_sdk(api_key=api_key,
                                client_name="hello world",
                                peacemakr_hostname="https://api.peacemakr.io",
                                persister=persister
                                )

# Required call. Registers your client. Requires network connectivity.
sdk.register()

# Optional call, used to sync configs. Requires network connectivity.
sdk.sync()
```

### Protecting your Data with Peacemakr's E2E-Encryption-as-a-Service
It's straightforward to encrypt and decrypt anything with peacmekar library
```python
import os

random_bytes = os.urandom(100)

# To protect data, invoke encrypt. Does not require network connectivity.
encrypted_bytes = sdk.encrypt(random_bytes)
print(encrypted_bytes)

# To operate on protected data, invoke decrypt. Does not require network connectivity.
decrypted_bytes = sdk.decrypt(encrypted_bytes)
print(decrypted_bytes)
```

## Contributing
We appreciate all contributions. Some basic guidelines are here, for more informaton
see CONTRIBUTING.md

Issues:
- Please include a minimal example that reproduces your issue
- Please use the tags to help us help you
- If you file an issue and you want to work on it, fantastic! Please assign it to yourself.

PRs:
- All PRs must be reviewed and pass CI
