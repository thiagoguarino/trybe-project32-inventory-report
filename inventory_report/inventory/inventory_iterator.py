from collections.abc import Iterator


# file authorship: thiago guarino
class InventoryIterator(Iterator):
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.index_from_object = 0

    def __next__(self):
        data = self.iterable_object[self.index_from_object]

        if not data:
            raise StopIteration

        self.index_from_object += 1
        return data
