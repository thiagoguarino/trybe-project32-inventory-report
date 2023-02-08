import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


def print_report(importer_class, file_path, report_type):
    report = InventoryRefactor(importer_class).import_data(
        file_path, report_type)
    print(report, end='')


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    file_path = sys.argv[1]

    report_type = sys.argv[2]

    if (file_path.endswith('.csv')):
        return print_report(CsvImporter, file_path, report_type)
    elif (file_path.endswith('.json')):
        return print_report(JsonImporter, file_path, report_type)
    elif (file_path.endswith('.xml')):
        return print_report(XmlImporter, file_path, report_type)


if __name__ == "__main__":
    main()
