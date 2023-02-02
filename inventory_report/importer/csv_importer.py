from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @staticmethod
    def import_data(file_path):
        try:
            if (file_path.endswith(".csv")):
                with open(file_path, encoding="utf-8") as csv_file:
                    reader = csv.DictReader(
                      csv_file,
                      delimiter=",",
                      quotechar='"'
                    )
                    return list(reader)
        except ValueError:
            raise ValueError("Arquivo inválido")
