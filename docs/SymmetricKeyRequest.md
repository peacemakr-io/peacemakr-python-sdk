# SymmetricKeyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the symmetric key request. | 
**derive_symmetric_key_ids** | **list[str]** | These are the keyId&#39;s of for the symmetric keys to actually derive. | 
**delivery_public_key_ids** | **list[str]** | These are the keyId&#39;s to deliver all of the derived symmetric keys. | 
**key_derivation_service_id** | **str** | The serviceId that must generate these keys. | 
**creation_time** | **int** | Epoch time of the symmetric key requestion request time. | 
**symmetric_key_length** | **int** | Length in bytes of the derived symmetric keys. | 
**packaged_ciphertext_version** | **int** | After deriving symmetric keys, this determines the ciphertext packaging scheme required for encrypted key delivery. | 
**must_sign_delivered_symmetric_keys** | **bool** | If true the key deriver must sign delivered symmetric keys ciphertext blobs | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


