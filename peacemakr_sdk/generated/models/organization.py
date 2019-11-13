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

from peacemakr_sdk.generated.models.api_key import APIKey  # noqa: F401,E501
from peacemakr_sdk.generated.models.contact import Contact  # noqa: F401,E501


class Organization(object):
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
        'id': 'str',
        'name': 'str',
        'contacts': 'list[Contact]',
        'stripe_customer_id': 'str',
        'client_ids': 'list[str]',
        'api_keys': 'list[APIKey]',
        'crypto_config_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'contacts': 'contacts',
        'stripe_customer_id': 'stripeCustomerId',
        'client_ids': 'clientIds',
        'api_keys': 'apiKeys',
        'crypto_config_id': 'cryptoConfigId'
    }

    def __init__(self, id=None, name=None, contacts=None, stripe_customer_id=None, client_ids=None, api_keys=None, crypto_config_id=None):  # noqa: E501
        """Organization - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._contacts = None
        self._stripe_customer_id = None
        self._client_ids = None
        self._api_keys = None
        self._crypto_config_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.contacts = contacts
        self.stripe_customer_id = stripe_customer_id
        self.client_ids = client_ids
        self.api_keys = api_keys
        self.crypto_config_id = crypto_config_id

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501


        :return: The id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501


        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def contacts(self):
        """Gets the contacts of this Organization.  # noqa: E501


        :return: The contacts of this Organization.  # noqa: E501
        :rtype: list[Contact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this Organization.


        :param contacts: The contacts of this Organization.  # noqa: E501
        :type: list[Contact]
        """
        if contacts is None:
            raise ValueError("Invalid value for `contacts`, must not be `None`")  # noqa: E501

        self._contacts = contacts

    @property
    def stripe_customer_id(self):
        """Gets the stripe_customer_id of this Organization.  # noqa: E501

        Identifies the the customer in Stripe associated with this org  # noqa: E501

        :return: The stripe_customer_id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._stripe_customer_id

    @stripe_customer_id.setter
    def stripe_customer_id(self, stripe_customer_id):
        """Sets the stripe_customer_id of this Organization.

        Identifies the the customer in Stripe associated with this org  # noqa: E501

        :param stripe_customer_id: The stripe_customer_id of this Organization.  # noqa: E501
        :type: str
        """
        if stripe_customer_id is None:
            raise ValueError("Invalid value for `stripe_customer_id`, must not be `None`")  # noqa: E501

        self._stripe_customer_id = stripe_customer_id

    @property
    def client_ids(self):
        """Gets the client_ids of this Organization.  # noqa: E501

        Array of client id's registered to this org  # noqa: E501

        :return: The client_ids of this Organization.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids):
        """Sets the client_ids of this Organization.

        Array of client id's registered to this org  # noqa: E501

        :param client_ids: The client_ids of this Organization.  # noqa: E501
        :type: list[str]
        """
        if client_ids is None:
            raise ValueError("Invalid value for `client_ids`, must not be `None`")  # noqa: E501

        self._client_ids = client_ids

    @property
    def api_keys(self):
        """Gets the api_keys of this Organization.  # noqa: E501

        Array of api keys registered to this org  # noqa: E501

        :return: The api_keys of this Organization.  # noqa: E501
        :rtype: list[APIKey]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """Sets the api_keys of this Organization.

        Array of api keys registered to this org  # noqa: E501

        :param api_keys: The api_keys of this Organization.  # noqa: E501
        :type: list[APIKey]
        """
        if api_keys is None:
            raise ValueError("Invalid value for `api_keys`, must not be `None`")  # noqa: E501

        self._api_keys = api_keys

    @property
    def crypto_config_id(self):
        """Gets the crypto_config_id of this Organization.  # noqa: E501

        cryptoconfigId of this org  # noqa: E501

        :return: The crypto_config_id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._crypto_config_id

    @crypto_config_id.setter
    def crypto_config_id(self, crypto_config_id):
        """Sets the crypto_config_id of this Organization.

        cryptoconfigId of this org  # noqa: E501

        :param crypto_config_id: The crypto_config_id of this Organization.  # noqa: E501
        :type: str
        """
        if crypto_config_id is None:
            raise ValueError("Invalid value for `crypto_config_id`, must not be `None`")  # noqa: E501

        self._crypto_config_id = crypto_config_id

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
        if issubclass(Organization, dict):
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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
