#Testes unitários para a função de limpeza e tratamento dos dados de receitas públicas.
# O teste verifica se a função CarregarTratarCsvReceitas está funcionando corretamente,
# garantindo que os dados sejam carregados, tratados e convertidos para o formato adequado.


import pandas as pd
from app.limpezaArrecadacoesCSV import CarregarTratarCsvReceitas

def testCarregarReceitasSaude(): 
    # Carrega o CSV de receitas da Saúde
    df = CarregarTratarCsvReceitas("data/receitas_saude.csv", setor="Saúde")

    # 1. DataFrame não pode estar vazio
    assert not df.empty

    # 2. Lista de colunas que devem existir e ser float
    colunas_numericas = [
        "Orçamento Atualizado (Valor Previsto)",
        "Receita Realizada (Valor Arrecadado)",
        "Valor Lançado"
    ]

    # 3. Para cada coluna da lista:
    for coluna in colunas_numericas:
        # Testa se a coluna existe
        assert coluna in df.columns
        # Testa se os valores são float
        assert pd.api.types.is_float_dtype(df[coluna])

    # 4. Setor deve estar correto
    assert (df["Setor"] == "Saúde").all()


def test_carregar_receitas_educacao(): 
    # Carrega o CSV de receitas da Educação
    df = CarregarTratarCsvReceitas("data/receitas_educacao.csv", setor="Educação")
    assert not df.empty
    colunas_numericas = [
        "Orçamento Atualizado (Valor Previsto)",
        "Receita Realizada (Valor Arrecadado)",
        "Valor Lançado"
    ]
    for coluna in colunas_numericas:
        assert coluna in df.columns
        assert pd.api.types.is_float_dtype(df[coluna])
    assert (df["Setor"] == "Educação").all()


def test_carregar_receitas_seguranca(): 
    # Carrega o CSV de receitas da Segurança
    df = CarregarTratarCsvReceitas("data/receitas_seguranca.csv", setor="Segurança")
    assert not df.empty
    colunas_numericas = [
        "Orçamento Atualizado (Valor Previsto)",
        "Receita Realizada (Valor Arrecadado)",
        "Valor Lançado"
    ]
    for coluna in colunas_numericas:
        assert coluna in df.columns
        assert pd.api.types.is_float_dtype(df[coluna])
    assert (df["Setor"] == "Segurança").all()


def test_carregar_receitas_previdencia(): 
    # Carrega o CSV de receitas da Previdência Social
    df = CarregarTratarCsvReceitas("data/receitas_previdencia_social.csv", setor="Previdência Social")
    assert not df.empty
    colunas_numericas = [
        "Orçamento Atualizado (Valor Previsto)",
        "Receita Realizada (Valor Arrecadado)",
        "Valor Lançado"
    ]
    for coluna in colunas_numericas:
        assert coluna in df.columns
        assert pd.api.types.is_float_dtype(df[coluna])
    assert (df["Setor"] == "Previdência Social").all()