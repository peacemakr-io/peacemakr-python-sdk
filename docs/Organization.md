# Organization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**contacts** | [**list[Contact]**](Contact.md) |  | 
**stripe_customer_id** | **str** | Identifies the the customer in Stripe associated with this org | [optional] 
**client_ids** | **list[str]** | Array of first 10 client id&#39;s registered to this org | 
**api_keys** | [**list[APIKey]**](APIKey.md) | Array of api keys registered to this org | 
**oidc_params** | [**list[OIDCAuthNParameters]**](OIDCAuthNParameters.md) | Array of OIDC params registered to this org | [optional] 
**manual_params** | [**list[ManualAuthNParameters]**](ManualAuthNParameters.md) | Array of manual auth params registered to this org | [optional] 
**crypto_config_id** | **str** | cryptoconfigId of this org | 
**number_of_registered_clients** | **int** | Number of registered clients to this org | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


