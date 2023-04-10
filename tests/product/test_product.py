from inventory_report.inventory.product import Product
import pytest


@pytest.fixture
def product():
    return {
        "id": 1,
        "nome_do_produto": "Produto",
        "nome_da_empresa": "Test",
        "data_de_fabricacao": "2000-03-13",
        "data_de_validade": "2023-10-04",
        "numero_de_serie": "13032000",
        "instrucoes_de_armazenamento": "instrução",
    }


def test_cria_produto(product):
    products = Product(
        product["id"],
        product["nome_do_produto"],
        product["nome_da_empresa"],
        product["data_de_fabricacao"],
        product["data_de_validade"],
        product["numero_de_serie"],
        product["instrucoes_de_armazenamento"],
    )

    assert products.id == 1
    assert products.nome_do_produto == "Produto"
    assert products.nome_da_empresa == "Test"
    assert products.data_de_fabricacao == "2000-03-13"
    assert products.data_de_validade == "2023-10-04"
    assert products.numero_de_serie == "13032000"
    assert products.instrucoes_de_armazenamento == "instrução"
