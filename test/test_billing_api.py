# coding: utf-8

"""
    Peacemakr

    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import peacemakr
from peacemakr.generated.api.billing_api import BillingApi  # noqa: E501
from peacemakr.rest import ApiException


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self):
        self.api = peacemakr.generated.api.billing_api.BillingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_billing_org_id_get(self):
        """Test case for billing_org_id_get

        Get the pricing plan for an org  # noqa: E501
        """
        pass

    def test_billing_org_id_post(self):
        """Test case for billing_org_id_post

        Update the pricing plan for an org  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
