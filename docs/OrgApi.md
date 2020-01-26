# peacemakr_sdk.OrgApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_admin_to_org**](OrgApi.md#add_admin_to_org) | **POST** /org/admin | Add a new admin to this org
[**add_api_key_to_org**](OrgApi.md#add_api_key_to_org) | **POST** /org/key | Add a new API Key to an org
[**add_organization**](OrgApi.md#add_organization) | **POST** /org | Create a new organization. Must be an authenticated request with a valid id_token from a trusted IdP.
[**delete_admin_from_org**](OrgApi.md#delete_admin_from_org) | **DELETE** /org/admin/{email} | Remove an existing admin from the org (You can not remove the last admin. It will faile with a Bad Request response.)
[**delete_api_key_from_org**](OrgApi.md#delete_api_key_from_org) | **DELETE** /org/key/{apikey} | Remove an existing API Key
[**delete_organization**](OrgApi.md#delete_organization) | **DELETE** /org/{orgId} | Remove an existing organization
[**get_cloud_organization_api_key**](OrgApi.md#get_cloud_organization_api_key) | **GET** /org/key/sharedCloud | Get an access key for the peacemakr shared cloud org (all cloud key derivers must use this)
[**get_organization**](OrgApi.md#get_organization) | **GET** /org/{orgId} | Get an existing organization
[**get_organization_from_api_key**](OrgApi.md#get_organization_from_api_key) | **GET** /org/key/{apikey} | Get an existing Organization
[**get_test_organization_api_key**](OrgApi.md#get_test_organization_api_key) | **GET** /org/key/test | Get an ephemeral test org api key
[**update_stripe_customer_id**](OrgApi.md#update_stripe_customer_id) | **POST** /org/stripeId | Update the stripe customer Id associated with this account


# **add_admin_to_org**
> Contact add_admin_to_org(contact)

Add a new admin to this org

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
contact = peacemakr_sdk.Contact() # Contact | 

try:
    # Add a new admin to this org
    api_response = api_instance.add_admin_to_org(contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->add_admin_to_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_api_key_to_org**
> APIKey add_api_key_to_org()

Add a new API Key to an org

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))

try:
    # Add a new API Key to an org
    api_response = api_instance.add_api_key_to_org()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->add_api_key_to_org: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIKey**](APIKey.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_organization**
> Organization add_organization(id_token, stripe_customer_id, org_name, contact)

Create a new organization. Must be an authenticated request with a valid id_token from a trusted IdP.

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
id_token = 'id_token_example' # str | 
stripe_customer_id = 'stripe_customer_id_example' # str | 
org_name = 'org_name_example' # str | 
contact = peacemakr_sdk.Contact() # Contact | 

try:
    # Create a new organization. Must be an authenticated request with a valid id_token from a trusted IdP.
    api_response = api_instance.add_organization(id_token, stripe_customer_id, org_name, contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->add_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_token** | **str**|  | 
 **stripe_customer_id** | **str**|  | 
 **org_name** | **str**|  | 
 **contact** | [**Contact**](Contact.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_from_org**
> delete_admin_from_org(email)

Remove an existing admin from the org (You can not remove the last admin. It will faile with a Bad Request response.)

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
email = 'email_example' # str | 

try:
    # Remove an existing admin from the org (You can not remove the last admin. It will faile with a Bad Request response.)
    api_instance.delete_admin_from_org(email)
except ApiException as e:
    print("Exception when calling OrgApi->delete_admin_from_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key_from_org**
> delete_api_key_from_org(apikey)

Remove an existing API Key

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
apikey = 'apikey_example' # str | 

try:
    # Remove an existing API Key
    api_instance.delete_api_key_from_org(apikey)
except ApiException as e:
    print("Exception when calling OrgApi->delete_api_key_from_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> delete_organization(org_id)

Remove an existing organization

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
org_id = 'org_id_example' # str | 

try:
    # Remove an existing organization
    api_instance.delete_organization(org_id)
except ApiException as e:
    print("Exception when calling OrgApi->delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_organization_api_key**
> APIKey get_cloud_organization_api_key()

Get an access key for the peacemakr shared cloud org (all cloud key derivers must use this)

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))

try:
    # Get an access key for the peacemakr shared cloud org (all cloud key derivers must use this)
    api_response = api_instance.get_cloud_organization_api_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_cloud_organization_api_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIKey**](APIKey.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> Organization get_organization(org_id)

Get an existing organization

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
org_id = 'org_id_example' # str | 

try:
    # Get an existing organization
    api_response = api_instance.get_organization(org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_from_api_key**
> Organization get_organization_from_api_key(apikey)

Get an existing Organization

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
apikey = 'apikey_example' # str | 

try:
    # Get an existing Organization
    api_response = api_instance.get_organization_from_api_key(apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_organization_from_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_organization_api_key**
> APIKey get_test_organization_api_key()

Get an ephemeral test org api key

### Example
```python
from __future__ import print_function
import time
import peacemakr_sdk
from peacemakr_sdk.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = peacemakr_sdk.OrgApi()

try:
    # Get an ephemeral test org api key
    api_response = api_instance.get_test_organization_api_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_test_organization_api_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIKey**](APIKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stripe_customer_id**
> APIKey update_stripe_customer_id(stripe_customer_id)

Update the stripe customer Id associated with this account

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
api_instance = peacemakr_sdk.OrgApi(peacemakr_sdk.generated.ApiClient(configuration))
stripe_customer_id = 'stripe_customer_id_example' # str | 

try:
    # Update the stripe customer Id associated with this account
    api_response = api_instance.update_stripe_customer_id(stripe_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->update_stripe_customer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_customer_id** | **str**|  | 

### Return type

[**APIKey**](APIKey.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

