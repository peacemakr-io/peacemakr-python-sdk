from random import randint
from time import time

from peacemakr_sdk.crypto_base import PeacemakrCryptoSDK
from peacemakr_sdk.generated import SymmetricKeyUseDomain


# TODO : Check if this is doing it's job for picking random index in the list.
def random_index(l: list):
    return l[randint(0, len(l) - 1)]


class CryptoImpl(PeacemakrCryptoSDK):

    def __init__(self, api_key=""):
        self.api_key = api_key

    def register(self):
        print("In register")
        pass

    def sync(self):
        print("In sync")
        pass

    # TODO : Fix type hinting for domain.
    def __domain_is_valid_for_encryption(self, domain: SymmetricKeyUseDomain) -> bool:
        # TODO : Test the time with the java time to make sure everything is ok.
        now_in_seconds = int(round(time() * 1000))
        return domain.creation_time + domain.symmetric_key_decryption_use_ttl > now_in_seconds \
               and domain.creation_time + domain.symmetric_key_inception_ttl <= now_in_seconds

    def __select_use_domain_name(self) -> str:
        valid_for_encryption = []
        for domain in self.crypto_config.symmetric_key_use_domains:
            if self.__domain_is_valid_for_encryption(domain):
                valid_for_encryption.append(domain)
        if not valid_for_encryption:
            return None
        return random_index(valid_for_encryption)

    def __get_valid_use_domain_for_encryption(self, use_domain_name: str) -> SymmetricKeyUseDomain:
        use_domains = self.crypto_config.symmetric_key_use_domains
        valid_domain_with_this_name = []

        # TODO : Handle logger call.

        for domain in use_domains:
            if domain.name != use_domain_name:
                continue
            if not self.__domain_is_valid_for_encryption(domain):
                continue
            if not domain.encryption_key_ids:
                continue
            valid_domain_with_this_name.append(domain)

        # TODO : Handle custom exceptions.
        if not valid_domain_with_this_name:
            raise Exception("No valid use domain for encryption found, with the name " + use_domain_name)

        return random_index(valid_domain_with_this_name)

    def __get_encryption_key_id(self, use_domain: SymmetricKeyUseDomain) -> str:
        return random_index(use_domain.encryption_key_ids)

    def __get_key(self, key_id: str) -> bytes:

    def encrypt(self, plain_text: bytes) -> bytes:
        print("In encrypt")
        # TODO: Check if call is correct.
        assert self.__verify_bootstrapped_and_registered
        self.__verify_bootstrapped_and_registered()
        used_domain_name = self.__select_use_domain_name()
        return self.encrypt_in_domain(plain_text, used_domain_name)

    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        print("In encrypt in domain")
        self.__verify_bootstrapped_and_registered()
        use_domain_for_encryption = self.__get_valid_use_domain_for_encryption(use_domain_name)
        encryption_key_id_for_encryption = self.__get_encryption_key_id(use_domain_for_encryption)

        key = None
        try:
            key = self.__get_key(encryption_key_id_for_encryption)

    def decrypt(self, cipher_text: bytes) -> bytes:
        print("In decrypt")
        pass
