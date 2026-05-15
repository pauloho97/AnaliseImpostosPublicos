import pandas as pd

def CarregarTratarCsvReceitas(caminhoCsv, setor=None):
    dataframe = pd.read_csv(caminhoCsv, sep=";")
    
    # Remover colunas lixo
    dataframe = dataframe.loc[:, ~dataframe.columns.str.contains('^Unnamed')]
    
    # Converter valores monetários
    ColunaValores = [
        "Orçamento Atualizado (Valor Previsto)",
        "Receita Realizada (Valor Arrecadado)",
        "Valor Lançado"
    ]
    
    for coluna in ColunaValores:
        dataframe[coluna] = (
            dataframe[coluna]
            .astype(str)
            .str.replace(".", "", regex=False)   # remove pontos de milhar
            .str.replace(",", ".", regex=False)  # troca vírgula por ponto
        )
        dataframe[coluna] = pd.to_numeric(dataframe[coluna], errors="coerce")
    
    # --- MELHORIA: TRATAMENTO DE NULOS ---
    # Converte qualquer valor vazio (NaN) nas colunas financeiras para 0
    dataframe[ColunaValores] = dataframe[ColunaValores].fillna(0)
    
    # Converter coluna de porcentagem (se quiser usar)
    if "% Previsto/Realizado" in dataframe.columns:
        dataframe["% Previsto/Realizado"] = (
            dataframe["% Previsto/Realizado"]
            .astype(str)
            .str.replace("%", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        dataframe["% Previsto/Realizado"] = pd.to_numeric(dataframe["% Previsto/Realizado"], errors="coerce")
        
        # Também garante que a porcentagem não seja nula
        dataframe["% Previsto/Realizado"] = dataframe["% Previsto/Realizado"].fillna(0)
    
    # Adicionar coluna Setor (se informado)
    if setor:
        dataframe["Setor"] = setor
    
    return dataframe

# Teste de validação
df = CarregarTratarCsvReceitas("data/receitas_saude.csv")
print(df.dtypes)
