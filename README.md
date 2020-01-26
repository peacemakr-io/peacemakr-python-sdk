<p align="center">
  <br>
    <img src="https://github.com/peacemakr-io/peacemakr-admin-portal/blob/master/peacemakr-admin/public/images/PeacemakrP-Golden.png" width="150"/>
  <br>
</p>

# Peacemakr Python Library

![Build Status](https://github.com/peacemakr-io/peacemakr-python-sdk/workflows/Build%20%26%20Test/badge.svg)

Peacemakr's Python Crypto SDK for application layer crypto, and, key lifecycle management.

We take security and trust very seriously. If you believe you have found a security issue, please responsibly disclose by [contacting us](mailto:security@peacemakr.io).

## Documentation

See the [API docs](https://github.com/peacemakr-io/peacemakr-python-sdk/tree/docs/docs)

## Installation
Install from source
```sh
python setup.py install
```

Coming soon: Install from pip
```sh
pip install --upgrade peacemakr
```

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

sdk.register()
```

### Encrypt and Decrypt
It's straightforward to encrypt and decrypt anything with peacmekar library
```python
import os
import b64encode

random_bytes = os.urandom(100)

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
