from inventory_report.importer.importer import Importer
import json


# file authorship: thiago guarino
class JsonImporter(Importer):

    @staticmethod
    def import_data(file_path):
        if (file_path.endswith('.json')):
            with open(file_path, encoding="utf-8") as file:
                return list(json.load(file))

        raise ValueError("Arquivo inválido")
