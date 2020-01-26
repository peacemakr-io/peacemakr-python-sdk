import pytest
from peacemakr.generated.api_client import ApiClient
from peacemakr.generated.configuration import Configuration
from peacemakr.generated.api.org_api import OrgApi
import peacemakr.factory as Factory
from peacemakr.impl.persister_impl import InMemoryPersister

import os
import random
import time
import string
from base64 import b64encode

# set up
@pytest.fixture
def setup_params():
    
    # set up test address
    test_url = os.getenv("PEACEMAKR_TEST_URL", "http://localhost:8080")

    # need to wait until server is setup, otherwise call to server will fail
    time.sleep(5)

    # set up test api_key
    configuration = Configuration()
    configuration.api_key['authorization'] = ""
    configuration.host = test_url + "/api/v1"
    api_client = ApiClient(configuration=configuration)

    org_api = OrgApi(api_client=api_client)
    api_key = None
    api_key = org_api.get_test_organization_api_key()
    assert api_key!=None, "No testing api key was found"

    params = {}
    params["api_key"] = api_key.key
    params["test_url"] = test_url
    return params


def test_register(setup_params):
    persister = InMemoryPersister()
    sdk = Factory.get_crypto_sdk(api_key=setup_params["api_key"], client_name="test_register", peacemakr_hostname=setup_params["test_url"], persister=persister)
    sdk.register()

    num_clients = persister.key_nums()
    assert(num_clients != 0)

def test_sync(setup_params):
    persister = InMemoryPersister()
    sdk = Factory.get_crypto_sdk(api_key=setup_params["api_key"], client_name="test_sync", peacemakr_hostname=setup_params["test_url"], persister=persister)
    sdk.register()

    # sleep for 1 sec to wait for sdk to have at least few keys ready
    # we should check for raise exception
    time.sleep(1)
    sdk.sync()

    num_clients = persister.key_nums()
    assert(num_clients != 0)

def test_encrypt_decrypt_bytes(setup_params):
    persister = InMemoryPersister()
    sdk = Factory.get_crypto_sdk(api_key=setup_params["api_key"], client_name="test_encrypt_decrypt_bytes", peacemakr_hostname=setup_params["test_url"], persister=persister)
    sdk.register()

    # sleep to wait for keys to be generated in server
    time.sleep(2)
    sdk.sync()

    num_clients = persister.key_nums()
    assert(num_clients != 0)

    # generate random bytes
    random_bytes = os.urandom(100)
    # encode random bytes to utf-8
    plain_text = random_bytes

    encrypted_text = sdk.encrypt(plain_text)
    assert(plain_text != encrypted_text)

    # ouptut is bytes
    decrypted_text = sdk.decrypt(encrypted_text)
    assert(decrypted_text == plain_text)

def test_encrypt_decrypt_string(setup_params):
    persister = InMemoryPersister()
    sdk = Factory.get_crypto_sdk(api_key=setup_params["api_key"], client_name="test_encrypt_decrypt_string", peacemakr_hostname=setup_params["test_url"], persister=persister)
    sdk.register()

    # sleep to wait for keys to be generated in server
    time.sleep(2)
    sdk.sync()

    num_clients = persister.key_nums()
    assert(num_clients != 0)

    N = random.randint(0,1000)
    plain_text = ''.join(random.choices(string.printable, k=N))

    encrypted_text = sdk.encrypt(plain_text.encode())
    assert(plain_text != encrypted_text)

    # ouptut is bytes
    decrypted_text = sdk.decrypt(encrypted_text)
    assert(decrypted_text == plain_text.encode())
