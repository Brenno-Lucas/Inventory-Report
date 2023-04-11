import os
import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

report = {
    "simples": SimpleReport,
    "completo": CompleteReport,
}

file_type = {
    ".csv": csv,
    ".json": JsonImporter,
    ".xml": XmlImporter,
}


class Inventory:
    @staticmethod
    def import_data(file: str, type: str):
        test = os.path.splitext(file)[1]
        if test == '.csv':
            with open(file, "r") as file:
                inventory = []
                data = file_type[test].DictReader(file)
                for item in data:
                    inventory.append(item)
                return(report[type].generate(inventory))
        else:
            return report[type].generate(file_type[test].import_data(file))
