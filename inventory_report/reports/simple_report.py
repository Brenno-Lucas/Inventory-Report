from datetime import date
from collections import Counter


class SimpleReport:

    @staticmethod
    def generate(report):
        manufacturing_date = min(
            [product["data_de_fabricacao"] for product in report]
            )
        expiration_date = min([
                product["data_de_validade"]
                for product in report
                if product["data_de_validade"] > str(date.today())
            ])
        company = Counter(
            [product["nome_da_empresa"] for product in report]
        ).most_common()[0][0]

        return f"""Data de fabricação mais antiga: {manufacturing_date}
Data de validade mais próxima: {expiration_date}
Empresa com mais produtos: {company}"""
