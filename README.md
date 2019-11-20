# peacemakr-python-sdk
Peacemakr's Python Crypto SDK for application layer crypto, and, key lifecycle management.


## Set up locally in virtualenv
Everything is smoked tested and developed in Python3.7
```sh
# start virtualenv

# set up core-crypto https://github.com/peacemakr-io/peacemakr-core-crypto
cd /path/to/peacemakr-core-crypto/bin && ./release-python.sh local /path/to/virtualenv/lib/site-packages release

pip install -r requirements.txt

# if you made changes in the file, to install the new changes
python setup.py install

# to run example
# Replace API Key in the example.py with your local api-key
python examples/example.py

# The correct behavior should print nothing and no errors
```

## Test locally in virtualenv
```sh
# install packages
pip install test-requirements.txt
# set up core-crypto https://github.com/peacemakr-io/peacemakr-core-crypto
cd /path/to/peacemakr-core-crypto/bin && ./release-python.sh local /path/to/virtualenv/lib/site-packages release

# testing
pytest test/test_integration.py
```
