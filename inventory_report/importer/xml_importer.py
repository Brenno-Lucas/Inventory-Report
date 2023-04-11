from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", encoding="utf-8") as file:
            list = xmltodict.parse(file.read())
            return list["dataset"]["record"]
