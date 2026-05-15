import sqlite3
from app.limpezaArrecadacoesCSV import CarregarTratarCsvReceitas
from app.limpezaDespesasCSV import CarregarTratarCsvDespesas

# 1. Conectar ao banco
conexaoBanco = sqlite3.connect("analise_impostos.db")

# 2. Listas de arquivos
arquivosReceitas = [
    ("data/receitas_educacao.csv", "Educação"),
    ("data/receitas_previdencia_social.csv", "Previdência Social"),
    ("data/receitas_saude.csv", "Saúde"),
    ("data/receitas_seguranca.csv", "Segurança Pública"),
    ("data/receitas_transportes.csv", "Transportes")
]

arquivosDespesas = [
    ("data/despesas_educacao_subfuncao.csv", "Educação"),
    ("data/despesas_previdencia_social_subfuncao.csv", "Previdência Social"),
    ("data/despesas_saude_subfuncao.csv", "Saúde"),
    ("data/despesas_seguranca_publica_subfuncao.csv", "Segurança Pública"),
    ("data/despesas_ministerio_transportes_subfuncao.csv", "Transportes")
]

# 3. Processar e inserir RECEITAS
print("Iniciando carga de Receitas...")
primeiroItem = True
for caminho, setor in arquivosReceitas:
    dataFrameReceitas = CarregarTratarCsvReceitas(caminho, setor=setor)
    
    if primeiroItem:
        # O primeiro arquivo 'substitui' a tabela antiga (limpa o banco)
        dataFrameReceitas.to_sql("receitas", conexaoBanco, if_exists="replace", index=False)
        primeiroItem = False
    else:
        # Os demais arquivos são acrescentados
        dataFrameReceitas.to_sql("receitas", conexaoBanco, if_exists="append", index=False)

# 4. Processar e inserir DESPESAS
print("Iniciando carga de Despesas...")
primeiroItem = True
for caminho, setor in arquivosDespesas:
    dataFrameDespesas = CarregarTratarCsvDespesas(caminho, setor=setor)
    
    if primeiroItem:
        # O primeiro arquivo 'substitui' a tabela antiga (limpa o banco)
        dataFrameDespesas.to_sql("despesas", conexaoBanco, if_exists="replace", index=False)
        primeiroItem = False
    else:
        # Os demais arquivos são acrescentados
        dataFrameDespesas.to_sql("despesas", conexaoBanco, if_exists="append", index=False)

# 5. Fechar conexão
conexaoBanco.close()
print("Carga finalizada com sucesso! O banco analise_impostos.db foi atualizado.")
