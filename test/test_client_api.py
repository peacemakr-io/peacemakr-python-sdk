# coding: utf-8

"""
    Peacemakr

    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import peacemakr_sdk
from peacemakr_sdk.api.client_api import ClientApi  # noqa: E501
from peacemakr_sdk.rest import ApiException


class TestClientApi(unittest.TestCase):
    """ClientApi unit test stubs"""

    def setUp(self):
        self.api = peacemakr_sdk.api.client_api.ClientApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_client(self):
        """Test case for add_client

        Register a new client  # noqa: E501
        """
        pass

    def test_add_client_public_key(self):
        """Test case for add_client_public_key

        Register a new public key for the client  # noqa: E501
        """
        pass

    def test_delete_client(self):
        """Test case for delete_client

        Remove an existing organization  # noqa: E501
        """
        pass

    def test_get_client(self):
        """Test case for get_client

        Get an existing client  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
