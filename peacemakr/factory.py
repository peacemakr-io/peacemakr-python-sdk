from peacemakr.impl.crypto_impl import CryptoImpl

def get_crypto_sdk(api_key="", client_name="", peacemakr_hostname="", persister=None, logger=None):
  return CryptoImpl(api_key=api_key, client_name=client_name, peacemakr_hostname=peacemakr_hostname, persister=persister, logger=logger)
