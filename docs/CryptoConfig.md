# CryptoConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**symmetric_key_use_domains** | [**list[SymmetricKeyUseDomain]**](SymmetricKeyUseDomain.md) | every application layer encryption must select a key to use from one specific active semmetric key encryption domain. this is an array of encryption domains id&#39;s that are currently available for encryption | 
**symmetric_key_use_domain_selector_scheme** | **str** | to guide SDK&#39;s on how to select an encryption domain, a selectorScheme helps an SDK map a encryption request to a set of keys and encryption algoritm | 
**owner_org_id** | **str** | the org id of the organization that owns these symmetric keys | 
**client_key_type** | **str** | the type of key that should be associated with clients, for example, rsa | 
**client_key_bitlength** | **int** | the bit length of all new client keys, for example, 2048 | 
**client_key_ttl** | **int** | the TTL on the client&#39;s local asymetric key | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


