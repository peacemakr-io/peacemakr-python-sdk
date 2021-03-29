# peacemakr.CryptoConfigApi

All URIs are relative to *http://api.peacemakr.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_collaborator**](CryptoConfigApi.md#add_collaborator) | **POST** /crypto/useDomain/{useDomainId}/collaborator | Add a collaborating org
[**add_existing_use_domain**](CryptoConfigApi.md#add_existing_use_domain) | **POST** /crypto/config/{cryptoConfigId}/useDomain/{useDomainId} | Add an existing use domain to another crypto config.
[**add_use_domain**](CryptoConfigApi.md#add_use_domain) | **POST** /crypto/config/{cryptoConfigId}/useDomain | Add a new active use domain and attached it to the crypto config.
[**get_crypto_config**](CryptoConfigApi.md#get_crypto_config) | **GET** /crypto/config/{cryptoConfigId} | Get the crypto configurations
[**rapid_rotation_use_domain**](CryptoConfigApi.md#rapid_rotation_use_domain) | **POST** /crypto/useDomain/{useDomainId}/rapidRotation | Rapid expiration of existing use doamin and immediately replacment with an identical use domain containing fresh keys
[**remove_collaborator**](CryptoConfigApi.md#remove_collaborator) | **DELETE** /crypto/useDomain/{useDomainId}/collaborator | Remove a collaborating org
[**remove_use_domain**](CryptoConfigApi.md#remove_use_domain) | **DELETE** /crypto/useDomain/{useDomainId} | Delete a fully expired use domain
[**update_crypto_config**](CryptoConfigApi.md#update_crypto_config) | **POST** /crypto/config/{cryptoConfigId} | Update the crypto configuration, ONLY the clientKeyType clientKeyBitlength, and clientKeyTTL fields.
[**update_crypto_config_fallback_to_cloud**](CryptoConfigApi.md#update_crypto_config_fallback_to_cloud) | **PUT** /crypto/useDomain/{useDomainId}/enableKDSFallbackToCloud | Update an existing crypto config&#39;s asymmetricKeyTTL
[**update_crypto_config_selector_scheme**](CryptoConfigApi.md#update_crypto_config_selector_scheme) | **PUT** /crypto/config/{cryptoConfigId}/domainSelectorScheme | Update an existing crypto config&#39;s domainSelectorScheme
[**update_expire_use_domain**](CryptoConfigApi.md#update_expire_use_domain) | **POST** /crypto/useDomain/{useDomainId}/updateExpire | Chnage expiration of a use domain


# **add_collaborator**
> TinyOrg add_collaborator(use_domain_id, collaborating_org_id, id_token)

Add a collaborating org

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
use_domain_id = 'use_domain_id_example' # str | 
collaborating_org_id = 'collaborating_org_id_example' # str | 
id_token = 'id_token_example' # str | 

try:
    # Add a collaborating org
    api_response = api_instance.add_collaborator(use_domain_id, collaborating_org_id, id_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->add_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_domain_id** | **str**|  | 
 **collaborating_org_id** | **str**|  | 
 **id_token** | **str**|  | 

### Return type

[**TinyOrg**](TinyOrg.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_existing_use_domain**
> add_existing_use_domain(crypto_config_id, use_domain_id)

Add an existing use domain to another crypto config.

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
crypto_config_id = 'crypto_config_id_example' # str | 
use_domain_id = 'use_domain_id_example' # str | 

try:
    # Add an existing use domain to another crypto config.
    api_instance.add_existing_use_domain(crypto_config_id, use_domain_id)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->add_existing_use_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_config_id** | **str**|  | 
 **use_domain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_use_domain**
> SymmetricKeyUseDomain add_use_domain(crypto_config_id, new_use_domain)

Add a new active use domain and attached it to the crypto config.

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
crypto_config_id = 'crypto_config_id_example' # str | 
new_use_domain = peacemakr.SymmetricKeyUseDomain() # SymmetricKeyUseDomain | 

try:
    # Add a new active use domain and attached it to the crypto config.
    api_response = api_instance.add_use_domain(crypto_config_id, new_use_domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->add_use_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_config_id** | **str**|  | 
 **new_use_domain** | [**SymmetricKeyUseDomain**](SymmetricKeyUseDomain.md)|  | 

### Return type

[**SymmetricKeyUseDomain**](SymmetricKeyUseDomain.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_config**
> CryptoConfig get_crypto_config(crypto_config_id)

Get the crypto configurations

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
crypto_config_id = 'crypto_config_id_example' # str | 

try:
    # Get the crypto configurations
    api_response = api_instance.get_crypto_config(crypto_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->get_crypto_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_config_id** | **str**|  | 

### Return type

[**CryptoConfig**](CryptoConfig.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rapid_rotation_use_domain**
> rapid_rotation_use_domain(use_domain_id, optional_next_key_derivation_service_id=optional_next_key_derivation_service_id)

Rapid expiration of existing use doamin and immediately replacment with an identical use domain containing fresh keys

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
use_domain_id = 'use_domain_id_example' # str | 
optional_next_key_derivation_service_id = 'optional_next_key_derivation_service_id_example' # str |  (optional)

try:
    # Rapid expiration of existing use doamin and immediately replacment with an identical use domain containing fresh keys
    api_instance.rapid_rotation_use_domain(use_domain_id, optional_next_key_derivation_service_id=optional_next_key_derivation_service_id)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->rapid_rotation_use_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_domain_id** | **str**|  | 
 **optional_next_key_derivation_service_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_collaborator**
> remove_collaborator(use_domain_id, collaborating_org_id, id_token)

Remove a collaborating org

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
use_domain_id = 'use_domain_id_example' # str | 
collaborating_org_id = 'collaborating_org_id_example' # str | 
id_token = 'id_token_example' # str | 

try:
    # Remove a collaborating org
    api_instance.remove_collaborator(use_domain_id, collaborating_org_id, id_token)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->remove_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_domain_id** | **str**|  | 
 **collaborating_org_id** | **str**|  | 
 **id_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_use_domain**
> remove_use_domain(use_domain_id)

Delete a fully expired use domain

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
use_domain_id = 'use_domain_id_example' # str | 

try:
    # Delete a fully expired use domain
    api_instance.remove_use_domain(use_domain_id)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->remove_use_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_domain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crypto_config**
> CryptoConfig update_crypto_config(crypto_config_id, updated_crypto_config)

Update the crypto configuration, ONLY the clientKeyType clientKeyBitlength, and clientKeyTTL fields.

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
crypto_config_id = 'crypto_config_id_example' # str | 
updated_crypto_config = peacemakr.CryptoConfig() # CryptoConfig | 

try:
    # Update the crypto configuration, ONLY the clientKeyType clientKeyBitlength, and clientKeyTTL fields.
    api_response = api_instance.update_crypto_config(crypto_config_id, updated_crypto_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->update_crypto_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_config_id** | **str**|  | 
 **updated_crypto_config** | [**CryptoConfig**](CryptoConfig.md)|  | 

### Return type

[**CryptoConfig**](CryptoConfig.md)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crypto_config_fallback_to_cloud**
> update_crypto_config_fallback_to_cloud(use_domain_id, fallback_to_cloud)

Update an existing crypto config's asymmetricKeyTTL

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
use_domain_id = 'use_domain_id_example' # str | 
fallback_to_cloud = true # bool | 

try:
    # Update an existing crypto config's asymmetricKeyTTL
    api_instance.update_crypto_config_fallback_to_cloud(use_domain_id, fallback_to_cloud)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->update_crypto_config_fallback_to_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_domain_id** | **str**|  | 
 **fallback_to_cloud** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crypto_config_selector_scheme**
> update_crypto_config_selector_scheme(crypto_config_id, new_selector_scheme)

Update an existing crypto config's domainSelectorScheme

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
crypto_config_id = 'crypto_config_id_example' # str | 
new_selector_scheme = 'new_selector_scheme_example' # str | 

try:
    # Update an existing crypto config's domainSelectorScheme
    api_instance.update_crypto_config_selector_scheme(crypto_config_id, new_selector_scheme)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->update_crypto_config_selector_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_config_id** | **str**|  | 
 **new_selector_scheme** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expire_use_domain**
> update_expire_use_domain(use_domain_id, inception_ttl, encryption_ttl, decryption_ttl, retention_ttl)

Chnage expiration of a use domain

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
api_instance = peacemakr.CryptoConfigApi(peacemakr.generated.apiClient(configuration))
use_domain_id = 'use_domain_id_example' # str | 
inception_ttl = 56 # int | 
encryption_ttl = 56 # int | 
decryption_ttl = 56 # int | 
retention_ttl = 56 # int | 

try:
    # Chnage expiration of a use domain
    api_instance.update_expire_use_domain(use_domain_id, inception_ttl, encryption_ttl, decryption_ttl, retention_ttl)
except ApiException as e:
    print("Exception when calling CryptoConfigApi->update_expire_use_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_domain_id** | **str**|  | 
 **inception_ttl** | **int**|  | 
 **encryption_ttl** | **int**|  | 
 **decryption_ttl** | **int**|  | 
 **retention_ttl** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[header](../README.md#header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

