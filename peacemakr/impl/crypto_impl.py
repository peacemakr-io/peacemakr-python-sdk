from peacemakr.crypto_base import PeacemakrCryptoSDK

from peacemakr.impl.models.cipher_text_aad import CiphertextAAD

from peacemakr.generated.api_client import ApiClient
from peacemakr.generated.api.client_api import ClientApi
from peacemakr.generated.api.crypto_config_api import CryptoConfigApi
from peacemakr.generated.api.org_api import OrgApi
from peacemakr.generated.api.key_service_api import KeyServiceApi

from peacemakr.generated.models.client import Client
from peacemakr.generated.configuration import Configuration
from peacemakr.generated.models import *
from peacemakr.generated.rest import ApiException

from peacemakr.exception.core_crypto import CoreCryptoError
from peacemakr.exception.failed_to_download_key import FailedToDownloadKeyError
from peacemakr.exception.invalid_cipher import InvalidCipherError
from peacemakr.exception.missing_api_key import MissingAPIKeyError
from peacemakr.exception.missing_client_name import MissingClientNameError
from peacemakr.exception.missing_persister import MissingPersisterError
from peacemakr.exception.no_valid_use_domains_for_encryption import NoValidUseDomainsForEncryptionError
from peacemakr.exception.no_valid_use_domains_for_decryption import NoValidUseDomainsForDecryptionError
from peacemakr.exception.peacemakr import PeacemakrError
from peacemakr.exception.persistence_layer_corruption_detected import PersistenceLayerCorruptionDetectedError
from peacemakr.exception.server import ServerError
from peacemakr.exception.unrecoverable_clock_skew_detected import UnrecoverableClockSkewDetectedError

from peacemakr.crypto_base import PeacemakrCryptoSDK
from peacemakr.impl.persister_impl import InMemoryPersister
from peacemakr.persister_base import Persister
import peacemakr_core_crypto_python as p

from random import randint
from functools import reduce
import logging
import time
import json
import base64
import sys

PERSISTER_PRIV_KEY = "Priv"
PERSISTER_PUB_KEY = "Pub"
PERSISTER_ASYM_TYPE = "AsymmetricKeyType"
PERSISTER_ASYM_CREATED_DATE_EPOCH = "AsymmetricKeyCreated"
PERSISTER_ASYM_BITLEN = "AsymmetricKeyBitlen"
PERSISTER_CLIENTID_KEY = "ClientId"
PERSISTER_PREFERRED_KEYID = "PreferredKeyId"
PERSISTER_APIKEY_KEY = "ApiKey"

DEFAULT_SYMM_CIPHER = p.SymmetricCipher.CHACHA20_POLY1305
DEFAULT_MESSAGE_DIGEST = p.DigestAlgorithm.SHA_256
MAX_ELASPED_TIME = 60 * 60 * 24

def random_index(l: list):
    assert isinstance(l, list) and len(l)
    return l[randint(0, len(l) - 1)]

