from peacemakr.persister_base import Persister

class InMemoryPersister(Persister):

    def __init__(self):
        self.__persister = {}

    def save(self, key, value):
        self.__persister[key] = value

    def load(self, key):
        return self.__persister[key]

    def exists(self, key):
        return key in self.__persister.keys()

    def key_nums(self):
        return len(self.__persister.keys())
