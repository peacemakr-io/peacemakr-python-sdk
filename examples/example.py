"""
  Authors: Daniel Huang, Clyde Caradine, Maxime Cuny

  This is a basic example on how to call Peacemakrs
  Python SDK functionalities.
"""
import random
from peacemakr_sdk.impl.persister_impl import InMemoryPersister
import peacemakr_sdk.factory as Factory

def example(configuration: dict):
  global os
  # Simply call get_crypto_sdk() with the according
  # parameters to obtain you SDK object
  sdk = Factory.get_crypto_sdk(**configuration)

  # Register you client with the server
  sdk.register()

  # Freshen up your configuration and keys
  # via a few network calls
  sdk.sync()

  # Let's generate some random bytes for our plain text
  plain_text = bytes(bytearray(random.getrandbits(8) for _ in range(4096)))

  # Encrypt the plain_text
  cipher_text_1 = sdk.encrypt(plain_text)

  # Encrypt the plain same plain text but
  # in a specific domain
  cipher_text_2 = sdk.encrypt_in_domain(plain_text, "test domain")

  # Decrypt your cipher texts
  decrypted_text_1 = sdk.decrypt(cipher_text_1)
  decrypted_text_2 = sdk.decrypt(cipher_text_2)
  assert(decrypted_text_1 == decrypted_text_2)


if __name__ == "__main__":
  '''
  api_key: replace with the one you obtained after signing up on https://admin.peacemakr.io/
  client_name: the name you wish to give your client
  peacemakr_hostname: the hostname of your Peacemakr instance
  persister: the persister you want to use, you can implement yours
             and integrate it by making it the child of Persister (persister_base.py)
  logger: if you need a specific type of logging done. A default logger will be set
          if not specified.
  '''
  configuration = {
    'api_key': 'E9qCEmgOAR/009W7OSIYsr67VwIYbGuGy++7mZ4/56U=',
    'client_name': 'example_client',
    'peacemakr_hostname': 'http://localhost:8080',
    'persister': InMemoryPersister(),
    'logger': None
  }
  example(configuration)
