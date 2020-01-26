# peacemakr.KeyDerivationServiceRegistryApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_key_derivation_service_instance**](KeyDerivationServiceRegistryApi.md#add_key_derivation_service_instance) | **POST** /crypto/deriver/instance | Register a new KeyDerivationServiceInstance
[**delete_key_derivation_service_instance**](KeyDerivationServiceRegistryApi.md#delete_key_derivation_service_instance) | **DELETE** /crypto/deriver/instance/{keyDerivationInstanceId} | Activate or deactivate an existing KeyDerivationServiceInstance
[**get_all_org_key_derivation_service_instances**](KeyDerivationServiceRegistryApi.md#get_all_org_key_derivation_service_instances) | **GET** /crypto/deriver/all-org-instances | Get the all key derivers registerd to org
[**get_all_shared_key_derivation_service_instances**](KeyDerivationServiceRegistryApi.md#get_all_shared_key_derivation_service_instances) | **GET** /crypto/deriver/all-shared-instances | Get the all key derivers that the org has access to - including shared cloud instances
[**get_key_derivation_service_instance**](KeyDerivationServiceRegistryApi.md#get_key_derivation_service_instance) | **GET** /crypto/deriver/instance/{keyDerivationInstanceId} | Get the keyderiver details by id
[**heartbeat_key_derivation_service_instance**](KeyDerivationServiceRegistryApi.md#heartbeat_key_derivation_service_instance) | **GET** /crypto/deriver/instance/{keyDerivationInstanceId}/heartbeat | Heatbeat from the given key derivation service instance


# **add_key_derivation_service_instance**
> KeyDerivationInstance add_key_derivation_service_instance(key_derivation_instance=key_derivation_instance)

Register a new KeyDerivationServiceInstance

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.KeyDerivationServiceRegistryApi(peacemakr.generated.ApiClient(configuration))
key_derivation_instance = peacemakr.KeyDerivationInstance() # KeyDerivationInstance |  (optional)

try:
    # Register a new KeyDerivationServiceInstance
    api_response = api_instance.add_key_derivation_service_instance(key_derivation_instance=key_derivation_instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyDerivationServiceRegistryApi->add_key_derivation_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_derivation_instance** | [**KeyDerivationInstance**](KeyDerivationInstance.md)|  | [optional] 

### Return type

[**KeyDerivationInstance**](KeyDerivationInstance.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_derivation_service_instance**
> delete_key_derivation_service_instance(key_derivation_instance_id, active)

Activate or deactivate an existing KeyDerivationServiceInstance

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.KeyDerivationServiceRegistryApi(peacemakr.generated.ApiClient(configuration))
key_derivation_instance_id = 'key_derivation_instance_id_example' # str | 
active = 'active_example' # str | 

try:
    # Activate or deactivate an existing KeyDerivationServiceInstance
    api_instance.delete_key_derivation_service_instance(key_derivation_instance_id, active)
except ApiException as e:
    print("Exception when calling KeyDerivationServiceRegistryApi->delete_key_derivation_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_derivation_instance_id** | **str**|  | 
 **active** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_org_key_derivation_service_instances**
> list[KeyDerivationInstance] get_all_org_key_derivation_service_instances()

Get the all key derivers registerd to org

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.KeyDerivationServiceRegistryApi(peacemakr.generated.ApiClient(configuration))

try:
    # Get the all key derivers registerd to org
    api_response = api_instance.get_all_org_key_derivation_service_instances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyDerivationServiceRegistryApi->get_all_org_key_derivation_service_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[KeyDerivationInstance]**](KeyDerivationInstance.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_shared_key_derivation_service_instances**
> list[KeyDerivationInstance] get_all_shared_key_derivation_service_instances()

Get the all key derivers that the org has access to - including shared cloud instances

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.KeyDerivationServiceRegistryApi(peacemakr.generated.ApiClient(configuration))

try:
    # Get the all key derivers that the org has access to - including shared cloud instances
    api_response = api_instance.get_all_shared_key_derivation_service_instances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyDerivationServiceRegistryApi->get_all_shared_key_derivation_service_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[KeyDerivationInstance]**](KeyDerivationInstance.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_derivation_service_instance**
> KeyDerivationInstance get_key_derivation_service_instance(key_derivation_instance_id)

Get the keyderiver details by id

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.KeyDerivationServiceRegistryApi(peacemakr.generated.ApiClient(configuration))
key_derivation_instance_id = 'key_derivation_instance_id_example' # str | 

try:
    # Get the keyderiver details by id
    api_response = api_instance.get_key_derivation_service_instance(key_derivation_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyDerivationServiceRegistryApi->get_key_derivation_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_derivation_instance_id** | **str**|  | 

### Return type

[**KeyDerivationInstance**](KeyDerivationInstance.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heartbeat_key_derivation_service_instance**
> HeatbeatResponse heartbeat_key_derivation_service_instance(key_derivation_instance_id)

Heatbeat from the given key derivation service instance

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.KeyDerivationServiceRegistryApi(peacemakr.generated.ApiClient(configuration))
key_derivation_instance_id = 'key_derivation_instance_id_example' # str | 

try:
    # Heatbeat from the given key derivation service instance
    api_response = api_instance.heartbeat_key_derivation_service_instance(key_derivation_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyDerivationServiceRegistryApi->heartbeat_key_derivation_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_derivation_instance_id** | **str**|  | 

### Return type

[**HeatbeatResponse**](HeatbeatResponse.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

