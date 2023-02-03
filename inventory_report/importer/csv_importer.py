from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @staticmethod
    def import_data(file_path):
        if (file_path.endswith('.csv')):
            with open(file_path, encoding="utf-8") as file:
                return list(csv.DictReader(
                  file,
                  delimiter=",",
                  quotechar='"'
                ))

        raise ValueError("Arquivo inválido")