class CryptoImpl(PeacemakrCryptoSDK):
    def __init__(self, api_key="", client_name="", peacemakr_hostname="", persister=None, logger=None):
        assert isinstance(api_key, str)
        assert isinstance(client_name, str)
        assert isinstance(peacemakr_hostname, str)
        assert logger is None or isinstance(logger, logging.Logger)
        if not client_name:
            raise MissingClientNameError("A client name is required")
        if not api_key:
            raise MissingAPIKeyError("An API key is required")
        if not persister or not isinstance(persister, Persister):
            raise MissingPersisterError("A persister is required")

        self.api_key = api_key
        self.client_name = client_name
        self.sdk_version = "0.0.1"
        self.peacemakr_hostname = peacemakr_hostname
        self.org = None
        self.crypto_config = None
        self.persister = persister
        self.logger = logger or logging.getLogger("default_logger")
        logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.__client = None
        self.__api_client = None
        self.__authentication = None
        self.__loaded_private_preferred_key = None
        self.__loaded_private_preferred_cipher = None
        self.__crypto_context = p.CryptoContext()

        self.__last_updated_time = None
        self.__sym_key_cache = dict()

    def __bootsrapped_private_preferred_key_and_cipher(self):
        self.__loaded_private_preferred_cipher = self.__get_asymmetric_cipher(self.persister.load(PERSISTER_ASYM_TYPE), self.persister.load(PERSISTER_ASYM_BITLEN))
        self.__loaded_private_preferred_key = p.Key(DEFAULT_SYMM_CIPHER, self.persister.load(PERSISTER_PRIV_KEY), True)

    def __is_registered(self) -> bool:
        return  self.persister.exists(PERSISTER_PREFERRED_KEYID)\
            and self.persister.exists(PERSISTER_CLIENTID_KEY)\
            and self.persister.exists(PERSISTER_PRIV_KEY)\
            and self.persister.exists(PERSISTER_PUB_KEY)\
            and self.persister.exists(PERSISTER_ASYM_TYPE)\
            and self.__loaded_private_preferred_key != None\
            and self.__loaded_private_preferred_cipher != None

    def __is_bootstrapped(self) -> bool:
        return self.org != None and self.crypto_config != None and self.__client != None

    def __update_config_by_elasped_time(self, max_elasped_time: int = 60*60*24):
        ''' update the config if program elasped more than `max_elasped_time` since the last update
        '''
        now = time.time()
        if (now - self.__last_updated_time) > max_elasped_time:
            # add logger
            self.logger.info("Process elasped more than {} secs, updating config".format(max_elasped_time))
            self.sync()
            self.__last_updated_time = time.time()

    def __do_bootstrap_org_and_crypto_config(self):
        # set up org, api_client, and crypto_config
        if self.__is_bootstrapped():
            self.logger.info("client is bootstrapped already")
            return

        api_client = self.__get_client()

        self.__load_org(api_client)
        self.__load_crypto_config(api_client)

    def __load_org(self, api_client: ApiClient):
        assert isinstance(api_client, ApiClient)
        org_api = OrgApi(api_client=api_client)
        try:
            self.org = org_api.get_organization_from_api_key(apikey=self.api_key)
        except ApiException as e:
            self.logger.warning("Excpetion in getting organization from api key: {}".format(e))
            raise ServerError(e)

    def __load_crypto_config(self, api_client: ApiClient):
        assert isinstance(api_client, ApiClient)
        crypto_config_api = CryptoConfigApi(api_client=api_client)
        try:
            self.crypto_config = crypto_config_api.get_crypto_config(self.org.crypto_config_id)
        except ApiException as e:
            self.logger.warning("Exception in getting crypto config: {}".format(e))
            raise ServerError(e)



    def __get_client(self) -> ApiClient:
        if self.__api_client != None:
            return self.__api_client

        if self.api_key == "":
            self.logger.warning("Missing API Key")
            raise MissingAPIKeyError("Missing API Key")

        configuration = Configuration()
        configuration.api_key['authorization'] = self.api_key
        configuration.host = self.peacemakr_hostname + "/api/v1"
        self.__api_client = ApiClient(configuration=configuration)

        self.persister.save(PERSISTER_APIKEY_KEY, self.api_key)
        return self.__api_client

    def __gen_new_asymmetric_keypair(self, persister: Persister) -> PublicKey:
        assert isinstance(persister, Persister)
        rand = p.RandomDevice()

        symm_cipher = DEFAULT_SYMM_CIPHER
        asymm_cipher = self.__get_asymmetric_cipher(self.crypto_config.client_key_type, self.crypto_config.client_key_bitlength)

        key = p.Key(asymm_cipher, symm_cipher, rand)

        pub_pem = key.get_pub_pem()
        priv_pem = key.get_priv_pem()

        created_time = int(round(time.time()))
        if created_time > sys.maxsize:
            self.logger.error("Failed to detect a valid time for local asymmetric key creation time")
            raise UnrecoverableClockSkewDetectedError("Failed to detect a valid time for local asymmetric key creation time")

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
        assert isinstance(key_type, str)
        assert isinstance(bit_length, int)

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

        if asymm_key not in asymm_dict:
            self.logger.warning('{} is not currently supported by Peacemakr. Going to default ECDH_P521'.format(asymm_key))
            return p.AsymmetricCipher.ECDH_P521

        return asymm_dict[asymm_key]

    def __get_symmetric_cipher(self, symmetric_alg: str) -> p.SymmetricCipher:
        assert isinstance(symmetric_alg, str)
        select_cipher = {
            "CHACHA20_POLY1305": p.SymmetricCipher.CHACHA20_POLY1305,
            "AES-128-GCM": p.SymmetricCipher.AES_128_GCM,
            "AES-192-GCM": p.SymmetricCipher.AES_192_GCM,
            "AES-256-GCM": p.SymmetricCipher.AES_256_GCM,
        }
        if symmetric_alg not in select_cipher:
            self.logger.warning('{} is not currently supported by Peacemakr. Going to default {}'.format(symmetric_alg, DEFAULT_SYMM_CIPHER))
            return DEFAULT_SYMM_CIPHER

        return select_cipher[symmetric_alg]

    def __get_digest_alg(self, digest_algorithm: str) -> p.DigestAlgorithm:
        assert isinstance(digest_algorithm, str)
        select_digest = {
            "SHA_224" : p.DigestAlgorithm.SHA_224,
            "SHA_256" : p.DigestAlgorithm.SHA_256,
            "SHA_384" : p.DigestAlgorithm.SHA_384,
            "SHA_512" : p.DigestAlgorithm.SHA_512,
        }
        if digest_algorithm not in select_digest:
            self.logger.warning('{} is not currently supported by Peacemakr. Going to default {}'.format(digest_algorithm, DEFAULT_MESSAGE_DIGEST))
            return DEFAULT_MESSAGE_DIGEST

        return select_digest[digest_algorithm]

    def __verify_bootstrapped_and_registered(self):
        if not self.__is_registered() or not self.__is_bootstrapped():
            self.logger.warning("SDK was not registered, please register before using other SDK operations")
            raise PeacemakrError("SDK was not registered, please register before using other SDK operations")

    def __save_new_asymmetric_key_pair(self, src: Persister, dst: Persister):
        assert isinstance(src, Persister)
        assert isinstance(dst, Persister)
        dst.save(PERSISTER_PRIV_KEY, src.load(PERSISTER_PRIV_KEY))
        dst.save(PERSISTER_PUB_KEY, src.load(PERSISTER_PUB_KEY))
        dst.save(PERSISTER_ASYM_TYPE, src.load(PERSISTER_ASYM_TYPE))
        dst.save(PERSISTER_ASYM_CREATED_DATE_EPOCH, src.load(PERSISTER_ASYM_CREATED_DATE_EPOCH))
        dst.save(PERSISTER_ASYM_BITLEN, src.load(PERSISTER_ASYM_BITLEN))

    def __gen_and_register_new_preferred_client_key(self):
        temp_in_memory_persister = InMemoryPersister()
        public_key = self.__gen_new_asymmetric_keypair(temp_in_memory_persister)

        client_api = ClientApi(self.__get_client())
        try:
            public_key = client_api.add_client_public_key(self.__client.id, public_key)
        except ApiException as e:
            self.logger.warning("Exception in adding client public key: {}".format(e))
            raise ServerError(e)

        self.__save_new_asymmetric_key_pair(temp_in_memory_persister, self.persister)
        self.persister.save(PERSISTER_PREFERRED_KEYID, public_key.id)


    def __update_local_crypto_config(self, new_config: p.CryptoConfig):
        assert isinstance(new_config, p.CryptoConfig)
        cur_asymmetric_key_type = self.persister.load(PERSISTER_ASYM_TYPE)
        if cur_asymmetric_key_type != new_config.client_key_type:
            self.logger.info("update client asymmetric key type and crypto config from {} to {}".format(cur_asymmetric_key_type, new_config.client_key_type))
            self.crypto_config = new_config
            self.__gen_and_register_new_preferred_client_key()
            return

        cur_asymmetric_key_creation_time = self.persister.load(PERSISTER_ASYM_CREATED_DATE_EPOCH)
        asymmetric_key_creation_time = cur_asymmetric_key_creation_time
        if (new_config.client_key_ttl + asymmetric_key_creation_time) > int(round(time.time())):
            self.logger.info("client key expired, generating new client key")
            self.crypto_config = new_config
            self.__gen_and_register_new_preferred_client_key()
            return

        cur_asymmetric_key_bit_lens = self.persister.load(PERSISTER_ASYM_BITLEN)
        asymmertric_key_bit_len = int(cur_asymmetric_key_bit_lens)
        if asymmertric_key_bit_len != new_config.client_key_bitlength:
            self.logger.info("update client key length and crypto config from {} to {}".format(asymmertric_key_bit_len, new_config.client_key_bitlength))
            self.crypto_config = new_config
            self.__gen_and_register_new_preferred_client_key()
            return

        self.crypto_config = new_config

    def __download_and_save_all_keys(self, required_keys: list =[]):
        assert isinstance(required_keys, list)
        ''' calls keyServiceApi to get all the encrypted keys just generated from the key deriver
        '''
        key_api = KeyServiceApi(api_client=self.__get_client())
        try:
            all_keys = key_api.get_all_encrypted_keys(self.__client.preferred_public_key_id, symmetric_key_ids=required_keys)            
        except ApiException as e:
            self.logger.warning("Exception in getting all encrypted keys: {}".format(e))
            raise ServerError(e)

        self.__decrypt_and_save(all_keys)



    def __decrypt_and_save(self, all_keys: list):
        ''' decryptes the encrypted symmetric keys and save them to persister
        '''
        assert isinstance(all_keys, list)
        # loaded private preferred key should be loaded at boostrap
        if self.__loaded_private_preferred_key == None:
            self.logger.warning("SDK was not registered, please register before using other SDK operations")
            raise PeacemakrError("SDK was not registered, please register before using other SDK operations")

        for key in all_keys:
            if key == None:
                continue

            raw_cipher_text_str = key.packaged_ciphertext
            if raw_cipher_text_str == None:
                self.logger.info("Failed to get raw ciphertext str from EncryptedSymmetricKey")
                continue

            # deserialized[0] is a pycapsule object that decrypt takes in,
            # deseralized[1] is the config (sym cipher, asym cipher, digest algo, and mode)
            deserialized = self.__crypto_context.deserialize(raw_cipher_text_str)

            extracted_aad = self.__crypto_context.extract_unverified_aad(raw_cipher_text_str)
            # check if extracted aad is null
            if extracted_aad == "" or not extracted_aad:
                self.logger.warning("Failed to extrat aad from the ciphertext")
                raise CoreCryptoError("Failed to extract aad from the ciphertext")

            aad = json.loads(extracted_aad.aad)

            verification_key = self.__get_or_download_public_key(aad["senderKeyID"])

            if self.__is_ec(self.__loaded_private_preferred_cipher):
                # verfication is the peer key and client key is "my_key"
                if isinstance(verification_key, str):
                    verification_key = p.Key(DEFAULT_SYMM_CIPHER, verification_key, False)

                shared_symm_key = p.Key(DEFAULT_SYMM_CIPHER, self.__loaded_private_preferred_key, verification_key)
                result = self.__crypto_context.decrypt(shared_symm_key, deserialized[0])
            elif self.__is_rsa(self.__loaded_private_preferred_cipher):
                result = self.__crypto_context.decrypt(self.__loaded_private_preferred_key, deserialized[0])
            else:
                self.logger.warning("This version of python SDK only support ec or rsa. Invalid cipher.")
                raise InvalidCipherError("This version of python SDK only support ec or rsa. Invalid cipher.")

            # data is the plaintext, result = [plainText, NeedVerify:bool]; plainText = {data, aad}
            need_verfication = result[1]
            # check verfication
            if need_verfication:
                verified = self.__crypto_context.verify(verification_key, result[0], deserialized[0])
                if verified == False:
                    raise CoreCryptoError('Verification step failed')

            keys_in_str = result[0].data

            key_len = key.key_length
            keys_in_bytes = base64.decodebytes(keys_in_str)
            for i in range(len(key.key_ids)):
                # loop thru each key id and save their respective keys
                key_in_bytes = keys_in_bytes[i*key_len:(i+1)*key_len]
                self.__sym_key_cache[key.key_ids[i]] = key_in_bytes
                self.persister.save(key.key_ids[i], key_in_bytes)

    def __is_ec(self, cipher: p.AsymmetricCipher) -> bool:
        assert isinstance(cipher, p.AsymmetricCipher)
        if cipher in {p.AsymmetricCipher.ECDH_P256, p.AsymmetricCipher.ECDH_P384, p.AsymmetricCipher.ECDH_P521}:
            return True
        return False

    def __is_rsa(self, cipher: p.AsymmetricCipher) -> bool:
        assert isinstance(cipher, p.AsymmetricCipher)
        if cipher in {p.AsymmetricCipher.RSA_2048, p.AsymmetricCipher.RSA_4096}:
            return True
        return False

    def __get_or_download_public_key(self, key_id: str) -> p.Key:
        assert isinstance(key_id, str)
        #FIXME: should we really use default symm cipher all the time?
        if (self.persister.exists(key_id)):
            return p.Key(DEFAULT_SYMM_CIPHER, self.persister.load(key_id), False)

        key_service_api = KeyServiceApi(self.__get_client())

        try:
            pub_key = key_service_api.get_public_key(key_id)
        except ApiException as e:
            self.logger.warning("Exception in getting public key: {}".format(e))
            raise ServerError(e)

        self.persister.save(key_id, pub_key.key)

        return p.Key(DEFAULT_SYMM_CIPHER, pub_key.key, False)


    def register(self):
        # check is register and is boostrap, if not initialize
        if self.__is_registered():
            if not self.__is_bootstrapped():
                self.__do_bootstrap_org_and_crypto_config()
            self.logger.info("User is registered and boostrapped already")
            return

        self.__do_bootstrap_org_and_crypto_config()
        # generate new asymmetric client keypair and then store info in persistor
        pub_key = self.__gen_new_asymmetric_keypair(self.persister)

        # generate new client with empty id and client public key
        client = Client(id = "", public_keys=[pub_key], sdk=self.sdk_version)

        client_api = ClientApi(api_client=self.__get_client())

        try:
            new_client = client_api.add_client(client)
        except ApiException as e:
            self.logger.warning("Exception in getting all adding client: {}".format(e))
            raise ServerError(e)

        self.__client = new_client

        # FIXME: add client checks like in Java?
        self.__bootsrapped_private_preferred_key_and_cipher()
        self.persister.save(PERSISTER_CLIENTID_KEY, self.__client.id)
        self.persister.save(PERSISTER_PREFERRED_KEYID, self.__client.public_keys[0].id)
        self.__last_updated_time = time.time()


    def sync(self):
        self.__verify_bootstrapped_and_registered()
        crypto_config_api = CryptoConfigApi(self.__get_client())

        try:
            new_config = crypto_config_api.get_crypto_config(self.crypto_config.id)
            if new_config != self.crypto_config:
                self.__update_local_crypto_config(new_config)
        except ApiException as e:
            self.logger.warning("Exception in getting crypto config: {}".format(e))
            raise ServerError(e)

        self.__download_and_save_all_keys()

    def __domain_is_valid_for_encryption(self, domain: SymmetricKeyUseDomain) -> bool:
        assert isinstance(domain, SymmetricKeyUseDomain)
        now_in_seconds = int(round(time.time()))
        return domain.creation_time + domain.symmetric_key_encryption_use_ttl > now_in_seconds \
               and domain.creation_time + domain.symmetric_key_inception_ttl <= now_in_seconds

    def __select_use_domain_name(self) -> str:
        domains = self.crypto_config.symmetric_key_use_domains
        valid_for_encryption = [d for d in domains if self.__domain_is_valid_for_encryption(d)]
        return random_index(valid_for_encryption) if valid_for_encryption else None

    def __get_valid_use_domain_for_encryption(self, use_domain_name: str) -> SymmetricKeyUseDomain:
        assert isinstance(use_domain_name, str)
        domains = self.crypto_config.symmetric_key_use_domains
        # TODO : Handle logger call.
        domains = list(filter(lambda d: d.name == use_domain_name, domains))
        domains = [d for d in domains if self.__domain_is_valid_for_encryption(d) and d.encryption_key_ids]
        if not domains:
            raise NoValidUseDomainsForEncryptionError("No valid use domain for encryption found, with the name " + use_domain_name)

        return random_index(domains)

    def __get_encryption_key_id(self, use_domain: SymmetricKeyUseDomain) -> str:
        assert isinstance(use_domain, SymmetricKeyUseDomain)
        return random_index(use_domain.encryption_key_ids)

    def __get_key(self, key_id: str) -> bytes:
        assert isinstance(key_id, str)

        if key_id in self.__sym_key_cache:
            return self.__sym_key_cache[key_id]

        if self.persister.exists(key_id):
            return self.persister.load(key_id)

        self.__download_and_save_all_keys([key_id])
        if not self.persister.exists(key_id):
            raise FailedToDownloadKeyError('KeyID: {}'.format(key_id))
        # TODO : Handle persister missing keys exception.

        return self.persister.load(key_id)



    def __get_signing_key(self, use_domain: SymmetricKeyUseDomain) -> p.Key:
        assert isinstance(use_domain, SymmetricKeyUseDomain)
        if use_domain.digest_algorithm is None:
            return None

        if self.__loaded_private_preferred_key == None:
            self.logger.warning("SDK was not registered, please register before using other SDK operations")
            raise PeacemakrError("SDK was not registered, please register before using other SDK operations")

        return self.__loaded_private_preferred_key



    def encrypt(self, plain_text: bytes) -> bytes:
        assert isinstance(plain_text, bytes)

        self.__verify_bootstrapped_and_registered()
        self.__update_config_by_elasped_time(MAX_ELASPED_TIME)
        used_domain_name = self.__select_use_domain_name()
        return self.encrypt_in_domain(plain_text, used_domain_name.name)

    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        assert isinstance(plain_text, bytes)
        assert isinstance(use_domain_name, str)

        self.__verify_bootstrapped_and_registered()
        self.__update_config_by_elasped_time(MAX_ELASPED_TIME)
        use_domain_for_encryption = self.__get_valid_use_domain_for_encryption(use_domain_name)
        encryption_key_id_for_encryption = self.__get_encryption_key_id(use_domain_for_encryption)

        symmetric_cipher = self.__get_symmetric_cipher(use_domain_for_encryption.symmetric_key_encryption_alg)
        signing_key = self.__get_signing_key(use_domain_for_encryption)
        digest = self.__get_digest_alg(use_domain_for_encryption.digest_algorithm)

        key = p.Key(symmetric_cipher, self.__get_key(encryption_key_id_for_encryption))

        # FIXME persister preferred keyid can cause delay if persister read from disk
        aad = CiphertextAAD(encryption_key_id_for_encryption, self.persister.load(PERSISTER_PREFERRED_KEYID))
        json_bytes = bytes(json.dumps(aad.__dict__), encoding='utf8')

        pm_plain_text = p.Plaintext(plain_text, json_bytes)
        random_device = p.RandomDevice()

        cipher_text = self.__crypto_context.encrypt(key, pm_plain_text, random_device)

        if not self.__crypto_context.sign(signing_key, pm_plain_text, digest, cipher_text):
            self.logger.warning('Signing failed. Verification not required when decrypting.')

        return self.__crypto_context.serialize(digest, cipher_text).encode(encoding='UTF-8')


    def __parse_cipher_text_AAD(self, aad: bytes) -> CiphertextAAD:
        assert isinstance(aad, bytes)
        j = json.loads(aad)
        return CiphertextAAD(**j)

    def __verify_message(self, aad: CiphertextAAD, cfg: p.CryptoConfig, ciphertext, plaintext: p.Plaintext) -> bool:
        assert isinstance(aad, CiphertextAAD)
        assert isinstance(cfg, p.CryptoConfig)
        assert isinstance(plaintext, p.Plaintext)
        # FIXME: figure out import for this
        # assert isinstance(ciphertext, PyCapsule)

        sender_key = self.__get_or_download_public_key(aad.senderKeyID)
        return self.__crypto_context.verify(sender_key, plaintext, ciphertext)

    def __find_viable_decryption_use_domains(self) -> list:
        use_domains = self.crypto_config.symmetric_key_use_domains
        viable_domains = [domain for domain in use_domains if domain.symmetric_key_decryption_allowed]
        return viable_domains

    def __is_key_id_decryption_viable(self, key_id: str) -> bool:
        assert isinstance(key_id, str)
        viable_decryption_domains = self.__find_viable_decryption_use_domains()
        for domain in viable_decryption_domains:
            if key_id in domain.encryption_key_ids:
                return True
        return False

    def decrypt(self, cipher_text: bytes) -> bytes:
        assert isinstance(cipher_text, bytes)
        self.__verify_bootstrapped_and_registered()
        self.__update_config_by_elasped_time(MAX_ELASPED_TIME)

        cipher_text_blob, cfg = self.__crypto_context.deserialize(cipher_text)
        aad = self.__crypto_context.extract_unverified_aad(cipher_text).aad
        aad = self.__parse_cipher_text_AAD(aad)
        if not self.__is_key_id_decryption_viable(aad.cryptoKeyID):
            self.logger.warning("Ciphertext is no longer viable for decryption")
            raise NoValidUseDomainsForDecryptionError("Ciphertext is no longer viable for decryption")

        key = self.__get_key(aad.cryptoKeyID)
        pmKey = p.Key(p.SymmetricCipher(cfg.symm_cipher), key)
        plain_text, need_verification = self.__crypto_context.decrypt(pmKey, cipher_text_blob)
        if need_verification and not self.__verify_message(aad, cfg, cipher_text_blob, plain_text):
            self.logger.warning("Tampering of data detected, verification failed.")
            raise CoreCryptoError("Tampering of data detected, verification failed.")

        result = plain_text.data

        assert isinstance(result, bytes)
        return result

