# peacemakr.OrgApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_admin_to_org**](OrgApi.md#add_admin_to_org) | **POST** /org/admin | Add a new admin to this org
[**add_api_key_to_org**](OrgApi.md#add_api_key_to_org) | **POST** /org/key | Add a new API Key to an org
[**add_id_p_to_org**](OrgApi.md#add_id_p_to_org) | **POST** /org/idp | Add the IdP specified in the body
[**add_organization**](OrgApi.md#add_organization) | **POST** /org | Create a new organization. Must be an authenticated request with a valid id_token from a trusted IdP.
[**add_pubkey_to_org**](OrgApi.md#add_pubkey_to_org) | **POST** /org/pubkey | Add the public key specified in the body. Returns the public key with populated key ID on success.
[**delete_admin_from_org**](OrgApi.md#delete_admin_from_org) | **DELETE** /org/admin/{email} | Remove an existing admin from the org (You can not remove the last admin. It will faile with a Bad Request response.)
[**delete_api_key_from_org**](OrgApi.md#delete_api_key_from_org) | **DELETE** /org/key/{apikey} | Remove an existing API Key
[**delete_id_p_from_org**](OrgApi.md#delete_id_p_from_org) | **DELETE** /org/idp | Remove the IdP specified by the url passed in the query from the org
[**delete_organization**](OrgApi.md#delete_organization) | **DELETE** /org/{orgId} | Remove an existing organization
[**delete_pubkey_from_org**](OrgApi.md#delete_pubkey_from_org) | **DELETE** /org/pubkey | Remove the public key specified by the url passed in the query from the org
[**get_cloud_organization_api_key**](OrgApi.md#get_cloud_organization_api_key) | **GET** /org/key/sharedCloud | Get an access key for the peacemakr shared cloud org (all cloud key derivers must use this)
[**get_organization**](OrgApi.md#get_organization) | **GET** /org/{orgId} | Get an existing organization
[**get_organization_from_api_key**](OrgApi.md#get_organization_from_api_key) | **GET** /org/key/{apikey} | Get an existing Organization
[**get_organization_from_token**](OrgApi.md#get_organization_from_token) | **GET** /org | Get an existing organization. Which org is dictated by the token presented for authentication.
[**get_test_organization_api_key**](OrgApi.md#get_test_organization_api_key) | **GET** /org/key/test | Get an ephemeral test org api key
[**update_stripe_customer_id**](OrgApi.md#update_stripe_customer_id) | **POST** /org/stripeId | Update the stripe customer Id associated with this account


# **add_admin_to_org**
> Contact add_admin_to_org(contact)

Add a new admin to this org

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
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
contact = peacemakr.Contact() # Contact | 

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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))

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

# **add_id_p_to_org**
> add_id_p_to_org(new_id_ps)

Add the IdP specified in the body

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
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
new_id_ps = [peacemakr.OIDCAuthNParameters()] # list[OIDCAuthNParameters] | 

try:
    # Add the IdP specified in the body
    api_instance.add_id_p_to_org(new_id_ps)
except ApiException as e:
    print("Exception when calling OrgApi->add_id_p_to_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_id_ps** | [**list[OIDCAuthNParameters]**](OIDCAuthNParameters.md)|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_organization**
> Organization add_organization(id_token, org_name, params, stripe_customer_id=stripe_customer_id)

Create a new organization. Must be an authenticated request with a valid id_token from a trusted IdP.

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
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
id_token = 'id_token_example' # str | 
org_name = 'org_name_example' # str | 
params = peacemakr.AddOrganizationParameters() # AddOrganizationParameters | 
stripe_customer_id = 'stripe_customer_id_example' # str |  (optional)

try:
    # Create a new organization. Must be an authenticated request with a valid id_token from a trusted IdP.
    api_response = api_instance.add_organization(id_token, org_name, params, stripe_customer_id=stripe_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->add_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_token** | **str**|  | 
 **org_name** | **str**|  | 
 **params** | [**AddOrganizationParameters**](AddOrganizationParameters.md)|  | 
 **stripe_customer_id** | **str**|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pubkey_to_org**
> list[ManualAuthNParameters] add_pubkey_to_org(new_pubkeys)

Add the public key specified in the body. Returns the public key with populated key ID on success.

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
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
new_pubkeys = [peacemakr.ManualAuthNParameters()] # list[ManualAuthNParameters] | 

try:
    # Add the public key specified in the body. Returns the public key with populated key ID on success.
    api_response = api_instance.add_pubkey_to_org(new_pubkeys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->add_pubkey_to_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_pubkeys** | [**list[ManualAuthNParameters]**](ManualAuthNParameters.md)|  | 

### Return type

[**list[ManualAuthNParameters]**](ManualAuthNParameters.md)

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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
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

# **delete_id_p_from_org**
> delete_id_p_from_org(idp_url)

Remove the IdP specified by the url passed in the query from the org

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
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
idp_url = 'idp_url_example' # str | 

try:
    # Remove the IdP specified by the url passed in the query from the org
    api_instance.delete_id_p_from_org(idp_url)
except ApiException as e:
    print("Exception when calling OrgApi->delete_id_p_from_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_url** | **str**|  | 

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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
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

# **delete_pubkey_from_org**
> delete_pubkey_from_org(keyid)

Remove the public key specified by the url passed in the query from the org

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
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
keyid = 'keyid_example' # str | 

try:
    # Remove the public key specified by the url passed in the query from the org
    api_instance.delete_pubkey_from_org(keyid)
except ApiException as e:
    print("Exception when calling OrgApi->delete_pubkey_from_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyid** | **str**|  | 

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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))

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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
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

# **get_organization_from_token**
> Organization get_organization_from_token()

Get an existing organization. Which org is dictated by the token presented for authentication.

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
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))

try:
    # Get an existing organization. Which org is dictated by the token presented for authentication.
    api_response = api_instance.get_organization_from_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgApi->get_organization_from_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = peacemakr.OrgApi()

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
import peacemakr
from peacemakr.rest import ApiException
from pprint import pprint

# Configure API key authorization: header
configuration = peacemakr.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = peacemakr.OrgApi(peacemakr.generated.apiClient(configuration))
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

