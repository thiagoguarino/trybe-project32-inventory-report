from inventory_report.inventory.product import Product
import pytest


@pytest.fixture
def product_fixture():
    return {
        "id": 1,
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    }


def test_cria_produto(product_fixture):
    new_product = Product(
        product_fixture["id"],
        product_fixture["nome_do_produto"],
        product_fixture["nome_da_empresa"],
        product_fixture["data_de_fabricacao"],
        product_fixture["data_de_validade"],
        product_fixture["numero_de_serie"],
        product_fixture["instrucoes_de_armazenamento"]
    )

    assert new_product.id == 1
    assert new_product.nome_do_produto == "Nicotine Polacrilex"
    assert new_product.nome_da_empresa == "Target Corporation"
    assert new_product.data_de_fabricacao == "2021-02-18"
    assert new_product.data_de_validade == "2023-09-17"
    assert new_product.numero_de_serie == "CR25 1551 4467 2549 4402 1"
    assert new_product.instrucoes_de_armazenamento == "instrucao 1"
