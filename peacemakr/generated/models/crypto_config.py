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

from peacemakr.generated.models.symmetric_key_use_domain import SymmetricKeyUseDomain  # noqa: F401,E501


class CryptoConfig(object):
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
        'symmetric_key_use_domains': 'list[SymmetricKeyUseDomain]',
        'symmetric_key_use_domain_selector_scheme': 'str',
        'owner_org_id': 'str',
        'client_key_type': 'str',
        'client_key_bitlength': 'int',
        'client_key_ttl': 'int'
    }

    attribute_map = {
        'id': 'id',
        'symmetric_key_use_domains': 'symmetricKeyUseDomains',
        'symmetric_key_use_domain_selector_scheme': 'symmetricKeyUseDomainSelectorScheme',
        'owner_org_id': 'ownerOrgId',
        'client_key_type': 'clientKeyType',
        'client_key_bitlength': 'clientKeyBitlength',
        'client_key_ttl': 'clientKeyTTL'
    }

    def __init__(self, id=None, symmetric_key_use_domains=None, symmetric_key_use_domain_selector_scheme=None, owner_org_id=None, client_key_type=None, client_key_bitlength=None, client_key_ttl=None):  # noqa: E501
        """CryptoConfig - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._symmetric_key_use_domains = None
        self._symmetric_key_use_domain_selector_scheme = None
        self._owner_org_id = None
        self._client_key_type = None
        self._client_key_bitlength = None
        self._client_key_ttl = None
        self.discriminator = None

        self.id = id
        self.symmetric_key_use_domains = symmetric_key_use_domains
        self.symmetric_key_use_domain_selector_scheme = symmetric_key_use_domain_selector_scheme
        self.owner_org_id = owner_org_id
        self.client_key_type = client_key_type
        self.client_key_bitlength = client_key_bitlength
        self.client_key_ttl = client_key_ttl

    @property
    def id(self):
        """Gets the id of this CryptoConfig.  # noqa: E501


        :return: The id of this CryptoConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CryptoConfig.


        :param id: The id of this CryptoConfig.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def symmetric_key_use_domains(self):
        """Gets the symmetric_key_use_domains of this CryptoConfig.  # noqa: E501

        every application layer encryption must select a key to use from one specific active semmetric key encryption domain. this is an array of encryption domains id's that are currently available for encryption  # noqa: E501

        :return: The symmetric_key_use_domains of this CryptoConfig.  # noqa: E501
        :rtype: list[SymmetricKeyUseDomain]
        """
        return self._symmetric_key_use_domains

    @symmetric_key_use_domains.setter
    def symmetric_key_use_domains(self, symmetric_key_use_domains):
        """Sets the symmetric_key_use_domains of this CryptoConfig.

        every application layer encryption must select a key to use from one specific active semmetric key encryption domain. this is an array of encryption domains id's that are currently available for encryption  # noqa: E501

        :param symmetric_key_use_domains: The symmetric_key_use_domains of this CryptoConfig.  # noqa: E501
        :type: list[SymmetricKeyUseDomain]
        """
        if symmetric_key_use_domains is None:
            raise ValueError("Invalid value for `symmetric_key_use_domains`, must not be `None`")  # noqa: E501

        self._symmetric_key_use_domains = symmetric_key_use_domains

    @property
    def symmetric_key_use_domain_selector_scheme(self):
        """Gets the symmetric_key_use_domain_selector_scheme of this CryptoConfig.  # noqa: E501

        to guide SDK's on how to select an encryption domain, a selectorScheme helps an SDK map a encryption request to a set of keys and encryption algoritm  # noqa: E501

        :return: The symmetric_key_use_domain_selector_scheme of this CryptoConfig.  # noqa: E501
        :rtype: str
        """
        return self._symmetric_key_use_domain_selector_scheme

    @symmetric_key_use_domain_selector_scheme.setter
    def symmetric_key_use_domain_selector_scheme(self, symmetric_key_use_domain_selector_scheme):
        """Sets the symmetric_key_use_domain_selector_scheme of this CryptoConfig.

        to guide SDK's on how to select an encryption domain, a selectorScheme helps an SDK map a encryption request to a set of keys and encryption algoritm  # noqa: E501

        :param symmetric_key_use_domain_selector_scheme: The symmetric_key_use_domain_selector_scheme of this CryptoConfig.  # noqa: E501
        :type: str
        """
        if symmetric_key_use_domain_selector_scheme is None:
            raise ValueError("Invalid value for `symmetric_key_use_domain_selector_scheme`, must not be `None`")  # noqa: E501

        self._symmetric_key_use_domain_selector_scheme = symmetric_key_use_domain_selector_scheme

    @property
    def owner_org_id(self):
        """Gets the owner_org_id of this CryptoConfig.  # noqa: E501

        the org id of the organization that owns these symmetric keys  # noqa: E501

        :return: The owner_org_id of this CryptoConfig.  # noqa: E501
        :rtype: str
        """
        return self._owner_org_id

    @owner_org_id.setter
    def owner_org_id(self, owner_org_id):
        """Sets the owner_org_id of this CryptoConfig.

        the org id of the organization that owns these symmetric keys  # noqa: E501

        :param owner_org_id: The owner_org_id of this CryptoConfig.  # noqa: E501
        :type: str
        """
        if owner_org_id is None:
            raise ValueError("Invalid value for `owner_org_id`, must not be `None`")  # noqa: E501

        self._owner_org_id = owner_org_id

    @property
    def client_key_type(self):
        """Gets the client_key_type of this CryptoConfig.  # noqa: E501

        the type of key that should be associated with clients, for example, rsa  # noqa: E501

        :return: The client_key_type of this CryptoConfig.  # noqa: E501
        :rtype: str
        """
        return self._client_key_type

    @client_key_type.setter
    def client_key_type(self, client_key_type):
        """Sets the client_key_type of this CryptoConfig.

        the type of key that should be associated with clients, for example, rsa  # noqa: E501

        :param client_key_type: The client_key_type of this CryptoConfig.  # noqa: E501
        :type: str
        """
        if client_key_type is None:
            raise ValueError("Invalid value for `client_key_type`, must not be `None`")  # noqa: E501

        self._client_key_type = client_key_type

    @property
    def client_key_bitlength(self):
        """Gets the client_key_bitlength of this CryptoConfig.  # noqa: E501

        the bit length of all new client keys, for example, 2048  # noqa: E501

        :return: The client_key_bitlength of this CryptoConfig.  # noqa: E501
        :rtype: int
        """
        return self._client_key_bitlength

    @client_key_bitlength.setter
    def client_key_bitlength(self, client_key_bitlength):
        """Sets the client_key_bitlength of this CryptoConfig.

        the bit length of all new client keys, for example, 2048  # noqa: E501

        :param client_key_bitlength: The client_key_bitlength of this CryptoConfig.  # noqa: E501
        :type: int
        """
        if client_key_bitlength is None:
            raise ValueError("Invalid value for `client_key_bitlength`, must not be `None`")  # noqa: E501

        self._client_key_bitlength = client_key_bitlength

    @property
    def client_key_ttl(self):
        """Gets the client_key_ttl of this CryptoConfig.  # noqa: E501

        the TTL on the client's local asymetric key  # noqa: E501

        :return: The client_key_ttl of this CryptoConfig.  # noqa: E501
        :rtype: int
        """
        return self._client_key_ttl

    @client_key_ttl.setter
    def client_key_ttl(self, client_key_ttl):
        """Sets the client_key_ttl of this CryptoConfig.

        the TTL on the client's local asymetric key  # noqa: E501

        :param client_key_ttl: The client_key_ttl of this CryptoConfig.  # noqa: E501
        :type: int
        """
        if client_key_ttl is None:
            raise ValueError("Invalid value for `client_key_ttl`, must not be `None`")  # noqa: E501

        self._client_key_ttl = client_key_ttl

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
        if issubclass(CryptoConfig, dict):
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
        if not isinstance(other, CryptoConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other