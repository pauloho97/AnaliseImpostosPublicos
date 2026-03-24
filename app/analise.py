import pandas as pd

# 1. Ler o CSV
dataFrame = pd.read_csv(
    "data/despesas_saude_subfuncao.csv",
    sep=";"
)

# 2. Remover coluna lixo
dataFrame = dataFrame.loc[:, ~dataFrame.columns.str.contains('^Unnamed')]

# 3. Converter colunas
colunas = [
    "Valor Empenhado",
    "Valor Liquidado",
    "Valor Pago",
    "Valor Restos a Pagar Pagos"
]

for col in colunas:
    dataFrame[col] = (
        dataFrame[col]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    dataFrame[col] = pd.to_numeric(dataFrame[col], errors="coerce")

# 4. Mostrar só 5 linhas (padrão)
print("\n--- PRIMEIRAS 5 ---")
print(dataFrame.head())

print("\n--- ÚLTIMAS 5 ---")
print(dataFrame.tail())

print("\n--- TIPOS ---")
print(dataFrame.dtypes)