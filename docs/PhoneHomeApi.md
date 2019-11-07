# peacemakr_sdk.PhoneHomeApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_post**](PhoneHomeApi.md#log_post) | **POST** /log | Used to report back to server a logged event


# **log_post**
> log_post(log)

Used to report back to server a logged event

Returns 200 ok if successfully persisted

### Example
```python
from __future__ import print_function
import time
import peacemakr_sdk
from peacemakr_sdk.generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr_sdk.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr_sdk.PhoneHomeApi(peacemakr_sdk.generated.ApiClient(configuration))
log = peacemakr_sdk.Log() # Log | 

try:
    # Used to report back to server a logged event
    api_instance.log_post(log)
except ApiException as e:
    print("Exception when calling PhoneHomeApi->log_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log** | [**Log**](Log.md)|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

