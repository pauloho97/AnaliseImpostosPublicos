# main.py
# Ponto de entrada do projeto
# - Carrega e trata o CSV de saúde usando a função do limpezaCSV.py
# - Exibe algumas informações iniciais para validar a limpeza
# - Para rodar no console: python -m app.main

from app.limpezaArrecadacoesCSV import CarregarTratarCsvReceitas
from app.limpezaDespesasCSV import CarregarTratarCsv, MostrarInfoBasica

def main():
    # Carregar CSV das despesas para cada setor usando a função do limpezaDespesasCSV.py
    # Carregar apenas o CSV da saúde.
    dataFrameSaude = CarregarTratarCsvDespesas("data/despesas_saude_subfuncao.csv", setor="Saúde")
    # Carregar apenas o CSV da educação
    dataFrameEducacao = CarregarTratarCsvDespesas("data/despesas_educacao_subfuncao.csv", setor="Educação")
    # Carregar apenas o CSV da segurança pública
    dataFrameSegurancaPublica = CarregarTratarCsvDespesas("data/despesas_seguranca_publica_subfuncao.csv", setor="Segurança Pública")
    # Carregar apenas o CSV do misnistério dos transportes
    dataFrameTransportes = CarregarTratarCsvDespesas("data/despesas_ministerio_transportes_subfuncao.csv", setor="Transportes")
    # Carregar apenas o CSV da previdência social
    dataFramePrevidenciaSocial = CarregarTratarCsvDespesas("data/despesas_previdencia_social_subfuncao.csv", setor="Previdência Social")

    # Carregar CSV das receitas para cada setor usando a função do limpezaArrecadacoesCSV.py
    # Carregar apenas o CSV da saúde
    dataFrameReceitasSaude = CarregarTratarCsvReceitas("data/receitas_saude.csv", setor = "Saúde")
    dataFrameReceitasSegurancaPublica = CarregarTratarCsvReceitas("data/receitas_seguranca.csv", setor = "Segurança Pública")
    dataFrameReceitasTransportes = CarregarTratarCsvReceitas("data/receitas_transportes.csv", setor = "Transportes")
    dataFrameReceitasPrevidenciaSocial = CarregarTratarCsvReceitas("data/receitas_previdencia_social.csv", setor = "Previdência Social")
    dataFrameReceitasEducacao = CarregarTratarCsvReceitas("data/receitas_educacao.csv", setor = "Educação")


    # Exibir informações básicas para validar a limpeza dos dados
    # Dados das despesas
    print("\n\t\t\t\t\t\t\t\033[91m🔴 === DESPESAS === 🔴\033[0m")
    MostrarInfoBasica(dataFrameSaude, nome_setor="Saúde")
    MostrarInfoBasica(dataFrameEducacao, nome_setor="Educação")
    MostrarInfoBasica(dataFrameSegurancaPublica, nome_setor="Segurança Pública")
    MostrarInfoBasica(dataFrameTransportes, nome_setor="Transportes")
    MostrarInfoBasica(dataFramePrevidenciaSocial, nome_setor="Previdência Social")

    # Dados das receitas
    print("\n\t\t\t\t\t\t\t\033[91m🔴 === RECEITAS === 🔴\033[0m")

    MostrarInfoBasica(dataFrameReceitasSaude, nome_setor="Saúde")
    MostrarInfoBasica(dataFrameEducacao, nome_setor="Educação")
    MostrarInfoBasica(dataFrameSegurancaPublica, nome_setor="Segurança Pública")
    MostrarInfoBasica(dataFrameTransportes, nome_setor="Transportes")
    MostrarInfoBasica(dataFramePrevidenciaSocial, nome_setor="Previdência Social")


if __name__ == "__main__":
    main()
