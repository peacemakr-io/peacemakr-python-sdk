from peacemakr_sdk.impl.crypto_impl import CryptoImpl



class Factory:
    def __init__(self):
        pass

    def get_crypto_sdk(self):
        return CryptoImpl()