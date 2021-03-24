import os

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

    class DiskPersister(Persister):
        def __init__(self, prefix: str):
            self.__persister = {}
            self.__prefix = prefix

        def save(self, key, value):
            # Store the value in the hot cache, but also write it to disk
            self.__persister[key] = value
            path = os.path.join(self.__prefix, key)
            with open(path, "w+") as f:
                f.write(value)

        def load(self, key):
            # If the value is in the cache, then return it
            if key in self.__persister:
                return self.__persister[key]
            path = os.path.join(self.__prefix, key)
            if not os.path.isfile(path):
                # We don't have this object
                return None
            # Read the file and return its contents
            with open(path, "r") as f:
                return f.read()

        def exists(self, key):
            path = os.path.join(self.__prefix, key)
            return key in self.__persister or os.path.isfile(path)
