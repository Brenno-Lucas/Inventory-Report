from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        simple_report = SimpleReport.generate(data)

        company_products = Counter(
            [product["nome_da_empresa"] for product in data]
        ).most_common()

        simple_report += '\nProdutos estocados por empresa:\n'

        for company, quantity in company_products:
            simple_report += f"- {company}: {quantity}\n"

        return simple_report
