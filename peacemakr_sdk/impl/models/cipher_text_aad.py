class CiphertextAAD():
    def __init__(self, cryptoKeyID: str = None, senderKeyID: str = None):
        self.crypto_key_id = cryptoKeyID
        self.sender_key_id = senderKeyID
