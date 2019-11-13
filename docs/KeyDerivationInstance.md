# KeyDerivationInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | instance id (concrete instance) | 
**service_ids** | **list[str]** | service id (virtual service id) | 
**active** | **bool** | currently online and accepting requests for key derivation | 
**version** | **str** |  | 
**base_url** | **str** | base URL from which this key deriver instance will respond to new key derivation job requests | [optional] 
**is_public** | **bool** | if true then the key deriver is visible to every other organization | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


