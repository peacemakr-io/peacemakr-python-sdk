# peacemakr.BillingApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_org_id_get**](BillingApi.md#billing_org_id_get) | **GET** /billing/{orgId} | Get the pricing plan for an org
[**billing_org_id_post**](BillingApi.md#billing_org_id_post) | **POST** /billing/{orgId} | Update the pricing plan for an org


# **billing_org_id_get**
> PricingPlan billing_org_id_get(org_id)

Get the pricing plan for an org

Returns the current pricing plan

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.BillingApi(peacemakr.generated.apiClient(configuration))
org_id = 'org_id_example' # str | 

try:
    # Get the pricing plan for an org
    api_response = api_instance.billing_org_id_get(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->billing_org_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**PricingPlan**](PricingPlan.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_org_id_post**
> billing_org_id_post(org_id, new_plan)

Update the pricing plan for an org

Returns 200 on successful pricing plan update

### Example
```python
from __future__ import print_function
import time
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.BillingApi(peacemakr.generated.apiClient(configuration))
org_id = 'org_id_example' # str | 
new_plan = peacemakr.PricingPlan() # PricingPlan | 

try:
    # Update the pricing plan for an org
    api_instance.billing_org_id_post(org_id, new_plan)
except ApiException as e:
    print("Exception when calling BillingApi->billing_org_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **new_plan** | [**PricingPlan**](PricingPlan.md)|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

