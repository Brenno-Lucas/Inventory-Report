from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            list = [i for i in reader]
            return list
