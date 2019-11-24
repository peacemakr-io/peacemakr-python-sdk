from peacemakr_sdk.crypto_base import PeacemakrCryptoSDK

from peacemakr_sdk.impl.models.cipher_text_aad import CiphertextAAD

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
from random import randint
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

def random_index(l: list):
    return l[randint(0, len(l) - 1)]

class CryptoImpl(PeacemakrCryptoSDK):
    def __init__(self, api_key="", client_name="", peacemakr_hostname="", persister=None, logger=None):
        self.api_key = api_key
        self.client_name = client_name
        self.sdk_version = "0.0.1"
        self.peacemakr_hostname = peacemakr_hostname
        self.org = None
        self.crypto_config = None
        self.persister = persister
        self.logger = logger

        self.__client = None
        self.__api_client = None
        self.__authentication = None
        self.__loaded_private_preferred_key = None
        self.__loaded_private_preferred_cipher = None
        self.__crypto_context = p.CryptoContext()

        self.__Chacha20Poly1305 = "CHACHA20_POLY1305"
        self.__Aes128gcm = "AES-128-GCM"
        self.__Aes192gcm = "AES-192-GCM"
        self.__Aes256gcm = "AES-256-GCM"

        self.__Sha224 = "SHA_224"
        self.__Sha256 = "SHA_256"
        self.__Sha384 = "SHA_384"
        self.__Sha512 = "SHA_512"

    def __is_registered(self) -> bool:
        ## TODO: save things to persister
        return  self.persister.exists(PERSISTER_PREFERRED_KEYID)\
            and self.persister.exists(PERSISTER_CLIENTID_KEY)\
            and self.persister.exists(PERSISTER_PRIV_KEY)\
            and self.persister.exists(PERSISTER_PUB_KEY)\
            and self.persister.exists(PERSISTER_ASYM_TYPE)

    def __is_bootstrapped(self) -> bool:
        return self.org != None and self.crypto_config != None and self.__client != None

    def __do_bootstrap_org_and_crypto_config(self):
        # set up org, api_client, and crypto_config
        if self.__is_bootstrapped():
            return

        api_client = self.__get_client()

        self.__load_org(api_client)
        self.__load_crypto_config(api_client)

    def __load_org(self, api_client: ApiClient):
        # TODO: add exception
        org_api = OrgApi(api_client=api_client)
        self.org = org_api.get_organization_from_api_key(apikey=self.api_key)

    def __load_crypto_config(self, api_client: ApiClient):
        # TODO: add exception
        crypto_config_api = CryptoConfigApi(api_client=api_client)
        self.crypto_config = crypto_config_api.get_crypto_config(self.org.crypto_config_id)

    def __get_client(self) -> ApiClient:
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
    def __gen_new_asymmetric_keypair(self, persister: InMemoryPersister) -> PublicKey:
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

    def __get_asymmetric_cipher(self, key_type: str, bit_length: int) -> p.AsymmetricCipher:
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
        if not self.__is_registered() or not self.__is_bootstrapped():
            raise Exception("SDK was not registered, please register before using other SDK operations.")


    def __save_new_asymmetric_key_pair(self, src: InMemoryPersister, dst: InMemoryPersister):
        dst.save(PERSISTER_PRIV_KEY, src.load(PERSISTER_PRIV_KEY))
        dst.save(PERSISTER_PUB_KEY, src.load(PERSISTER_PUB_KEY))
        dst.save(PERSISTER_ASYM_TYPE, src.load(PERSISTER_ASYM_TYPE))
        dst.save(PERSISTER_ASYM_CREATED_DATE_EPOCH, src.load(PERSISTER_ASYM_CREATED_DATE_EPOCH))
        dst.save(PERSISTER_ASYM_BITLEN, src.load(PERSISTER_ASYM_BITLEN))

    def __gen_and_register_new_preferred_client_key(self):
        temp_in_memory_persister: InMemoryPersister = InMemoryPersister()
        public_key = self.__gen_new_asymmetric_keypair(temp_in_memory_persister)

        client_api = ClientApi(self.__get_client())
        try:
            public_key = client_api.add_client_public_key(self.__client.id, public_key)
        except ApiException as e:
            pass

        self.__save_new_asymmetric_key_pair(temp_in_memory_persister, self.persister)
        self.persister.save(PERSISTER_PREFERRED_KEYID, public_key.id)


    def __update_local_crypto_config(self, new_config: p.CryptoConfig):

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

    def __download_and_save_all_keys(self, required_keys: list =[]):
        ''' calls keyServiceApi to get all the encrypted keys just generated from the key deriver
        '''
        key_api = KeyServiceApi(api_client=self.__get_client())
        all_keys = key_api.get_all_encrypted_keys(self.__client.preferred_public_key_id, symmetric_key_ids=required_keys)

        if len(all_keys) == 0:
            print('')
            # add logger

        self.__decrypt_and_save(all_keys)
        #self.persister.debug()


    def __decrypt_and_save(self, all_keys: list):
        ''' decryptes the encrypted symmetric keys and save them to persister
        '''
        if (self.__loaded_private_preferred_key == None):
            self.__loaded_private_preferred_cipher = self.__get_asymmetric_cipher(self.persister.load(PERSISTER_ASYM_TYPE), self.persister.load(PERSISTER_ASYM_BITLEN))
            self.__loaded_private_preferred_key = p.Key(DEFAULT_SYMM_CIPHER, self.persister.load(PERSISTER_PRIV_KEY), True)

        for key in all_keys:
            if key == None:
                continue

            raw_cipher_text_str = key.packaged_ciphertext
            if raw_cipher_text_str == None:
                print('')

            # deserialized[0] is a pycapule object that decrypt takes in, deseralized[1] is the config
            deserialized = self.__crypto_context.deserialize(raw_cipher_text_str)

            extracted_aad = self.__crypto_context.extract_unverified_aad(raw_cipher_text_str)
            # check if extracted aad is null
            if extracted_aad == "":
                print('')
                # raise exception

            aad = json.loads(extracted_aad.aad)

            verification_key = self.__get_or_download_public_key(aad["senderKeyID"])

            if self.__is_ec(self.__loaded_private_preferred_cipher):
                # verfication is the peer key and client key is "my_key"
                if isinstance(verification_key, str):
                    verification_key = p.Key(DEFAULT_SYMM_CIPHER, verification_key, False)

                ehcd_key = p.Key(DEFAULT_SYMM_CIPHER, self.__loaded_private_preferred_key, verification_key)
                result = self.__crypto_context.decrypt(ehcd_key, deserialized[0])
            elif self.__is_rsa(self.__loaded_private_preferred_cipher):
                result = self.__crypto_context.decrypt(self.__loaded_private_preferred_key, deserialized[0])
            else:
                raise Exception("Invalid asymetric cipher")

            # data is the plaintext, result = [plainText, NeedVerify:bool]; plainText = {data, aad}
            need_verfication = result[1]
            # check verfication
            if need_verfication:
                verfied = self.__crypto_context.verify(verification_key, result[0], deserialized[0])
                if verfied == False:
                    print('')
                    # raise verficationException?

            keys_in_str = result[0].data

            key_len = key.key_length
            keys_in_bytes = base64.decodebytes(keys_in_str.encode())
            for i in range(len(key.key_ids)):
                # loop thru each key id and save their respective keys
                key_in_bytes = keys_in_bytes[i*key_len:(i+1)*key_len]
                self.persister.save(key.key_ids[i], key_in_bytes)

    def __is_ec(self, cipher: p.AsymmetricCipher) -> bool:
        if cipher in {p.AsymmetricCipher.ECDH_P256, p.AsymmetricCipher.ECDH_P384, p.AsymmetricCipher.ECDH_P521}:
            return True
        return False

    def __is_rsa(self, cipher: p.AsymmetricCipher) -> bool:
        if cipher in {p.AsymmetricCipher.RSA_2048, p.AsymmetricCipher.RSA_4096}:
            return True
        return False

    def __get_or_download_public_key(self, key_id: str, cfg: p.CryptoConfig =None) -> p.Key:
        if (self.persister.exists(key_id)):
            return p.Key(p.SymmetricCipher(cfg.symm_cipher), self.persister.load(key_id), False)
        else:
            return p.Key(DEFAULT_SYMM_CIPHER, self.persister.load(key_id), False)

        key_service_api = KeyServiceApi(self.__get_client())

        try
            pub_key = key_service_api.get_public_key(key_id)
        except Exception as e:
            raise e

        self.persister.save(key_id, pub_key.key)

        if not cfg:
            return  p.Key(DEFAULT_SYMM_CIPHER, pub_key.key, False)
        else:
            return p.Key(p.SymmetricCipher(cfg.symm_cipher), pub_key.key, False)


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

        try:
            new_client = client_api.add_client(client)
        except Exception as e:
            raise e

        self.__client = new_client

        self.persister.save(PERSISTER_CLIENTID_KEY, self.__client.id)
        self.persister.save(PERSISTER_PREFERRED_KEYID, self.__client.public_keys[0].id)


    def sync(self):
        self.__verify_bootstrapped_and_registered()
        crypto_config_api = CryptoConfigApi(self.__get_client())

        try:
            new_config = crypto_config_api.get_crypto_config(self.crypto_config.id)
            if new_config != self.crypto_config:
                self.__update_local_crypto_config(new_config)
        except ApiException as e:
            raise ServerException(e)

        self.__download_and_save_all_keys()

    def __domain_is_valid_for_encryption(self, domain: SymmetricKeyUseDomain) -> bool:
        now_in_seconds = int(round(time.time()))
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

        if not valid_domain_with_this_name:
            raise Exception("No valid use domain for encryption found, with the name " + use_domain_name)

        return random_index(valid_domain_with_this_name)

    def __get_encryption_key_id(self, use_domain: SymmetricKeyUseDomain) -> str:
        return random_index(use_domain.encryption_key_ids)

    def __get_key(self, key_id: str) -> bytes:
        if self.persister.exists(key_id):
            return self.persister.load(key_id)

        self.__download_and_save_all_keys([key_id])

        # TODO : Handle persister missing keys exception.
        return self.persister.load(key_id)


    def __get_symmetric_cipher(self, symmetric_key_encryption_alg: str) -> p.SymmetricCipher:
        select_cipher = {
            self.__Chacha20Poly1305: p.SymmetricCipher.CHACHA20_POLY1305,
            self.__Aes128gcm: p.SymmetricCipher.AES_128_GCM,
            self.__Aes192gcm: p.SymmetricCipher.AES_192_GCM,
            self.__Aes256gcm: p.SymmetricCipher.AES_256_GCM,
        }
        return select_cipher[symmetric_key_encryption_alg]

    def __get_signing_key(self, use_domain: SymmetricKeyUseDomain) -> p.Key:
        if use_domain.digest_algorithm is None:
            return None

        if self.__loaded_private_preferred_key != None:
            return self.__loaded_private_preferred_key

        private_pem = self.persister.load(PERSISTER_PRIV_KEY)
        self.__loaded_private_preferred_key = p.Key(DEFAULT_SYMM_CIPHER, private_pem)
        self.__loaded_private_preferred_cipher = self.__get_asymmetric_cipher(self.persister.load(PERSISTER_ASYM_TYPE), int(self.persister.load(PERSISTER_ASYM_BITLEN)))

        return self.__loaded_private_preferred_key

    def __get_digest_alg(self, digest_algorithm: str) -> p.DigestAlgorithm:
        if digest_algorithm == self.__Sha224:
            return p.DigestAlgorithm.SHA_224
        elif digest_algorithm == self.__Sha256:
            return p.DigestAlgorithm.SHA_256
        elif digest_algorithm == self.__Sha384:
            return p.DigestAlgorithm.SHA_384
        elif digest_algorithm == self.__Sha512:
            return p.DigestAlgorithm.SHA_512
        else:
            # TODO : Handle logger.
            return DEFAULT_MESSAGE_DIGEST

    def encrypt(self, plain_text: bytes) -> bytes:
        # TODO: Check if function exists.
        assert self.__verify_bootstrapped_and_registered, "Missing implementation for __verify_bootstrapped_and_registered"
        self.__verify_bootstrapped_and_registered()
        used_domain_name = self.__select_use_domain_name()
        return self.encrypt_in_domain(plain_text, used_domain_name.name)

    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        self.__verify_bootstrapped_and_registered()
        use_domain_for_encryption = self.__get_valid_use_domain_for_encryption(use_domain_name)
        encryption_key_id_for_encryption = self.__get_encryption_key_id(use_domain_for_encryption)

        symmetric_cipher = self.__get_symmetric_cipher(use_domain_for_encryption.symmetric_key_encryption_alg)
        signing_key = self.__get_signing_key(use_domain_for_encryption)
        digest = self.__get_digest_alg(use_domain_for_encryption.digest_algorithm)

        key = None
        try:
            key = p.Key(symmetric_cipher, self.__get_key(encryption_key_id_for_encryption))
        except Exception as e:
            raise e

        aad = CiphertextAAD(encryption_key_id_for_encryption, self.persister.load(PERSISTER_PREFERRED_KEYID))
        json_bytes = bytes(json.dumps(aad.__dict__), encoding='utf8')
        pm_plain_text = p.Plaintext(plain_text, base64.b64encode(json_bytes))
        random_device = p.RandomDevice()

        cipher_text = self.__crypto_context.encrypt(key, pm_plain_text, random_device)
        try:
            self.__crypto_context.sign(signing_key, pm_plain_text, digest, cipher_text)
        except Exception as e:
            raise e

        return self.__crypto_context.serialize(digest, cipher_text)


    def __parse_cipher_text_AAD(self, aad: str) -> CiphertextAAD:
        j = json.loads(base64.b64decode(aad))
        return CiphertextAAD(**j)

    def __verify_message(self, aad: CiphertextAAD, cfg: p.CryptoConfig, ciphertext, plaintext: p.Plaintext) -> bool:
        sender_key = self.__get_or_download_public_key(aad.senderKeyID, cfg)
        return self.__crypto_context.verify(sender_key, plaintext, ciphertext)

    def __find_viable_decryption_use_domains(self) -> list:
        use_domains = self.crypto_config.symmetric_key_use_domains
        viable_domains = [domain for domain in use_domains if domain.symmetric_key_decryption_allowed]
        return viable_domains

    def __is_key_id_decryption_viable(self, key_id: str) -> bool:
        viable_decryption_domains = self.__find_viable_decryption_use_domains()
        for domain in viable_decryption_domains:
            if key_id in domain.encryption_key_ids:
                return True
        return False

    def decrypt(self, cipher_text: bytes) -> bytes:
        self.__verify_bootstrapped_and_registered()

        cipher_text_blob, cfg = self.__crypto_context.deserialize(cipher_text)
        aad = self.__crypto_context.extract_unverified_aad(cipher_text).aad
        aad = self.__parse_cipher_text_AAD(aad)
        if not self.__is_key_id_decryption_viable(aad.cryptoKeyID):
            raise Exception('Ciphertext is no longer viable for decryption')

        key = None
        try:
            key = self.__get_key(aad.cryptoKeyID)
        except Exception as e:
            raise e

        pmKey = p.Key(p.SymmetricCipher(cfg.symm_cipher), key)
        plain_text, need_verification = self.__crypto_context.decrypt(pmKey, cipher_text_blob)
        if need_verification:
            if not self.__verify_message(aad, cfg, cipher_text_blob, plain_text):
                raise Exception('Problem verifying')

        return plain_text.data.encode()
