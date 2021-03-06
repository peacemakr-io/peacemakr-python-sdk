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

from peacemakr.generated.api_client import ApiClient


class KeyDerivationServiceRegistryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_key_derivation_service_instance(self, **kwargs):  # noqa: E501
        """Register a new KeyDerivationServiceInstance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_key_derivation_service_instance(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KeyDerivationInstance key_derivation_instance:
        :return: KeyDerivationInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_key_derivation_service_instance_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_key_derivation_service_instance_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_key_derivation_service_instance_with_http_info(self, **kwargs):  # noqa: E501
        """Register a new KeyDerivationServiceInstance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_key_derivation_service_instance_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KeyDerivationInstance key_derivation_instance:
        :return: KeyDerivationInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_derivation_instance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_key_derivation_service_instance" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'key_derivation_instance' in params:
            body_params = params['key_derivation_instance']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['header']  # noqa: E501

        return self.api_client.call_api(
            '/crypto/deriver/instance', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KeyDerivationInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_key_derivation_service_instance(self, key_derivation_instance_id, active, **kwargs):  # noqa: E501
        """Activate or deactivate an existing KeyDerivationServiceInstance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_key_derivation_service_instance(key_derivation_instance_id, active, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_derivation_instance_id: (required)
        :param str active: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_key_derivation_service_instance_with_http_info(key_derivation_instance_id, active, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_key_derivation_service_instance_with_http_info(key_derivation_instance_id, active, **kwargs)  # noqa: E501
            return data

    def delete_key_derivation_service_instance_with_http_info(self, key_derivation_instance_id, active, **kwargs):  # noqa: E501
        """Activate or deactivate an existing KeyDerivationServiceInstance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_key_derivation_service_instance_with_http_info(key_derivation_instance_id, active, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_derivation_instance_id: (required)
        :param str active: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_derivation_instance_id', 'active']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_key_derivation_service_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_derivation_instance_id' is set
        if ('key_derivation_instance_id' not in params or
                params['key_derivation_instance_id'] is None):
            raise ValueError("Missing the required parameter `key_derivation_instance_id` when calling `delete_key_derivation_service_instance`")  # noqa: E501
        # verify the required parameter 'active' is set
        if ('active' not in params or
                params['active'] is None):
            raise ValueError("Missing the required parameter `active` when calling `delete_key_derivation_service_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_derivation_instance_id' in params:
            path_params['keyDerivationInstanceId'] = params['key_derivation_instance_id']  # noqa: E501

        query_params = []
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501

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
            '/crypto/deriver/instance/{keyDerivationInstanceId}', 'DELETE',
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

    def get_all_org_key_derivation_service_instances(self, **kwargs):  # noqa: E501
        """Get the all key derivers registerd to org  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_org_key_derivation_service_instances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[KeyDerivationInstance]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_org_key_derivation_service_instances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_org_key_derivation_service_instances_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_org_key_derivation_service_instances_with_http_info(self, **kwargs):  # noqa: E501
        """Get the all key derivers registerd to org  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_org_key_derivation_service_instances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[KeyDerivationInstance]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_org_key_derivation_service_instances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/crypto/deriver/all-org-instances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[KeyDerivationInstance]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_shared_key_derivation_service_instances(self, **kwargs):  # noqa: E501
        """Get the all key derivers that the org has access to - including shared cloud instances  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_shared_key_derivation_service_instances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[KeyDerivationInstance]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_shared_key_derivation_service_instances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_shared_key_derivation_service_instances_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_shared_key_derivation_service_instances_with_http_info(self, **kwargs):  # noqa: E501
        """Get the all key derivers that the org has access to - including shared cloud instances  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_shared_key_derivation_service_instances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[KeyDerivationInstance]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_shared_key_derivation_service_instances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/crypto/deriver/all-shared-instances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[KeyDerivationInstance]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_key_derivation_service_instance(self, key_derivation_instance_id, **kwargs):  # noqa: E501
        """Get the keyderiver details by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_key_derivation_service_instance(key_derivation_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_derivation_instance_id: (required)
        :return: KeyDerivationInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_key_derivation_service_instance_with_http_info(key_derivation_instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_key_derivation_service_instance_with_http_info(key_derivation_instance_id, **kwargs)  # noqa: E501
            return data

    def get_key_derivation_service_instance_with_http_info(self, key_derivation_instance_id, **kwargs):  # noqa: E501
        """Get the keyderiver details by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_key_derivation_service_instance_with_http_info(key_derivation_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_derivation_instance_id: (required)
        :return: KeyDerivationInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_derivation_instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_key_derivation_service_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_derivation_instance_id' is set
        if ('key_derivation_instance_id' not in params or
                params['key_derivation_instance_id'] is None):
            raise ValueError("Missing the required parameter `key_derivation_instance_id` when calling `get_key_derivation_service_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_derivation_instance_id' in params:
            path_params['keyDerivationInstanceId'] = params['key_derivation_instance_id']  # noqa: E501

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
            '/crypto/deriver/instance/{keyDerivationInstanceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KeyDerivationInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def heartbeat_key_derivation_service_instance(self, key_derivation_instance_id, **kwargs):  # noqa: E501
        """Heatbeat from the given key derivation service instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heartbeat_key_derivation_service_instance(key_derivation_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_derivation_instance_id: (required)
        :return: HeatbeatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.heartbeat_key_derivation_service_instance_with_http_info(key_derivation_instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.heartbeat_key_derivation_service_instance_with_http_info(key_derivation_instance_id, **kwargs)  # noqa: E501
            return data

    def heartbeat_key_derivation_service_instance_with_http_info(self, key_derivation_instance_id, **kwargs):  # noqa: E501
        """Heatbeat from the given key derivation service instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.heartbeat_key_derivation_service_instance_with_http_info(key_derivation_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key_derivation_instance_id: (required)
        :return: HeatbeatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_derivation_instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method heartbeat_key_derivation_service_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_derivation_instance_id' is set
        if ('key_derivation_instance_id' not in params or
                params['key_derivation_instance_id'] is None):
            raise ValueError("Missing the required parameter `key_derivation_instance_id` when calling `heartbeat_key_derivation_service_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_derivation_instance_id' in params:
            path_params['keyDerivationInstanceId'] = params['key_derivation_instance_id']  # noqa: E501

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
            '/crypto/deriver/instance/{keyDerivationInstanceId}/heartbeat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HeatbeatResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
