from peacemakr_sdk.generated.api_client import ApiClient
from peacemakr_sdk.generated.api.client_api import ClientApi
from peacemakr_sdk.generated.api.crypto_config_api import CryptoConfigApi
from peacemakr_sdk.generated.api.org_api import OrgApi
from peacemakr_sdk.generated.api.key_service_api import KeyServiceApi

from peacemakr_sdk.generated.models.client import Client
from peacemakr_sdk.generated.configuration import Configuration
from peacemakr_sdk.generated.models import *

from peacemakr_sdk.generated.rest import ApiException
from peacemakr_sdk.crypto_base import PeacemakrCryptoSDK
from peacemakr_sdk.impl.persister_impl import InMemoryPersister
import peacemakr_core_crypto_python as p

import time
import json
import base64

PYTHON_SDK_VERSION = "0.0.1"
PERSISTER_PRIV_KEY = "Priv"
PERSISTER_PUB_KEY = "Pub"
PERSISTER_ASYM_TYPE = "AsymmetricKeyType"
PERSISTER_ASYM_CREATED_DATE_EPOCH = "AsymmetricKeyCreated"
PERSISTER_ASYM_BITLEN = "AsymmetricKeyBitlen"
PERSISTER_CLIENTID_KEY = "ClientId"
PERSISTER_PREFERRED_KEYID = "PreferredKeyId"
PERSISTER_APIKEY_KEY = "ApiKey"

DEFAULT_SYMM_CIPHER = p.SymmetricCipher.CHACHA20_POLY1305

