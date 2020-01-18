import peacemakr_sdk
import peacemakr_sdk.factory as Factory


def main():
    api_key = "api-key"
    sdk = Factory.get_crypto_sdk()
    
    sdk.register()
    sdk.sync()
    sdk.encrypt(b'some text')
    sdk.encrypt_in_domain(b'some text', "some domain")
    sdk.decrypt(b'cipher text')


if __name__ == "__main__":
    main()  


