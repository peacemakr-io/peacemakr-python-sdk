# coding: utf-8

"""
    Peacemakr

    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from peacemakr_sdk.generated.api_client import ApiClient


class KeyServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_encrypted_keys(self, encrypting_key_id, **kwargs):  # noqa: E501
        """Get all encrypted symmetric keys that are encrypted with this encrypting keyId, optionally limiting the request to a set of symmetric key domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_encrypted_keys(encrypting_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str encrypting_key_id: (required)
        :param list[str] symmetric_key_ids:
        :return: list[EncryptedSymmetricKey]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_encrypted_keys_with_http_info(encrypting_key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_encrypted_keys_with_http_info(encrypting_key_id, **kwargs)  # noqa: E501
            return data

    def get_all_encrypted_keys_with_http_info(self, encrypting_key_id, **kwargs):  # noqa: E501
        """Get all encrypted symmetric keys that are encrypted with this encrypting keyId, optionally limiting the request to a set of symmetric key domains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_encrypted_keys_with_http_info(encrypting_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str encrypting_key_id: (required)
        :param list[str] symmetric_key_ids:
        :return: list[EncryptedSymmetricKey]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['encrypting_key_id', 'symmetric_key_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_encrypted_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'encrypting_key_id' is set
        if ('encrypting_key_id' not in params or
                params['encrypting_key_id'] is None):
            raise ValueError("Missing the required parameter `encrypting_key_id` when calling `get_all_encrypted_keys`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'encrypting_key_id' in params:
            path_params['encryptingKeyId'] = params['encrypting_key_id']  # noqa: E501

        query_params = []
        if 'symmetric_key_ids' in params:
            query_params.append(('symmetricKeyIds', params['symmetric_key_ids']))  # noqa: E501
            collection_formats['symmetricKeyIds'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['header']  # noqa: E501

        return self.api_client.call_api(
            '/crypto/symmetric/{encryptingKeyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EncryptedSymmetricKey]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_public_key(self, key_id, **kwargs):  # noqa: E501
        """Get the public key associated with the passed-in key ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_key(key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_id: (required)
        :return: PublicKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_public_key_with_http_info(key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_public_key_with_http_info(key_id, **kwargs)  # noqa: E501
            return data

    def get_public_key_with_http_info(self, key_id, **kwargs):  # noqa: E501
        """Get the public key associated with the passed-in key ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_public_key_with_http_info(key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_id: (required)
        :return: PublicKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_public_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params or
                params['key_id'] is None):
            raise ValueError("Missing the required parameter `key_id` when calling `get_public_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_id' in params:
            path_params['keyID'] = params['key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['header']  # noqa: E501

        return self.api_client.call_api(
            '/crypto/asymmetric/{keyID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicKey',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_new_encrypted_keys(self, encrypting_key_id, encrypted_symmetric_key, **kwargs):  # noqa: E501
        """Add a new encrypted key. The encrypting key that protects the encrypted key is identified with encryptingKeyId. Request must come from a registered key manager.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_new_encrypted_keys(encrypting_key_id, encrypted_symmetric_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str encrypting_key_id: (required)
        :param list[EncryptedSymmetricKey] encrypted_symmetric_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_new_encrypted_keys_with_http_info(encrypting_key_id, encrypted_symmetric_key, **kwargs)  # noqa: E501
        else:
            (data) = self.post_new_encrypted_keys_with_http_info(encrypting_key_id, encrypted_symmetric_key, **kwargs)  # noqa: E501
            return data

    def post_new_encrypted_keys_with_http_info(self, encrypting_key_id, encrypted_symmetric_key, **kwargs):  # noqa: E501
        """Add a new encrypted key. The encrypting key that protects the encrypted key is identified with encryptingKeyId. Request must come from a registered key manager.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_new_encrypted_keys_with_http_info(encrypting_key_id, encrypted_symmetric_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str encrypting_key_id: (required)
        :param list[EncryptedSymmetricKey] encrypted_symmetric_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['encrypting_key_id', 'encrypted_symmetric_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_new_encrypted_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'encrypting_key_id' is set
        if ('encrypting_key_id' not in params or
                params['encrypting_key_id'] is None):
            raise ValueError("Missing the required parameter `encrypting_key_id` when calling `post_new_encrypted_keys`")  # noqa: E501
        # verify the required parameter 'encrypted_symmetric_key' is set
        if ('encrypted_symmetric_key' not in params or
                params['encrypted_symmetric_key'] is None):
            raise ValueError("Missing the required parameter `encrypted_symmetric_key` when calling `post_new_encrypted_keys`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'encrypting_key_id' in params:
            path_params['encryptingKeyId'] = params['encrypting_key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'encrypted_symmetric_key' in params:
            body_params = params['encrypted_symmetric_key']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['header']  # noqa: E501

        return self.api_client.call_api(
            '/crypto/symmetric/{encryptingKeyId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
