from peacemakr_sdk.generated.api_client import ApiClient
from peacemakr_sdk.generated.api.client_api import ClientApi
from peacemakr_sdk.generated.api.crypto_config_api import CryptoConfigApi
from peacemakr_sdk.generated.api.org_api import OrgApi

from peacemakr_sdk.generated.models.client import Client
from peacemakr_sdk.generated.configuration import Configuration
from peacemakr_sdk.generated.models import *
from peacemakr_sdk.crypto_base import PeacemakrCryptoSDK
import peacemakr_core_crypto_python as p

import time

PERSISTER_PREFERRED_KEY_ID = ""
PERSISTER_CLIENTID_KEY = ""

DEFAULT_SYMM_CIPHER = p.SymmetricCipher.CHACHA20_POLY1305

class CryptoImpl(PeacemakrCryptoSDK):

    def __init__(self, api_key="", client_name="", peacemakr_hostname="", persister=None, logger=None):
        self.api_key = api_key
        self.client_name = client_name
        self.sdk_version = 0
        self.peacemakr_hostname = peacemakr_hostname
        self.org = None
        self.crypto_config = None
        self.persister = persister
        self.logger = logger

        # private vars
        self._client = None
        self._api_client = None
        self._authentication = None
        self._loaded_private_preferred_key = None
        self._loaded_private_preferred_cipher = None

    # Register, Boostrap
    def _is_registered(self):
        ## TODO: save things to persister
        return False

    def _is_boostrapped(self):
        return self.org != None and self.crypto_config != None and self._client != None

    def _do_boostrap_org_and_crypto_config(self):
        # set up org, api_client, and crypto_config
        if self._is_boostrapped():
            return

        api_client = self._get_client()
        
        self._load_org(api_client)
        self._load_crypto_config(api_client)

    def _load_org(self, api_client):
        # TODO: add exception
        org_api = OrgApi(api_client=api_client)

        self.org = org_api.get_organization_from_api_key(apikey=self.api_key)
        print(self.org)
           
    def _load_crypto_config(self, api_client):
        # TODO: add exception
        crypto_config_api = CryptoConfigApi(api_client=api_client)
        self.crypto_config = crypto_config_api.get_crypto_config(self.org.crypto_config_id)

    def _get_client(self):
        ''' set up api client
        '''
        if self._api_client != None:
            return self._api_client
        
        if self.api_key == "":
            # raise Exception
            return None 

        configuration = Configuration()
        configuration.api_key['authorization'] = self.api_key
        configuration.host = self.peacemakr_hostname + "/api/v1"
        self._api_client = ApiClient(configuration=configuration)
        
        # persister save api key

        return self._api_client

    # Key Related functions
    def _gen_new_asymmetric_keypair(self, persister):
        rand = p.RandomDevice()

        symm_cipher = DEFAULT_SYMM_CIPHER
        asymm_cipher = self._get_asymmetric_cipher(self.crypto_config.client_key_type, self.crypto_config.client_key_bitlength)

        key = p.Key(asymm_cipher, symm_cipher, rand)

        pub_pem = key.get_pub_pem()

        pub_key = PublicKey(id="", key=pub_pem, creation_time=int(round(time.time())), key_type=self.crypto_config.client_key_type, encoding="pem")

        return pub_key

    def _get_asymmetric_cipher(self, key_type, bit_length):
        prefix_dict = {
            "ec" : "ECDH_P",
            "rsa": "RSA_"
        }

        asymm_dict = {
            "RSA_2048": p.AsymmetricCipher.RSA_2048,
            "RSA_4096": p.AsymmetricCipher.RSA_4096,
            "ECDH_P256": p.AsymmetricCipher.ECDH_P256,
            "ECDH_P384": p.AsymmetricCipher.ECDH_P384,
            "ECDH_P512": p.AsymmetricCipher.ECDH_P521,
        }

        prefix = prefix_dict[key_type]
        asymm_key = '{}{}'.format(prefix, bit_length)

        return asymm_dict[asymm_key]
        


    def register(self):

        # check is register and is boostrap, if not initialize
        if self._is_registered():
            if not self._is_boostrapped:
                self._do_boostrap_org_and_crypto_config()
            return
        

        self._do_boostrap_org_and_crypto_config()
        # generate new asymmetric client keypair and then store info in persistor
        pub_key = self._gen_new_asymmetric_keypair(self.persister)

        # generate new client with empty id and client public key
        client = Client(id = "", public_keys=[pub_key])

        client_api = ClientApi(api_client=self._get_client())

        # try:
        new_client = client_api.add_client(client)
        #except someException

        self._client = new_client

        # save info in persister

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