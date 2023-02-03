from abc import ABC, ABCMeta, abstractmethod


class Importer(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def import_data(file):
        '''interface method to import data
        from different file type'''
        return
