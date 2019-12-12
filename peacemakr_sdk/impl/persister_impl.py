from peacemakr_sdk.persister_base import Persister

class InMemoryPersister(Persister):

    def __init__(self):
        self.__persister = {}

    def save(self, key, value):
        self.__persister[key] = value

    def load(self, key):
        return self.__persister[key]

    def exists(self, key):
        return key in self.__persister.keys()

    def debug(self):
        for key in self.__persister:
            print(key, "->", self.__persister[key])
