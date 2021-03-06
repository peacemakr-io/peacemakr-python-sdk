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
from peacemakr.generated.api.login_api import LoginApi  # noqa: E501
from peacemakr.generated.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = peacemakr.generated.api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login(self):
        """Test case for login

        After aquiring and OAuth2 openId id_token from IdP (like google login), present it here and proceed with the required flow.  If this is a new user, they'll have to create an org, else, they will just get their org details, and an APIKey associated with their org.  # noqa: E501
        """
        pass

    def test_login_invite_user(self):
        """Test case for login_invite_user

        Invite (bind) an existing user that is not already bound to an org, to your org  # noqa: E501
        """
        pass

    def test_login_uninvite_user(self):
        """Test case for login_uninvite_user

        Uninvite (remove) an existing user that is part of your org  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
