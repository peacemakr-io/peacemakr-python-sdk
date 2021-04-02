import os
import pickle

from peacemakr.persister_base import Persister

class InMemoryPersister(Persister):

    def __init__(self):
        self.__persister = {}

    def save(self, key, value):
        self.__persister[key] = value

    def load(self, key):
        if not self.exists(key):
            return None
        return self.__persister[key]

    def exists(self, key):
        return key in self.__persister.keys()

    def key_nums(self):
        return len(self.__persister.keys())

class DiskPersister(Persister):
    def __init__(self, prefix: str):
        self.__persister = {}
        self.__prefix = prefix

    def key_nums(self):
        return len(self.__persister.keys())

    def save(self, key, value):
        # Store the value in the hot cache, but also write it to disk
        self.__persister[key] = value
        # TODO: Fix this
        # this is a hack to make sure we can save key_id (ex: z981l+Sak/jALkdlzjksl..) by subsituting '/' with '_'
        # if key_id has '/', it will cause file creation error
        key = key.replace('/', '_')
        path = os.path.join(self.__prefix, key)
        with open(path, "wb+") as f:
            pickle.dump(value, f, protocol=0)

    def load(self, key):
        # If the value is in the cache, then return it
        if key in self.__persister:
            return self.__persister[key]
        # TODO: Fix this
        # this is a hack to make sure we can save key_id (ex: z981l+Sak/jALkdlzjksl..) by subsituting '/' with '_'
        # if key_id has '/', it will cause file creation error
        key = key.replace('/', '_')
        path = os.path.join(self.__prefix, key)
        if not os.path.isfile(path):
            # We don't have this object
            return None
        # Read the file and return its contents
        with open(path, "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                return None

    def exists(self, key):
        # TODO: Fix this
        # this is a hack to make sure we can save key_id (ex: z981l+Sak/jALkdlzjksl..) by subsituting '/' with '_'
        # if key_id has '/', it will cause file creation error
        key = key.replace('/', '_')
        path = os.path.join(self.__prefix, key)
        return key in self.__persister or os.path.isfile(path)
