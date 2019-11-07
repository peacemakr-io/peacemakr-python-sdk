# peacemakr_sdk.ClientApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client**](ClientApi.md#add_client) | **POST** /client | Register a new client
[**add_client_public_key**](ClientApi.md#add_client_public_key) | **POST** /client/{clientId}/addPublicKey | Register a new public key for the client
[**delete_client**](ClientApi.md#delete_client) | **DELETE** /client/{clientId} | Remove an existing organization
[**get_client**](ClientApi.md#get_client) | **GET** /client/{clientId} | Get an existing client


# **add_client**
> Client add_client(client)

Register a new client

### Example
```python
from __future__ import print_function
import time
import peacemakr_sdk
from peacemakr_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr_sdk.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr_sdk.ClientApi(peacemakr_sdk.ApiClient(configuration))
client = peacemakr_sdk.Client() # Client | 

try:
    # Register a new client
    api_response = api_instance.add_client(client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->add_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**Client**](Client.md)|  | 

### Return type

[**Client**](Client.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_client_public_key**
> PublicKey add_client_public_key(client_id, new_public_key)

Register a new public key for the client

### Example
```python
from __future__ import print_function
import time
import peacemakr_sdk
from peacemakr_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr_sdk.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr_sdk.ClientApi(peacemakr_sdk.ApiClient(configuration))
client_id = 'client_id_example' # str | 
new_public_key = peacemakr_sdk.PublicKey() # PublicKey | 

try:
    # Register a new public key for the client
    api_response = api_instance.add_client_public_key(client_id, new_public_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->add_client_public_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **new_public_key** | [**PublicKey**](PublicKey.md)|  | 

### Return type

[**PublicKey**](PublicKey.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> Client delete_client(client_id)

Remove an existing organization

### Example
```python
from __future__ import print_function
import time
import peacemakr_sdk
from peacemakr_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr_sdk.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr_sdk.ClientApi(peacemakr_sdk.ApiClient(configuration))
client_id = 'client_id_example' # str | 

try:
    # Remove an existing organization
    api_response = api_instance.delete_client(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->delete_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**Client**](Client.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> Client get_client(client_id)

Get an existing client

### Example
```python
from __future__ import print_function
import time
import peacemakr_sdk
from peacemakr_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr_sdk.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr_sdk.ClientApi(peacemakr_sdk.ApiClient(configuration))
client_id = 'client_id_example' # str | 

try:
    # Get an existing client
    api_response = api_instance.get_client(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**Client**](Client.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

