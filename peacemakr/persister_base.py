from abc import ABC, abstractmethod

class Persister(ABC):

    @abstractmethod
    def save(self, key, value):
        pass

    @abstractmethod
    def load(self, key):
        pass

    @abstractmethod
    def exists(self, key):
        pass
