from abc import ABCMeta, abstractmethod


class IFeature(metaclass=ABCMeta):
    @abstractmethod
    def build(self):
        pass