class CryptoImpl(PeacemakrCryptoSDK):
    def __init__(self, api_key="", client_name="", peacemakr_hostname="", persister=None, logger=None):
        '''
            This is the CryptoSDK constructor.
            Public Attributes are:
                api_key: str: api key accessible from admin portal
                client_name: str: the clients name
                sdk_version: str: version number of the current SDK
                peacemakr_hostname: str: the SDK hostname
                org: obj: the organization's information
                crypto_config: obj: the current local crypto configuration
                persister: obj: the persister
                logger: obj: the logger API
                client: obj: the client API

            Private Attributes are:
                api_cient:
                authentication:
                loaded_private_preferred_key:
                loaded_private_preferred_cipher:
        '''
        self.api_key = api_key
        self.client_name = client_name
        self.sdk_version = "0.0.1"
        self.peacemakr_hostname = peacemakr_hostname
        self.org = None
        self.crypto_config = None
        self.persister = persister
        self.logger = logger

        # private vars
        self.__client = None
        self.__api_client = None
        self.__authentication = None
        self.__loaded_private_preferred_key = None
        self.__loaded_private_preferred_cipher = None

    # Register, Boostrap
    def __is_registered(self):
        ## TODO: save things to persister
        return  self.persister.exists(PERSISTER_PREFERRED_KEYID)\
            and self.persister.exists(PERSISTER_CLIENTID_KEY)\
            and self.persister.exists(PERSISTER_PRIV_KEY)\
            and self.persister.exists(PERSISTER_PUB_KEY)\
            and self.persister.exists(PERSISTER_ASYM_TYPE)

    def __is_bootstrapped(self):
        return self.org != None and self.crypto_config != None and self.__client != None

    def __do_bootstrap_org_and_crypto_config(self):
        # set up org, api_client, and crypto_config
        if self.__is_bootstrapped():
            return

        api_client = self.__get_client()

        self.__load_org(api_client)
        self.__load_crypto_config(api_client)
    
    def __load_org(self, api_client):
        # TODO: add exception
        org_api = OrgApi(api_client=api_client)
        self.org = org_api.get_organization_from_api_key(apikey=self.api_key)

    def __load_crypto_config(self, api_client):
        # TODO: add exception
        crypto_config_api = CryptoConfigApi(api_client=api_client)
        self.crypto_config = crypto_config_api.get_crypto_config(self.org.crypto_config_id)

    def __get_client(self):
        ''' set up api client
        '''
        if self.__api_client != None:
            return self.__api_client

        if self.api_key == "":
            # raise Exception
            return None

        configuration = Configuration()
        configuration.api_key['authorization'] = self.api_key
        configuration.host = self.peacemakr_hostname + "/api/v1"
        self.__api_client = ApiClient(configuration=configuration)

        # persister save api key

        return self.__api_client

    # Key Related functions
    def __gen_new_asymmetric_keypair(self, persister):
        rand = p.RandomDevice()

        symm_cipher = DEFAULT_SYMM_CIPHER
        asymm_cipher = self.__get_asymmetric_cipher(self.crypto_config.client_key_type, self.crypto_config.client_key_bitlength)

        key = p.Key(asymm_cipher, symm_cipher, rand)

        pub_pem = key.get_pub_pem()
        priv_pem = key.get_priv_pem()

        created_time = int(round(time.time()))
        pub_key = PublicKey(id="",
                            key=pub_pem,
                            creation_time=created_time,
                            key_type=self.crypto_config.client_key_type,
                            encoding="pem")

        persister.save(PERSISTER_PRIV_KEY, priv_pem)
        persister.save(PERSISTER_PUB_KEY, pub_pem)
        persister.save(PERSISTER_ASYM_TYPE, self.crypto_config.client_key_type)
        persister.save(PERSISTER_ASYM_CREATED_DATE_EPOCH, created_time)
        persister.save(PERSISTER_ASYM_BITLEN, self.crypto_config.client_key_bitlength)

        return pub_key

    def __get_asymmetric_cipher(self, key_type, bit_length):
        prefix_dict = {
            "ec" : "ECDH_P",
            "rsa": "RSA_"
        }

        asymm_dict = {
            "RSA_2048": p.AsymmetricCipher.RSA_2048,
            "RSA_4096": p.AsymmetricCipher.RSA_4096,
            "ECDH_P256": p.AsymmetricCipher.ECDH_P256,
            "ECDH_P384": p.AsymmetricCipher.ECDH_P384,
            "ECDH_P521": p.AsymmetricCipher.ECDH_P521,
        }

        prefix = prefix_dict[key_type.lower()]
        asymm_key = '{}{}'.format(prefix, bit_length)

        return asymm_dict[asymm_key]


    def __verify_bootstrapped_and_registered(self):
        # FIXME: the exception needs to be peacemakr specific
        if not self.__is_registered() or not self.__is_bootstrapped():
            raise Exception("SDK was not registered, please register before using other SDK operations.")


    def __save_new_asymmetric_key_pair(self, src, dst):
        dst.save(PERSISTER_PRIV_KEY, src.load(PERSISTER_PRIV_KEY))
        dst.save(PERSISTER_PUB_KEY, src.load(PERSISTER_PUB_KEY))
        dst.save(PERSISTER_ASYM_TYPE, src.load(PERSISTER_ASYM_TYPE))
        dst.save(PERSISTER_ASYM_CREATED_DATE_EPOCH, src.load(PERSISTER_ASYM_CREATED_DATE_EPOCH))
        dst.save(PERSISTER_ASYM_BITLEN, src.load(PERSISTER_ASYM_BITLEN))

    def __gen_and_register_new_preferred_client_key(self):
        print("Generating a new preferred client key")
        temp_in_memory_persister: InMemoryPersister = InMemoryPersister()
        public_key = self.__gen_new_asymmetric_keypair(temp_in_memory_persister)

        print("Registering the new public key")
        client_api = ClientApi(self.__get_client())
        try:
            public_key = client_api.add_client_public_key(self.__client.id, public_key)
        except ApiException as e:
            print(e)
            pass

        print("Successfully registered new public key as client preferred key")
        self.__save_new_asymmetric_key_pair(temp_in_memory_persister, self.persister)
        self.persister.save(PERSISTER_PREFERRED_KEYID, public_key.id)

        print("Successfully saved new public key as client preferred key")

    def __update_local_crypto_config(self, new_config):
        cur_asymmetric_key_type = self.persister.load(PERSISTER_ASYM_TYPE)
        if not new_config.client_key_type == cur_asymmetric_key_type:
            #FIXME: add logger
            self.crypto_config = new_config
            self.__gen_and_register_new_preferred_client_key()
            return

        cur_asymmetric_key_creation_time = self.persister.load(PERSISTER_ASYM_CREATED_DATE_EPOCH)
        asymmetric_key_creation_time = cur_asymmetric_key_creation_time
        if (new_config.client_key_ttl + asymmetric_key_creation_time) > int(round(time.time())):
            #FFIXME: add logger
            self.crypto_config = new_config
            self.__gen_and_register_new_preferred_client_key()
            return

        cur_asymmetric_key_bit_lens = self.persister.load(PERSISTER_ASYM_BITLEN)
        asymmertric_key_bit_len = int(cur_asymmetric_key_bit_lens)
        if asymmertric_key_bit_len != new_config.client_key_bitlength:
            #FIXME: add logger
            self.crypto_config = new_config
            self.__gen_and_register_new_preferred_client_key()
            return

        self.crypto_config = new_config

    def __download_and_save_all_keys(self, required_keys=[]):
        ''' calls keyServiceApi to get all the encrypted keys just generated from the key deriver
        '''

        key_api = KeyServiceApi(api_client=self.__get_client())
        all_keys = key_api.get_all_encrypted_keys(self.__client.preferred_public_key_id, symmetric_key_ids=required_keys)

        if len(all_keys) == 0:
            # add logger
            print("No encrypted symmetric keys to be decrypted")

        self.__decrypt_and_save(all_keys)
        #self.persister.debug()


    def __decrypt_and_save(self, all_keys):
        ''' decryptes the encrypted symmetric keys and save them to persister
        '''

        if (self.__loaded_private_preferred_key == None):
            self.__loaded_private_preferred_cipher = self.__get_asymmetric_cipher(self.persister.load(PERSISTER_ASYM_TYPE), self.persister.load(PERSISTER_ASYM_BITLEN))
            self.__loaded_private_preferred_key = p.Key(DEFAULT_SYMM_CIPHER, self.persister.load(PERSISTER_PRIV_KEY), True)

        context = p.CryptoContext()
        for key in all_keys:
            if key == None:
                continue

            raw_cipher_text_str = key.packaged_ciphertext
            if raw_cipher_text_str == None:
                print("Error: raw cipher text is None")


            # deserialized[0] is a pycapule object that decrypt takes in, deseralized[1] is the config
            deserialized = context.deserialize(raw_cipher_text_str)

            extracted_aad = context.extract_unverified_aad(raw_cipher_text_str)
            # check if extracted aad is null
            if extracted_aad == "":
                # raise exception
                print("Extracted aad is empty")

            aad = json.loads(extracted_aad.aad)

            verification_key = self.__get_or_download_public_key(aad["senderKeyID"])

            if self.__is_ec(self.__loaded_private_preferred_cipher):
                # print("In EC")
                # verfication is the peer key and client key is "my_key"
                ehcd_key = p.Key(DEFAULT_SYMM_CIPHER, self.__loaded_private_preferred_key, verification_key)
                result = context.decrypt(ehcd_key, deserialized[0])
            elif self.__is_rsa(self.__loaded_private_preferred_cipher):
                # print("In RSA")
                result = context.decrypt(self.__loaded_private_preferred_key, deserialized[0])
            else:
                # raise exception
                print("KEY SELECT NOT IDENTIFIED, SOMETHING IS WRONG")

            # data is the plaintext, result = [plainText, NeedVerify:bool]; plainText = {data, aad}
            need_verfication = result[1]
            # check verfication
            if need_verfication:
                verfied = context.verify(verification_key, result[0], deserialized[0])
                if verfied == False:
                    # raise verficationException?
                    print("Error Verfication Failed")

            keys_in_str = result[0].data

            key_len = key.key_length
            keys_in_bytes = base64.decodebytes(keys_in_str.encode())
            for i in range(len(key.key_ids)):
                # loop thru each key id and save their respective keys
                key_in_bytes = keys_in_bytes[i*key_len:(i+1)*key_len]
                self.persister.save(key.key_ids[i], key_in_bytes)

    def __is_ec(self, cipher):
        if cipher in {p.AsymmetricCipher.ECDH_P256, p.AsymmetricCipher.ECDH_P384, p.AsymmetricCipher.ECDH_P521}:
            return True
        return False

    def __is_rsa(self, cipher):
        if cipher in {p.AsymmetricCipher.RSA_2048, p.AsymmetricCipher.RSA_4096}:
            return True
        return False

    def __get_or_download_public_key(self, key_id):
        if (self.persister.exists(key_id)):
            return self.persister.load(key_id)

        key_service_api = KeyServiceApi(self.__get_client())

        # TODO:add try, except
        # try
        pub_key = key_service_api.get_public_key(key_id)
        # except

        self.persister.save(key_id, pub_key.key)

        # constructor for AsymmetricKey:(SYM_CIPHER, pub_key:str, pri_key=True/False)
        pub_pem = p.Key(DEFAULT_SYMM_CIPHER, pub_key.key, False)

        return pub_pem


    def register(self):
        # check is register and is boostrap, if not initialize
        try:
            self.__verify_bootstrapped_and_registered()
        except Exception as e:
            self.__do_bootstrap_org_and_crypto_config()

        # generate new asymmetric client keypair and then store info in persistor
        pub_key = self.__gen_new_asymmetric_keypair(self.persister)

        # generate new client with empty id and client public key
        client = Client(id = "", public_keys=[pub_key], sdk=self.sdk_version)

        client_api = ClientApi(api_client=self.__get_client())

        # try:
        new_client = client_api.add_client(client)
        #except someException

        self.__client = new_client

        self.persister.save(PERSISTER_CLIENTID_KEY, self.__client.id)
        self.persister.save(PERSISTER_PREFERRED_KEYID, self.__client.public_keys[0].id)

        # self.persister.debug() # prints all info in the persister


    def sync(self):
        self.__verify_bootstrapped_and_registered()
        crypto_config_api = CryptoConfigApi(self.__get_client())

        try:
            new_config = crypto_config_api.get_crypto_config(self.crypto_config.id)
            if new_config != self.crypto_config:
                self.__update_local_crypto_config(new_config)
        except ApiException as e:
            #FIXME: create server exception
            raise ServerException(e)

        self.__download_and_save_all_keys()

    def encrypt(self, plain_text: bytes) -> bytes:
        print("In encrypt")
        pass


    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        print("In encrypt in domain")
        pass


    def decrypt(self, cipher_text: bytes) -> bytes:
        print("In decrypt")
        pass

    def check_registered(self):
        return self.__is_registered() and self.__is_bootstrapped()

    def check_synced(self):
        return self.check_registered() and self.__loaded_private_preferred_key != None
