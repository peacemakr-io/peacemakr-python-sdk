# SymmetricKeyUseDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**owner_org_id** | **str** | the org id of the organization that owns these symmetric keys | 
**name** | **str** |  | [optional] 
**creation_time** | **int** |  | 
**symmetric_key_inception_ttl** | **int** | number of seconds since key creation that the key will be available for encryption | 
**symmetric_key_encryption_use_ttl** | **int** | number of seconds since key creation that the key will be available for encryption | 
**symmetric_key_encryption_allowed** | **bool** | whether this use domain is available for encryption; if false, these keys should not be used for encrypting new messages | [optional] 
**symmetric_key_decryption_use_ttl** | **int** | number of seconds since key creation that the key will be available for decryption | 
**symmetric_key_decryption_allowed** | **bool** | whether this use domain is available for decryption; if false, these keys should not be used for decrypting messages | [optional] 
**symmetric_key_retention_use_ttl** | **int** | number of seconds since key creation that the key will be available for retention purposes | 
**symmetric_key_length** | **int** | the number of bits of all symmetric keys in this use domain | 
**symmetric_key_encryption_alg** | **str** | the specific encryption alg to encrypt new plaintexts for application layer encryption operations | [default to 'CHACHA20_POLY1305']
**encrypting_packaged_ciphertext_version** | **int** | after encrypting new plaintexts, package the ciphertext with this version of the packaged ciphertext | 
**symmetric_key_derivation_service_id** | **str** | the symmetric key derivation serivce id that can derive and wrap these keys | 
**encryption_key_ids** | **list[str]** | these are the semmetric key id&#39;s that belong to this use domain - these keys never belong to any other use domain | 
**endable_kds_fallback_to_cloud** | **bool** | if all registered kds service become unreachable, then incoming requests for new and existing keys may fallback to the cloud provided KDS | 
**require_signed_key_delivery** | **bool** | if required, all clients must receive these keys in a signed symmetric key delivery from the key deriver | 
**digest_algorithm** | **str** | The digest algorithm to use for signing messages in this use domain | [optional] [default to 'SHA_256']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


