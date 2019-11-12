from peacemakr_sdk.persister_base import Persister

class InMemoryPersister(Persister):

    def __init__(self):
        self._persister = {}

    def save(self, key, value):
        self._persister[key] = value

    def load(self, key):
        return self._persister[key]

    def exists(self, key):
        return key in self._persister.keys()