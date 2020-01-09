# Peacemakr Python Library

![Build Status](https://github.com/peacemakr-io/peacemakr-python-sdk/workflows/.github/workflows/peacemakr_python_sdk.yml/badge.svg)

Peacemakr's Python Crypto SDK for application layer crypto, and, key lifecycle management.

We take security and trust very seriously. If you believe you have found a security issue, please responsibly disclose by [contacting us](mailto:security@peacemakr.io).

## Documentation

## Installation
Install from source
```sh
python setup.py install
```

Coming soon: Install from pip
```sh
pip install --upgrade peacemakr_sdk
```

### Requirements
Python 3.4+

## Usage
The library requires your API key from the dashboard which is available at https://admin.peacemakr.io/.

Set the API key and initialize the persister to start using the SDK.
```python
import peacemakr_sdk.factory as factory
api_key = "api-key"
persister = InMemoryPersister()
sdk = factory.get_crypto_sdk(api_key=api_key,
                                client_name="hello world",
                                peacemakr_hostname="https://api.peacemakr.io",
                                persister=persister
                                )
sdk.register()
```

### Encrypt and Decrypt
It's straightforward to encrypt and decrypt anything with peacmekar library
```python
import peacemakr_sdk.factory as factory
import os
import b64encode
sdk = factory.get_crypto_sdk(api_key=..., client_name=..., peacemakr_hostname=..., persister=...)
random_bytes = b64encode(os.urandom(100))

encrypted_bytes = sdk.encrypt(random_bytes)

decrypted_bytes = sdk.decrypt(encrypted_bytes)
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