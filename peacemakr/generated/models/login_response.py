# coding: utf-8

"""
    Peacemakr

    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from peacemakr.generated.models.organization import Organization  # noqa: F401,E501


class LoginResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'must_create_org': 'bool',
        'message_ofthe_day': 'str',
        'org': 'Organization'
    }

    attribute_map = {
        'must_create_org': 'mustCreateOrg',
        'message_ofthe_day': 'messageOftheDay',
        'org': 'Org'
    }

    def __init__(self, must_create_org=None, message_ofthe_day=None, org=None):  # noqa: E501
        """LoginResponse - a model defined in Swagger"""  # noqa: E501

        self._must_create_org = None
        self._message_ofthe_day = None
        self._org = None
        self.discriminator = None

        if must_create_org is not None:
            self.must_create_org = must_create_org
        if message_ofthe_day is not None:
            self.message_ofthe_day = message_ofthe_day
        if org is not None:
            self.org = org

    @property
    def must_create_org(self):
        """Gets the must_create_org of this LoginResponse.  # noqa: E501

        if true, then the user is not attached to an existing org, and must create a new org  # noqa: E501

        :return: The must_create_org of this LoginResponse.  # noqa: E501
        :rtype: bool
        """
        return self._must_create_org

    @must_create_org.setter
    def must_create_org(self, must_create_org):
        """Sets the must_create_org of this LoginResponse.

        if true, then the user is not attached to an existing org, and must create a new org  # noqa: E501

        :param must_create_org: The must_create_org of this LoginResponse.  # noqa: E501
        :type: bool
        """

        self._must_create_org = must_create_org

    @property
    def message_ofthe_day(self):
        """Gets the message_ofthe_day of this LoginResponse.  # noqa: E501

        if set, please display this message to the user on login  # noqa: E501

        :return: The message_ofthe_day of this LoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._message_ofthe_day

    @message_ofthe_day.setter
    def message_ofthe_day(self, message_ofthe_day):
        """Sets the message_ofthe_day of this LoginResponse.

        if set, please display this message to the user on login  # noqa: E501

        :param message_ofthe_day: The message_ofthe_day of this LoginResponse.  # noqa: E501
        :type: str
        """

        self._message_ofthe_day = message_ofthe_day

    @property
    def org(self):
        """Gets the org of this LoginResponse.  # noqa: E501


        :return: The org of this LoginResponse.  # noqa: E501
        :rtype: Organization
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this LoginResponse.


        :param org: The org of this LoginResponse.  # noqa: E501
        :type: Organization
        """

        self._org = org

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LoginResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
