#Testes unitários para a função de limpeza e tratamento dos dados das despesas públicas.
# O teste verifica se a função CarregarTratarCsvReceitas está funcionando corretamente,
# garantindo que os dados sejam carregados, tratados e convertidos para o formato adequado.


import pandas as pd
from app.limpezaDespesasCSV import CarregarTratarCsvDespesas

def testCarregarDespesasSaude():
    # Carrega o CSV de despesas da Saúde
    df = CarregarTratarCsvDespesas("data/despesas_saude_subfuncao.csv", setor="Saúde")

    # 1. DataFrame não pode estar vazio
    assert not df.empty

    # 2. Lista de colunas que devem existir e ser float
    colunas_numericas = ["Valor Empenhado", "Valor Liquidado", "Valor Pago", "Valor Restos a Pagar Pagos"]

    # 3. Para cada coluna da lista:
    for coluna in colunas_numericas:
        # Testa se a coluna existe
        assert coluna in df.columns
        # Testa se os valores são float
        assert pd.api.types.is_float_dtype(df[coluna])

    # 4. Setor deve estar correto
    assert (df["Setor"] == "Saúde").all()


def test_carregar_despesas_educacao():
    # Carrega o CSV de despesas da Educação
    df = CarregarTratarCsvDespesas("data/despesas_educacao_subfuncao.csv", setor="Educação")
    assert not df.empty
    colunas_numericas = ["Valor Empenhado", "Valor Liquidado", "Valor Pago", "Valor Restos a Pagar Pagos"]
    for coluna in colunas_numericas:
        assert coluna in df.columns
        assert pd.api.types.is_float_dtype(df[coluna])
    assert (df["Setor"] == "Educação").all()


def test_carregar_despesas_seguranca():
    # Carrega o CSV de despesas da Segurança Pública
    df = CarregarTratarCsvDespesas("data/despesas_seguranca_publica_subfuncao.csv", setor="Segurança Pública")
    assert not df.empty
    colunas_numericas = ["Valor Empenhado", "Valor Liquidado", "Valor Pago", "Valor Restos a Pagar Pagos"]
    for coluna in colunas_numericas:
        assert coluna in df.columns
        assert pd.api.types.is_float_dtype(df[coluna])
    assert (df["Setor"] == "Segurança Pública").all()


def test_carregar_despesas_previdencia():
    # Carrega o CSV de despesas da Previdência Social
    df = CarregarTratarCsvDespesas("data/despesas_previdencia_social_subfuncao.csv", setor="Previdência Social")
    assert not df.empty
    colunas_numericas = ["Valor Empenhado", "Valor Liquidado", "Valor Pago", "Valor Restos a Pagar Pagos"]
    for coluna in colunas_numericas:
        assert coluna in df.columns
        assert pd.api.types.is_float_dtype(df[coluna])
    assert (df["Setor"] == "Previdência Social").all()


def test_carregar_despesas_transportes():
    # Carrega o CSV de despesas do Ministério dos Transportes
    df = CarregarTratarCsvDespesas("data/despesas_ministerio_transportes_subfuncao.csv", setor="Transportes")
    assert not df.empty
    colunas_numericas = ["Valor Empenhado", "Valor Liquidado", "Valor Pago", "Valor Restos a Pagar Pagos"]
    for coluna in colunas_numericas:
        assert coluna in df.columns
        assert pd.api.types.is_float_dtype(df[coluna])
    assert (df["Setor"] == "Transportes").all()