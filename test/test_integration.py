import pytest
from peacemakr_sdk.generated.api_client import ApiClient
from peacemakr_sdk.generated.configuration import Configuration
from peacemakr_sdk.generated.api.org_api import OrgApi
from peacemakr_sdk.generated.api.server_management_api import ServerManagementApi

import peacemakr_sdk.factory as Factory
from peacemakr_sdk.impl.persister_impl import InMemoryPersister

import time
# set up
@pytest.fixture
def setup_api_key():
    # set up test api_key
    # set up test address
    time.sleep(2)
    configuration = Configuration()
    configuration.api_key['authorization'] = ""
    configuration.host = "http://peacemakr-services:80" + "/api/v1"
    api_client = ApiClient(configuration=configuration)

    client_api = ServerManagementApi(api_client)
    print(client_api.health_get())
    org_api = OrgApi(api_client=api_client)
    api_key = None

    api_key = org_api.get_test_organization_api_key()
    print(api_key)
    assert api_key!=None, "No testing api key was found"
    return api_key


def test_register(setup_api_key):

    persister = InMemoryPersister()
    sdk = Factory.get_crypto_sdk(api_key=setup_api_key.key, client_name="test register", peacemakr_hostname="http://peacemakr-services:80", persister=persister)
    sdk.register()
    print(persister.debug())


# def test_sync(setup_api_key):
#     persister = InMemoryPersister()
#     sdk = Factory.get_crypto_sdk(api_key=setup_api_key.key, client_name="test register", peacemakr_hostname="http://localhost:8080", persister=persister)
#     sdk.register()
#     # sleep for 1 sec to wait for sdk to have at least few keys ready
#     # we should check for raise exception
#     time.sleep(1)
#     sdk.sync()

    