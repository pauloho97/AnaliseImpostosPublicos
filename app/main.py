# main.py
# Ponto de entrada do projeto
# - Carrega e trata o CSV de saúde usando a função do limpezaCSV.py
# - Exibe algumas informações iniciais para validar a limpeza
# - Para rodar no console: python -m app.main

from app.limpezaCSV import CarregarTratarCsv, MostrarInfoBasica

def main():
    # Carregar apenas o CSV da saúde
    dataFrameSaude = CarregarTratarCsv("data/despesas_saude_subfuncao.csv", setor="Saúde")
    # Carregar apenas o CSV da educação
    dataFrameEducacao = CarregarTratarCsv("data/despesas_educacao_subfuncao.csv", setor="Educação")
    # Carregar apenas o CSV da segurança pública
    dataFrameSegurancaPublica = CarregarTratarCsv("data/despesas_seguranca_publica_subfuncao.csv", setor="Segurança Pública")
    # Carregar apenas o CSV do misnistério dos transportes
    dataFrameTransportes = CarregarTratarCsv("data/despesas_ministerio_transportes_subfuncao.csv", setor="Transportes")
    # Carregar apenas o CSV da previdência social
    dataFramePrevidenciaSocial = CarregarTratarCsv("data/despesas_previdencia_social_subfuncao.csv", setor="Previdência Social")


    # Exibir informações básicas para validar a limpeza dos dados
    MostrarInfoBasica(dataFrameSaude, nome_setor="Saúde")
    MostrarInfoBasica(dataFrameEducacao, nome_setor="Educação")
    MostrarInfoBasica(dataFrameSegurancaPublica, nome_setor="Segurança Pública")
    MostrarInfoBasica(dataFrameTransportes, nome_setor="Transportes")
    MostrarInfoBasica(dataFramePrevidenciaSocial, nome_setor="Previdência Social")
if __name__ == "__main__":
    main()
