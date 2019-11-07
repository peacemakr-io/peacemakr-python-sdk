from peacemakr_sdk.crypto_base import PeacemakrCryptoSDK


class CryptoImpl(PeacemakrCryptoSDK):

    def __init__(self, api_key=""):
        self.api_key = api_key
        

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
        print("In decrypt")
        pass
