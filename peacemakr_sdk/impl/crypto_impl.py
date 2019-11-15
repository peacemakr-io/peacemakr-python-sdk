from peacemakr_sdk.crypto_base import PeacemakrCryptoSDK

from peacemakr_sdk.impl.models.cipher_text_aad import CiphertextAAD

import json

class CryptoImpl(PeacemakrCryptoSDK):

    def __init__(self, api_key=""):
        self.api_key = api_key


    def __parse_cipher_text_AAD(self, aad: str):
        return CiphertextAAD(**json.loads(aad))


    def register(self):
        print("In register")
        pass


    def sync(self):
        print("In sync")
        pass


    def encrypt(self, plain_text: bytes) -> bytes:
        print("In encrypt")
        pass


    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        print("In encrypt in domain")
        pass


    def decrypt(self, cipher_text: bytes) -> bytes:
        # FIXME: not sure what's the use case for serialize deserialize in core crypto
        # FIXME: uncomment code when the functions are implemented (in other PRs)

        # self.__verify_bootstrapped_and_registered()
        aad = self.__parse_cipher_text_AAD(p.CryptoContext().extract_unverified_aad(cipher_text).aad)
        key = None
        try:
            # key = self.__get_key(aad.cryptoKeyID)
            pass
        except Exception as e:
            # FIXME: Above should not be Exception but something explicit
            # raise PersistenceLayerCorruptionDetected(e)
            pass

        # verificationKey = self.__get_or_download_public_key()
        # return p.CryptoContext().decrypt(key, verificationKey, cipher_text)
