import base64
import peacemakr_core_crypto_python as p

from random import randint
from time import time

from peacemakr_sdk.crypto_base import PeacemakrCryptoSDK
from peacemakr_sdk.generated import SymmetricKeyUseDomain


# TODO : Check if this is doing it's job for picking random index in the list.
def random_index(l: list):
    return l[randint(0, len(l) - 1)]

DEFAULT_MESSAGE_DIGEST = p.DigestAlgorithm.SHA_256

class CryptoImpl(PeacemakrCryptoSDK):

    def __init__(self, api_key=""):
        self.api_key = api_key

        self.__Chacha20Poly1305 = "Peacemakr.Symmetric.CHACHA20_POLY1305"
        self.__Aes128gcm = "Peacemakr.Symmetric.AES_128_GCM"
        self.__Aes192gcm = "Peacemakr.Symmetric.AES_192_GCM"
        self.__Aes256gcm = "Peacemakr.Symmetric.AES-256-GCM"

        self.__Sha224 = "Peacemakr.Digest.SHA_224"
        self.__Sha256 = "Peacemakr.Digest.SHA_256"
        self.__Sha384 = "Peacemakr.Digest.SHA_384"
        self.__Sha512 = "Peacemakr.Digest.SHA_512"

    def register(self):
        print("In register")
        pass

    def sync(self):
        print("In sync")
        pass

    # TODO : Fix type hinting for domain.
    def __domain_is_valid_for_encryption(self, domain: SymmetricKeyUseDomain) -> bool:
        # TODO : Test the time with the java time to make sure everything is ok.
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

        # TODO : Handle custom exceptions.
        if not valid_domain_with_this_name:
            raise Exception("No valid use domain for encryption found, with the name " + use_domain_name)

        return random_index(valid_domain_with_this_name)

    def __get_encryption_key_id(self, use_domain: SymmetricKeyUseDomain) -> str:
        return random_index(use_domain.encryption_key_ids)

    def __get_key(self, key_id: str) -> bytes:
        # TODO : Handle already existing keys using persister.

        # Is this list really required ?
        required_keys = [key_id]

        # Check function exists
        assert self.__download_and_save_all_keys, "Missing implementation for __download_and_save_all_keys"
        self.__download_and_save_all_keys(required_keys)

        # TODO : Handle persister missing keys exception.

        key = self.persister.load(key_id)
        return key

    def __get_symmetric_cipher(self, symmetric_key_encryption_alg: str) -> p.SymmetricCipher:
        # FIXME: This needs some cleaning up, last elt of dict should not exist but there is a problem
        select_cipher = {
            self.__Chacha20Poly1305: p.SymmetricCipher.CHACHA20_POLY1305,
            self.__Aes128gcm: p.SymmetricCipher.AES_128_GCM,
            self.__Aes192gcm: p.SymmetricCipher.AES_192_GCM,
            self.__Aes256gcm: p.SymmetricCipher.AES_256_GCM,
            'AES-256-GCM': p.SymmetricCipher.AES_256_GCM
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
        print("In encrypt")
        # TODO: Check if function exists.
        assert self.__verify_bootstrapped_and_registered, "Missing implementation for __verify_bootstrapped_and_registered"
        self.__verify_bootstrapped_and_registered()
        used_domain_name = self.__select_use_domain_name()
        return self.encrypt_in_domain(plain_text, used_domain_name)

    def encrypt_in_domain(self, plain_text: bytes, use_domain_name: str) -> bytes:
        print("In encrypt in domain")
        self.__verify_bootstrapped_and_registered()
        use_domain_for_encryption = self.__get_valid_use_domain_for_encryption(use_domain_name)
        encryption_key_id_for_encryption = self.__get_encryption_key_id(use_domain_for_encryption)

        key = None
        symmetric_cipher = self.__get_symmetric_cipher(use_domain_for_encryption.symmetric_key_encryption_alg)
        try:
            key = p.Key(symmetric_cipher, self.__get_key(encryption_key_id_for_encryption))
        except Exception:
            # TODO : Handle logger error
            # TODO : Handle custom peacemakr errors
            print("Something went wrong with encrypt domain")

        signing_key = self.__get_signing_key()
        digest = self.__get_digest_alg(use_domain_for_encryption.digest_algorithm)

        aad = CiphertextAAD()
        aad.crypto_key_id = encryption_key_id_for_encryption
        aad.sender_key_id = self.persister.load(PERSISTER_PREFERRED_KEYID);

        pm_plain_text = p.Plaintext(plain_text, bytes(json.dumps(aad.__dict__), encoding='utf8'))

        random_device = p.RandomDevice()

        cipher_text = p.CryptoContext().encrypt(key, pm_plain_text, random_device)

        my_priv_key_str = self.persister.load(PERSISTER_PRIV_KEY)
        my_key = p.Key(symmetric_cipher, my_priv_key_str)

        try :
            p.CryptoContext().sign(my_key, pm_plain_text, digest, cipher_text)
        except Exception as e:
            raise(e)

        return p.CryptoContext().serialize(digest, cipher_text)


    def decrypt(self, cipher_text: bytes) -> bytes:
        print("In decrypt")
        pass
