# -*- coding: utf-8 -*-
"""Example Module docstrings.
This module ...
Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::
        $ python example_google.py
Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.
Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.
        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.
"""

from abc import ABC, abstractmethod

class PeacemakrCryptoSDK(ABC):

    @abstractmethod
    def register(self):
        """Registers to Peacemakr as a client.

        The persister is used to detect prior registrations on this client, so safe
        to call multiple times. Once a successful invocation of Register is executed once, subsequent calls become a
        noop. One successful call is required before any cryptographic use of this SDK.

        Registration may fail with invalid apiKey, missing network connectivity, or an invalid persister. On failure,
        take corrections action and invoke again.

        Raises:
            AttributeError: TODO to be modified later.
            ValueError: ...

        """
        pass


    @abstractmethod
    def sync(self):
        """Sync all available keys for this client.

        This invocation will help performance of subsequent encryption and decryption calls.

        Sync may fail, if registration was not invoked, if there's network connectivity issues, or
        unexpected authorization issues.

        Raises:
            AttributeError: TODO to be modified later.
            ValueError: ...

        """
        pass


    @abstractmethod
    def encrypt(self, plain_text: bytes) -> bytes:
        """Encrypt the plaintext, using a random available usedomain.

        Args:
            plain_text (bytes): Plaintext bytes to encrypt.

        Returns:
            bytes: Opaquely packaged ciphertext.

        Raises:
            AttributeError: TODO to be modified later.
            ValueError: ...

        """
        pass


    @abstractmethod
    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        """
        Encrypt the plaintext, but restrict which keys may be used to a Use Domain of this specific name. Names of Use
        Domains are not unique, and this non-unique property of your Organization's Use Domains allows for graceful
        rotation of encryption keys off of old (retiring, stale, or compromised) Use Domains, simply by creating a new
        Use Domain with the same name. The transitional purity, both Use Domains may be selected for encryption use by
        clients restricted to one particular name. Then, retiring of one of the two Use Domains is possible without
        disrupting your deployed application.

        Args:
            plain_text (bytes): Plaintext to encrypt.
            use_domain_name (str): Non-unique User Domain of your organization's.

        Returns:
            bytes: Opaquely packaged ciphertext.

        Raises:
            AttributeError: TODO to be modified later.
            ValueError: ...

        """
        pass


    @abstractmethod
    def decrypt(self, cipher_text: bytes) -> bytes:
        """
        Decrypt the opaquely packaged ciphertext and return the original plain text.

        Args:
            cipher_text (bytes): CipherText to decrypt.

        Returns:
            bytes: decrypted plaintext in bytes

        Raises:
            AttributeError: TODO to be modified later.
            ValueError: ...

        """
        pass
