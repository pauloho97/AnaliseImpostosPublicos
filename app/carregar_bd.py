import sqlite3
from app.limpezaArrecadacoesCSV import CarregarTratarCsvReceitas
from app.limpezaDespesasCSV import CarregarTratarCsvDespesas

# 1. Conectar ao banco
conn = sqlite3.connect("analise_impostos.db")

# 2. Lista de arquivos de receitas e despesas com seus setores
arquivos_receitas = [
    ("data/receitas_educacao.csv", "Educação"),
    ("data/receitas_previdencia_social.csv", "Previdência Social"),
    ("data/receitas_saude.csv", "Saúde"),
    ("data/receitas_seguranca.csv", "Segurança Pública"),
    ("data/receitas_transportes.csv", "Transportes")
]

arquivos_despesas = [
    ("data/despesas_educacao_subfuncao.csv", "Educação"),
    ("data/despesas_previdencia_social_subfuncao.csv", "Previdência Social"),
    ("data/despesas_saude_subfuncao.csv", "Saúde"),
    ("data/despesas_seguranca_publica_subfuncao.csv", "Segurança Pública"),
    ("data/despesas_ministerio_transportes_subfuncao.csv", "Transportes")
]

# 3. Processar e inserir receitas
for caminho, setor in arquivos_receitas:
    df_receitas = CarregarTratarCsvReceitas(caminho, setor=setor)
    df_receitas.to_sql("receitas", conn, if_exists="append", index=False)

# 4. Processar e inserir despesas
for caminho, setor in arquivos_despesas:
    df_despesas = CarregarTratarCsvDespesas(caminho, setor=setor)
    df_despesas.to_sql("despesas", conn, if_exists="append", index=False)

# 5. Fechar conexão
conn.close()
