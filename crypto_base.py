from abc import ABC, abstractmethod


class AbstractCryptoClass(ABC):

    '''
    Regsiter to Peacemakr as client
    '''
    @abstractmethod
    def register(self):
        pass

    '''
    Sync all avaliable keys for this clients
    '''
    @abstractmethod
    def sync(self):
        pass

    '''
    Encrypt the plaintext, using a random available usedomain
    '''
    @abstractmethod
    def encrypt(self, plain_text: bytes) -> bytes:
        pass

    '''
    Encrypt the plaintext using specified domain.
    '''
    @abstractmethod
    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        pass

    '''
    Decrypt the ciphertext and return original plaintext
    '''
    @abstractmethod
    def decrypt(self, cipher_text: bytes) -> bytes:
        pass