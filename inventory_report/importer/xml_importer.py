from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):

    @staticmethod
    def import_data(file_path):
        try:
            if (file_path.endswith(".json")):
                with open(file_path, encoding="utf-8") as xml_file:
                    reader = xmltodict.parse(xml_file)
                    return reader
        except ValueError:
            raise ValueError("Arquivo inválido")
