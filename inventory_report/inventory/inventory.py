from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xmltodict


class Inventory:

    def __file_checker(file_path):
        with open(file_path, encoding="utf-8") as file:
            if (file_path.endswith('.csv')):
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))
            elif (file_path.endswith('.json')):
                return json.load(file)
            elif (file_path.endswith('.xml')):
                return xmltodict.parse(file.read())["dataset"]["record"]

    def __file_reader(file_path):
        try:
            return Inventory.__file_checker(file_path)
        except FileNotFoundError:
            raise FileNotFoundError("FILE NOT FOUND: " + file_path)
        except ValueError:
            raise ValueError("FILE WITH INVALID FORMAT")

    @staticmethod
    def import_data(file_path, report_type):
        read_file = Inventory.__file_reader(file_path)

        if (report_type == "simples"):
            return SimpleReport.generate(read_file)
        elif (report_type == "completo"):
            return CompleteReport.generate(read_file)
