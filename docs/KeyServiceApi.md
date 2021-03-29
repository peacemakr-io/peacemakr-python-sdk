# peacemakr.KeyServiceApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_encrypted_keys**](KeyServiceApi.md#get_all_encrypted_keys) | **GET** /crypto/symmetric/{encryptingKeyId} | Get all encrypted symmetric keys that are encrypted with this encrypting keyId, optionally limiting the request to a set of symmetric key domains
[**get_public_key**](KeyServiceApi.md#get_public_key) | **GET** /crypto/asymmetric/{keyID} | Get the public key associated with the passed-in key ID
[**post_new_encrypted_keys**](KeyServiceApi.md#post_new_encrypted_keys) | **POST** /crypto/symmetric/{encryptingKeyId} | Add a new encrypted key. The encrypting key that protects the encrypted key is identified with encryptingKeyId. Request must come from a registered key manager.


# **get_all_encrypted_keys**
> list[EncryptedSymmetricKey] get_all_encrypted_keys(encrypting_key_id, symmetric_key_ids=symmetric_key_ids)

Get all encrypted symmetric keys that are encrypted with this encrypting keyId, optionally limiting the request to a set of symmetric key domains

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
api_instance = peacemakr.KeyServiceApi(peacemakr.generated.apiClient(configuration))
encrypting_key_id = 'encrypting_key_id_example' # str | 
symmetric_key_ids = ['symmetric_key_ids_example'] # list[str] |  (optional)

try:
    # Get all encrypted symmetric keys that are encrypted with this encrypting keyId, optionally limiting the request to a set of symmetric key domains
    api_response = api_instance.get_all_encrypted_keys(encrypting_key_id, symmetric_key_ids=symmetric_key_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyServiceApi->get_all_encrypted_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypting_key_id** | **str**|  | 
 **symmetric_key_ids** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**list[EncryptedSymmetricKey]**](EncryptedSymmetricKey.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_key**
> PublicKey get_public_key(key_id)

Get the public key associated with the passed-in key ID

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
api_instance = peacemakr.KeyServiceApi(peacemakr.generated.apiClient(configuration))
key_id = 'key_id_example' # str | 

try:
    # Get the public key associated with the passed-in key ID
    api_response = api_instance.get_public_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyServiceApi->get_public_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

[**PublicKey**](PublicKey.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_new_encrypted_keys**
> post_new_encrypted_keys(encrypting_key_id, encrypted_symmetric_key)

Add a new encrypted key. The encrypting key that protects the encrypted key is identified with encryptingKeyId. Request must come from a registered key manager.

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
api_instance = peacemakr.KeyServiceApi(peacemakr.generated.apiClient(configuration))
encrypting_key_id = 'encrypting_key_id_example' # str | 
encrypted_symmetric_key = [peacemakr.EncryptedSymmetricKey()] # list[EncryptedSymmetricKey] | 

try:
    # Add a new encrypted key. The encrypting key that protects the encrypted key is identified with encryptingKeyId. Request must come from a registered key manager.
    api_instance.post_new_encrypted_keys(encrypting_key_id, encrypted_symmetric_key)
except ApiException as e:
    print("Exception when calling KeyServiceApi->post_new_encrypted_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypting_key_id** | **str**|  | 
 **encrypted_symmetric_key** | [**list[EncryptedSymmetricKey]**](EncryptedSymmetricKey.md)|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

