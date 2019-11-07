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


class PhoneHomeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def log_post(self, log, **kwargs):  # noqa: E501
        """Used to report back to server a logged event  # noqa: E501

        Returns 200 ok if successfully persisted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_post(log, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Log log: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.log_post_with_http_info(log, **kwargs)  # noqa: E501
        else:
            (data) = self.log_post_with_http_info(log, **kwargs)  # noqa: E501
            return data

    def log_post_with_http_info(self, log, **kwargs):  # noqa: E501
        """Used to report back to server a logged event  # noqa: E501

        Returns 200 ok if successfully persisted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.log_post_with_http_info(log, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Log log: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['log']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method log_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'log' is set
        if ('log' not in params or
                params['log'] is None):
            raise ValueError("Missing the required parameter `log` when calling `log_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'log' in params:
            body_params = params['log']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['header']  # noqa: E501

        return self.api_client.call_api(
            '/log', 'POST',
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
