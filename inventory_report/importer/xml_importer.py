from inventory_report.importer.importer import Importer
import xmltodict


# file authorship: thiago guarino
class XmlImporter(Importer):

    @staticmethod
    def import_data(file_path):
        if (file_path.endswith('.xml')):
            with open(file_path, encoding="utf-8") as file:
                return list(xmltodict.parse(file.read())["dataset"]["record"])

        raise ValueError("Arquivo inválido")
