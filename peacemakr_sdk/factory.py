from peacemakr_sdk.impl.crypto_impl import CryptoImpl



class Factory:
    def __init__(self):
        pass

    def get_crypto_sdk(self, api_key="", client_name="", peacemakr_hostname="", persister=None, logger=None):
        return CryptoImpl(api_key=api_key, client_name=client_name, peacemakr_hostname=peacemakr_hostname, persister=persister)