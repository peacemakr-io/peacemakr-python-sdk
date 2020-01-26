class CiphertextAAD():
    def __init__(self, cryptoKeyID: str = '', senderKeyID: str = ''):
        self.cryptoKeyID = cryptoKeyID
        self.senderKeyID = senderKeyID
