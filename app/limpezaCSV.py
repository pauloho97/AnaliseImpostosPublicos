# Arquivo para carregar e tratar os dados do CSV, removendo colunas desnecessárias e convertendo 
# os valores monetários para um formato numérico adequado.


import pandas as pd

def CarregarTratarCsv(caminhoCsv, setor=None):
    dataframe = pd.read_csv(caminhoCsv, sep=";")
    
    # Remover colunas lixo
    dataframe = dataframe.loc[:, ~dataframe.columns.str.contains('^Unnamed')]
    
    # Converter valores monetários
    ColunaValores = [
        "Valor Empenhado",
        "Valor Liquidado",
        "Valor Pago",
        "Valor Restos a Pagar Pagos"
    ]
    
    for coluna in ColunaValores:
        dataframe[coluna] = (
            dataframe[coluna]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        dataframe[coluna] = pd.to_numeric(dataframe[coluna], errors="coerce")
    
    # Converter Mês Ano para datetime
    dataframe["MesAno"] = pd.to_datetime(dataframe["Mês Ano"], format="%m/%Y")


    # Adicionar coluna Setor (se informado)
    if setor:
        dataframe["Setor"] = setor
    
    return dataframe
