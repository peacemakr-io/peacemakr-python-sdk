import peacemakr_sdk
from peacemakr_sdk.factory import Factory
from peacemakr_sdk.impl.persister_impl import InMemoryPersister

def main():
    api_key = "/ZW/VzgAgLjGfORzyEuWPxkp8O37hgzkU+uXGbc8Dtw="
    persister = InMemoryPersister()

    sdk = Factory().get_crypto_sdk(api_key=api_key,
                                   client_name="test client",
                                   peacemakr_hostname="http://localhost:8080",
                                   persister=persister
                                   )
    
    sdk.register()
    # sdk.sync()
    # sdk.encrypt(b'some text')
    # sdk.encrypt_in_domain(b'some text', "some domain")
    # sdk.decrypt(b'cipher text')


if __name__ == "__main__":
    main()  


