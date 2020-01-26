# peacemakr.ServerManagementApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](ServerManagementApi.md#health_get) | **GET** /health | See if the server is healthy


# **health_get**
> health_get()

See if the server is healthy

Returns 200 if the server is healthy

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = peacemakr.ServerManagementApi()

try:
    # See if the server is healthy
    api_instance.health_get()
except ApiException as e:
    print("Exception when calling ServerManagementApi->health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

