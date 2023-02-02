from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    @staticmethod
    def import_data(file_path):
        try:
            if (file_path.endswith(".json")):
                with open(file_path, encoding="utf-8") as json_file:
                    reader = json.load(json_file)
                    return reader
        except ValueError:
            raise ValueError("Arquivo inválido")
