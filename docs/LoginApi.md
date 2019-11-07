# peacemakr_sdk.LoginApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginApi.md#login) | **GET** /login | After aquiring and OAuth2 openId id_token from IdP (like google login), present it here and proceed with the required flow.  If this is a new user, they&#39;ll have to create an org, else, they will just get their org details, and an APIKey associated with their org.
[**login_invite_user**](LoginApi.md#login_invite_user) | **POST** /login/inviteUser | Invite (bind) an existing user that is not already bound to an org, to your org
[**login_uninvite_user**](LoginApi.md#login_uninvite_user) | **DELETE** /login/inviteUser | Uninvite (remove) an existing user that is part of your org


# **login**
> LoginResponse login(id_token)

After aquiring and OAuth2 openId id_token from IdP (like google login), present it here and proceed with the required flow.  If this is a new user, they'll have to create an org, else, they will just get their org details, and an APIKey associated with their org.

### Example
```python
from __future__ import print_function
import time
import peacemakr_sdk
from peacemakr_sdk.generated.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = peacemakr_sdk.LoginApi()
id_token = 'id_token_example' # str | 

try:
    # After aquiring and OAuth2 openId id_token from IdP (like google login), present it here and proceed with the required flow.  If this is a new user, they'll have to create an org, else, they will just get their org details, and an APIKey associated with their org.
    api_response = api_instance.login(id_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_token** | **str**|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_invite_user**
> login_invite_user(email)

Invite (bind) an existing user that is not already bound to an org, to your org

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
api_instance = peacemakr_sdk.LoginApi(peacemakr_sdk.generated.ApiClient(configuration))
email = 'email_example' # str | 

try:
    # Invite (bind) an existing user that is not already bound to an org, to your org
    api_instance.login_invite_user(email)
except ApiException as e:
    print("Exception when calling LoginApi->login_invite_user: %s\n" % e)
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

# **login_uninvite_user**
> login_uninvite_user(email)

Uninvite (remove) an existing user that is part of your org

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
api_instance = peacemakr_sdk.LoginApi(peacemakr_sdk.generated.ApiClient(configuration))
email = 'email_example' # str | 

try:
    # Uninvite (remove) an existing user that is part of your org
    api_instance.login_uninvite_user(email)
except ApiException as e:
    print("Exception when calling LoginApi->login_uninvite_user: %s\n" % e)
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

