from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", encoding="utf-8") as file:
            list = json.load(file)
            return list
