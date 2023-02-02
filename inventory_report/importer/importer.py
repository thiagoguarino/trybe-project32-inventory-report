import abc


class Importer(abc.ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def import_data(self, file):
        '''interface method to import data
        from different file type'''
        return
