from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


# file authorship: thiago guarino
class InventoryRefactor(Iterable):
    def __init__(self, importer_class):
        self.importer = importer_class
        self.data = list()

    def import_data(self, file_path, report_type="completo"):
        products_in_stock = self.importer.import_data(file_path)

        self.data.extend(products_in_stock)

        if report_type == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)

    def __iter__(self):
        result = InventoryIterator(self.data)
        return result
