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


class SymmetricKeyUseDomain(object):
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
        'owner_org_id': 'str',
        'name': 'str',
        'creation_time': 'int',
        'symmetric_key_inception_ttl': 'int',
        'symmetric_key_encryption_use_ttl': 'int',
        'symmetric_key_encryption_allowed': 'bool',
        'symmetric_key_decryption_use_ttl': 'int',
        'symmetric_key_decryption_allowed': 'bool',
        'symmetric_key_retention_use_ttl': 'int',
        'symmetric_key_length': 'int',
        'symmetric_key_encryption_alg': 'str',
        'encrypting_packaged_ciphertext_version': 'int',
        'symmetric_key_derivation_service_id': 'str',
        'encryption_key_ids': 'list[str]',
        'endable_kds_fallback_to_cloud': 'bool',
        'require_signed_key_delivery': 'bool',
        'digest_algorithm': 'str'
    }

    attribute_map = {
        'id': 'id',
        'owner_org_id': 'ownerOrgId',
        'name': 'name',
        'creation_time': 'creationTime',
        'symmetric_key_inception_ttl': 'symmetricKeyInceptionTTL',
        'symmetric_key_encryption_use_ttl': 'symmetricKeyEncryptionUseTTL',
        'symmetric_key_encryption_allowed': 'symmetricKeyEncryptionAllowed',
        'symmetric_key_decryption_use_ttl': 'symmetricKeyDecryptionUseTTL',
        'symmetric_key_decryption_allowed': 'symmetricKeyDecryptionAllowed',
        'symmetric_key_retention_use_ttl': 'symmetricKeyRetentionUseTTL',
        'symmetric_key_length': 'symmetricKeyLength',
        'symmetric_key_encryption_alg': 'symmetricKeyEncryptionAlg',
        'encrypting_packaged_ciphertext_version': 'encryptingPackagedCiphertextVersion',
        'symmetric_key_derivation_service_id': 'symmetricKeyDerivationServiceId',
        'encryption_key_ids': 'encryptionKeyIds',
        'endable_kds_fallback_to_cloud': 'endableKDSFallbackToCloud',
        'require_signed_key_delivery': 'requireSignedKeyDelivery',
        'digest_algorithm': 'digestAlgorithm'
    }

    def __init__(self, id=None, owner_org_id=None, name=None, creation_time=None, symmetric_key_inception_ttl=None, symmetric_key_encryption_use_ttl=None, symmetric_key_encryption_allowed=None, symmetric_key_decryption_use_ttl=None, symmetric_key_decryption_allowed=None, symmetric_key_retention_use_ttl=None, symmetric_key_length=None, symmetric_key_encryption_alg='CHACHA20_POLY1305', encrypting_packaged_ciphertext_version=None, symmetric_key_derivation_service_id=None, encryption_key_ids=None, endable_kds_fallback_to_cloud=None, require_signed_key_delivery=None, digest_algorithm='SHA_256'):  # noqa: E501
        """SymmetricKeyUseDomain - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._owner_org_id = None
        self._name = None
        self._creation_time = None
        self._symmetric_key_inception_ttl = None
        self._symmetric_key_encryption_use_ttl = None
        self._symmetric_key_encryption_allowed = None
        self._symmetric_key_decryption_use_ttl = None
        self._symmetric_key_decryption_allowed = None
        self._symmetric_key_retention_use_ttl = None
        self._symmetric_key_length = None
        self._symmetric_key_encryption_alg = None
        self._encrypting_packaged_ciphertext_version = None
        self._symmetric_key_derivation_service_id = None
        self._encryption_key_ids = None
        self._endable_kds_fallback_to_cloud = None
        self._require_signed_key_delivery = None
        self._digest_algorithm = None
        self.discriminator = None

        self.id = id
        self.owner_org_id = owner_org_id
        if name is not None:
            self.name = name
        self.creation_time = creation_time
        self.symmetric_key_inception_ttl = symmetric_key_inception_ttl
        self.symmetric_key_encryption_use_ttl = symmetric_key_encryption_use_ttl
        if symmetric_key_encryption_allowed is not None:
            self.symmetric_key_encryption_allowed = symmetric_key_encryption_allowed
        self.symmetric_key_decryption_use_ttl = symmetric_key_decryption_use_ttl
        if symmetric_key_decryption_allowed is not None:
            self.symmetric_key_decryption_allowed = symmetric_key_decryption_allowed
        self.symmetric_key_retention_use_ttl = symmetric_key_retention_use_ttl
        self.symmetric_key_length = symmetric_key_length
        self.symmetric_key_encryption_alg = symmetric_key_encryption_alg
        self.encrypting_packaged_ciphertext_version = encrypting_packaged_ciphertext_version
        self.symmetric_key_derivation_service_id = symmetric_key_derivation_service_id
        self.encryption_key_ids = encryption_key_ids
        self.endable_kds_fallback_to_cloud = endable_kds_fallback_to_cloud
        self.require_signed_key_delivery = require_signed_key_delivery
        if digest_algorithm is not None:
            self.digest_algorithm = digest_algorithm

    @property
    def id(self):
        """Gets the id of this SymmetricKeyUseDomain.  # noqa: E501


        :return: The id of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SymmetricKeyUseDomain.


        :param id: The id of this SymmetricKeyUseDomain.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def owner_org_id(self):
        """Gets the owner_org_id of this SymmetricKeyUseDomain.  # noqa: E501

        the org id of the organization that owns these symmetric keys  # noqa: E501

        :return: The owner_org_id of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: str
        """
        return self._owner_org_id

    @owner_org_id.setter
    def owner_org_id(self, owner_org_id):
        """Sets the owner_org_id of this SymmetricKeyUseDomain.

        the org id of the organization that owns these symmetric keys  # noqa: E501

        :param owner_org_id: The owner_org_id of this SymmetricKeyUseDomain.  # noqa: E501
        :type: str
        """
        if owner_org_id is None:
            raise ValueError("Invalid value for `owner_org_id`, must not be `None`")  # noqa: E501

        self._owner_org_id = owner_org_id

    @property
    def name(self):
        """Gets the name of this SymmetricKeyUseDomain.  # noqa: E501


        :return: The name of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SymmetricKeyUseDomain.


        :param name: The name of this SymmetricKeyUseDomain.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def creation_time(self):
        """Gets the creation_time of this SymmetricKeyUseDomain.  # noqa: E501


        :return: The creation_time of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SymmetricKeyUseDomain.


        :param creation_time: The creation_time of this SymmetricKeyUseDomain.  # noqa: E501
        :type: int
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def symmetric_key_inception_ttl(self):
        """Gets the symmetric_key_inception_ttl of this SymmetricKeyUseDomain.  # noqa: E501

        number of seconds since key creation that the key will be available for encryption  # noqa: E501

        :return: The symmetric_key_inception_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: int
        """
        return self._symmetric_key_inception_ttl

    @symmetric_key_inception_ttl.setter
    def symmetric_key_inception_ttl(self, symmetric_key_inception_ttl):
        """Sets the symmetric_key_inception_ttl of this SymmetricKeyUseDomain.

        number of seconds since key creation that the key will be available for encryption  # noqa: E501

        :param symmetric_key_inception_ttl: The symmetric_key_inception_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :type: int
        """
        if symmetric_key_inception_ttl is None:
            raise ValueError("Invalid value for `symmetric_key_inception_ttl`, must not be `None`")  # noqa: E501

        self._symmetric_key_inception_ttl = symmetric_key_inception_ttl

    @property
    def symmetric_key_encryption_use_ttl(self):
        """Gets the symmetric_key_encryption_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501

        number of seconds since key creation that the key will be available for encryption  # noqa: E501

        :return: The symmetric_key_encryption_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: int
        """
        return self._symmetric_key_encryption_use_ttl

    @symmetric_key_encryption_use_ttl.setter
    def symmetric_key_encryption_use_ttl(self, symmetric_key_encryption_use_ttl):
        """Sets the symmetric_key_encryption_use_ttl of this SymmetricKeyUseDomain.

        number of seconds since key creation that the key will be available for encryption  # noqa: E501

        :param symmetric_key_encryption_use_ttl: The symmetric_key_encryption_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :type: int
        """
        if symmetric_key_encryption_use_ttl is None:
            raise ValueError("Invalid value for `symmetric_key_encryption_use_ttl`, must not be `None`")  # noqa: E501

        self._symmetric_key_encryption_use_ttl = symmetric_key_encryption_use_ttl

    @property
    def symmetric_key_encryption_allowed(self):
        """Gets the symmetric_key_encryption_allowed of this SymmetricKeyUseDomain.  # noqa: E501

        whether this use domain is available for encryption; if false, these keys should not be used for encrypting new messages  # noqa: E501

        :return: The symmetric_key_encryption_allowed of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: bool
        """
        return self._symmetric_key_encryption_allowed

    @symmetric_key_encryption_allowed.setter
    def symmetric_key_encryption_allowed(self, symmetric_key_encryption_allowed):
        """Sets the symmetric_key_encryption_allowed of this SymmetricKeyUseDomain.

        whether this use domain is available for encryption; if false, these keys should not be used for encrypting new messages  # noqa: E501

        :param symmetric_key_encryption_allowed: The symmetric_key_encryption_allowed of this SymmetricKeyUseDomain.  # noqa: E501
        :type: bool
        """

        self._symmetric_key_encryption_allowed = symmetric_key_encryption_allowed

    @property
    def symmetric_key_decryption_use_ttl(self):
        """Gets the symmetric_key_decryption_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501

        number of seconds since key creation that the key will be available for decryption  # noqa: E501

        :return: The symmetric_key_decryption_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: int
        """
        return self._symmetric_key_decryption_use_ttl

    @symmetric_key_decryption_use_ttl.setter
    def symmetric_key_decryption_use_ttl(self, symmetric_key_decryption_use_ttl):
        """Sets the symmetric_key_decryption_use_ttl of this SymmetricKeyUseDomain.

        number of seconds since key creation that the key will be available for decryption  # noqa: E501

        :param symmetric_key_decryption_use_ttl: The symmetric_key_decryption_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :type: int
        """
        if symmetric_key_decryption_use_ttl is None:
            raise ValueError("Invalid value for `symmetric_key_decryption_use_ttl`, must not be `None`")  # noqa: E501

        self._symmetric_key_decryption_use_ttl = symmetric_key_decryption_use_ttl

    @property
    def symmetric_key_decryption_allowed(self):
        """Gets the symmetric_key_decryption_allowed of this SymmetricKeyUseDomain.  # noqa: E501

        whether this use domain is available for decryption; if false, these keys should not be used for decrypting messages  # noqa: E501

        :return: The symmetric_key_decryption_allowed of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: bool
        """
        return self._symmetric_key_decryption_allowed

    @symmetric_key_decryption_allowed.setter
    def symmetric_key_decryption_allowed(self, symmetric_key_decryption_allowed):
        """Sets the symmetric_key_decryption_allowed of this SymmetricKeyUseDomain.

        whether this use domain is available for decryption; if false, these keys should not be used for decrypting messages  # noqa: E501

        :param symmetric_key_decryption_allowed: The symmetric_key_decryption_allowed of this SymmetricKeyUseDomain.  # noqa: E501
        :type: bool
        """

        self._symmetric_key_decryption_allowed = symmetric_key_decryption_allowed

    @property
    def symmetric_key_retention_use_ttl(self):
        """Gets the symmetric_key_retention_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501

        number of seconds since key creation that the key will be available for retention purposes  # noqa: E501

        :return: The symmetric_key_retention_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: int
        """
        return self._symmetric_key_retention_use_ttl

    @symmetric_key_retention_use_ttl.setter
    def symmetric_key_retention_use_ttl(self, symmetric_key_retention_use_ttl):
        """Sets the symmetric_key_retention_use_ttl of this SymmetricKeyUseDomain.

        number of seconds since key creation that the key will be available for retention purposes  # noqa: E501

        :param symmetric_key_retention_use_ttl: The symmetric_key_retention_use_ttl of this SymmetricKeyUseDomain.  # noqa: E501
        :type: int
        """
        if symmetric_key_retention_use_ttl is None:
            raise ValueError("Invalid value for `symmetric_key_retention_use_ttl`, must not be `None`")  # noqa: E501

        self._symmetric_key_retention_use_ttl = symmetric_key_retention_use_ttl

    @property
    def symmetric_key_length(self):
        """Gets the symmetric_key_length of this SymmetricKeyUseDomain.  # noqa: E501

        the number of bits of all symmetric keys in this use domain  # noqa: E501

        :return: The symmetric_key_length of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: int
        """
        return self._symmetric_key_length

    @symmetric_key_length.setter
    def symmetric_key_length(self, symmetric_key_length):
        """Sets the symmetric_key_length of this SymmetricKeyUseDomain.

        the number of bits of all symmetric keys in this use domain  # noqa: E501

        :param symmetric_key_length: The symmetric_key_length of this SymmetricKeyUseDomain.  # noqa: E501
        :type: int
        """
        if symmetric_key_length is None:
            raise ValueError("Invalid value for `symmetric_key_length`, must not be `None`")  # noqa: E501

        self._symmetric_key_length = symmetric_key_length

    @property
    def symmetric_key_encryption_alg(self):
        """Gets the symmetric_key_encryption_alg of this SymmetricKeyUseDomain.  # noqa: E501

        the specific encryption alg to encrypt new plaintexts for application layer encryption operations  # noqa: E501

        :return: The symmetric_key_encryption_alg of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: str
        """
        return self._symmetric_key_encryption_alg

    @symmetric_key_encryption_alg.setter
    def symmetric_key_encryption_alg(self, symmetric_key_encryption_alg):
        """Sets the symmetric_key_encryption_alg of this SymmetricKeyUseDomain.

        the specific encryption alg to encrypt new plaintexts for application layer encryption operations  # noqa: E501

        :param symmetric_key_encryption_alg: The symmetric_key_encryption_alg of this SymmetricKeyUseDomain.  # noqa: E501
        :type: str
        """
        if symmetric_key_encryption_alg is None:
            raise ValueError("Invalid value for `symmetric_key_encryption_alg`, must not be `None`")  # noqa: E501

        self._symmetric_key_encryption_alg = symmetric_key_encryption_alg

    @property
    def encrypting_packaged_ciphertext_version(self):
        """Gets the encrypting_packaged_ciphertext_version of this SymmetricKeyUseDomain.  # noqa: E501

        after encrypting new plaintexts, package the ciphertext with this version of the packaged ciphertext  # noqa: E501

        :return: The encrypting_packaged_ciphertext_version of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: int
        """
        return self._encrypting_packaged_ciphertext_version

    @encrypting_packaged_ciphertext_version.setter
    def encrypting_packaged_ciphertext_version(self, encrypting_packaged_ciphertext_version):
        """Sets the encrypting_packaged_ciphertext_version of this SymmetricKeyUseDomain.

        after encrypting new plaintexts, package the ciphertext with this version of the packaged ciphertext  # noqa: E501

        :param encrypting_packaged_ciphertext_version: The encrypting_packaged_ciphertext_version of this SymmetricKeyUseDomain.  # noqa: E501
        :type: int
        """
        if encrypting_packaged_ciphertext_version is None:
            raise ValueError("Invalid value for `encrypting_packaged_ciphertext_version`, must not be `None`")  # noqa: E501

        self._encrypting_packaged_ciphertext_version = encrypting_packaged_ciphertext_version

    @property
    def symmetric_key_derivation_service_id(self):
        """Gets the symmetric_key_derivation_service_id of this SymmetricKeyUseDomain.  # noqa: E501

        the symmetric key derivation serivce id that can derive and wrap these keys  # noqa: E501

        :return: The symmetric_key_derivation_service_id of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: str
        """
        return self._symmetric_key_derivation_service_id

    @symmetric_key_derivation_service_id.setter
    def symmetric_key_derivation_service_id(self, symmetric_key_derivation_service_id):
        """Sets the symmetric_key_derivation_service_id of this SymmetricKeyUseDomain.

        the symmetric key derivation serivce id that can derive and wrap these keys  # noqa: E501

        :param symmetric_key_derivation_service_id: The symmetric_key_derivation_service_id of this SymmetricKeyUseDomain.  # noqa: E501
        :type: str
        """
        if symmetric_key_derivation_service_id is None:
            raise ValueError("Invalid value for `symmetric_key_derivation_service_id`, must not be `None`")  # noqa: E501

        self._symmetric_key_derivation_service_id = symmetric_key_derivation_service_id

    @property
    def encryption_key_ids(self):
        """Gets the encryption_key_ids of this SymmetricKeyUseDomain.  # noqa: E501

        these are the semmetric key id's that belong to this use domain - these keys never belong to any other use domain  # noqa: E501

        :return: The encryption_key_ids of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: list[str]
        """
        return self._encryption_key_ids

    @encryption_key_ids.setter
    def encryption_key_ids(self, encryption_key_ids):
        """Sets the encryption_key_ids of this SymmetricKeyUseDomain.

        these are the semmetric key id's that belong to this use domain - these keys never belong to any other use domain  # noqa: E501

        :param encryption_key_ids: The encryption_key_ids of this SymmetricKeyUseDomain.  # noqa: E501
        :type: list[str]
        """
        if encryption_key_ids is None:
            raise ValueError("Invalid value for `encryption_key_ids`, must not be `None`")  # noqa: E501

        self._encryption_key_ids = encryption_key_ids

    @property
    def endable_kds_fallback_to_cloud(self):
        """Gets the endable_kds_fallback_to_cloud of this SymmetricKeyUseDomain.  # noqa: E501

        if all registered kds service become unreachable, then incoming requests for new and existing keys may fallback to the cloud provided KDS  # noqa: E501

        :return: The endable_kds_fallback_to_cloud of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: bool
        """
        return self._endable_kds_fallback_to_cloud

    @endable_kds_fallback_to_cloud.setter
    def endable_kds_fallback_to_cloud(self, endable_kds_fallback_to_cloud):
        """Sets the endable_kds_fallback_to_cloud of this SymmetricKeyUseDomain.

        if all registered kds service become unreachable, then incoming requests for new and existing keys may fallback to the cloud provided KDS  # noqa: E501

        :param endable_kds_fallback_to_cloud: The endable_kds_fallback_to_cloud of this SymmetricKeyUseDomain.  # noqa: E501
        :type: bool
        """
        if endable_kds_fallback_to_cloud is None:
            raise ValueError("Invalid value for `endable_kds_fallback_to_cloud`, must not be `None`")  # noqa: E501

        self._endable_kds_fallback_to_cloud = endable_kds_fallback_to_cloud

    @property
    def require_signed_key_delivery(self):
        """Gets the require_signed_key_delivery of this SymmetricKeyUseDomain.  # noqa: E501

        if required, all clients must receive these keys in a signed symmetric key delivery from the key deriver  # noqa: E501

        :return: The require_signed_key_delivery of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: bool
        """
        return self._require_signed_key_delivery

    @require_signed_key_delivery.setter
    def require_signed_key_delivery(self, require_signed_key_delivery):
        """Sets the require_signed_key_delivery of this SymmetricKeyUseDomain.

        if required, all clients must receive these keys in a signed symmetric key delivery from the key deriver  # noqa: E501

        :param require_signed_key_delivery: The require_signed_key_delivery of this SymmetricKeyUseDomain.  # noqa: E501
        :type: bool
        """
        if require_signed_key_delivery is None:
            raise ValueError("Invalid value for `require_signed_key_delivery`, must not be `None`")  # noqa: E501

        self._require_signed_key_delivery = require_signed_key_delivery

    @property
    def digest_algorithm(self):
        """Gets the digest_algorithm of this SymmetricKeyUseDomain.  # noqa: E501

        The digest algorithm to use for signing messages in this use domain  # noqa: E501

        :return: The digest_algorithm of this SymmetricKeyUseDomain.  # noqa: E501
        :rtype: str
        """
        return self._digest_algorithm

    @digest_algorithm.setter
    def digest_algorithm(self, digest_algorithm):
        """Sets the digest_algorithm of this SymmetricKeyUseDomain.

        The digest algorithm to use for signing messages in this use domain  # noqa: E501

        :param digest_algorithm: The digest_algorithm of this SymmetricKeyUseDomain.  # noqa: E501
        :type: str
        """

        self._digest_algorithm = digest_algorithm

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
        if issubclass(SymmetricKeyUseDomain, dict):
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
        if not isinstance(other, SymmetricKeyUseDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other