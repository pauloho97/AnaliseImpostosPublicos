# Código antigo na tentativa de coletar dados da API do Portal da Transparência.

# import requests

# TOKEN = "e195d64f4cc21c0b139620372db87c73"

# def testar_token():
#     url = "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos"

#     headers = {
#         "chave-api-dados": TOKEN,
#         "Accept": "application/json"
#     }

#     response = requests.get(url, headers=headers)

#     print(response.request.headers)
    
#     print("Status code:", response.status_code)

#     if response.status_code == 200:
#         dados = response.json()
#         print("Token funcionando ✔️")
#         print(dados[:2])  # mostra 2 registros
#     else:
#         print("Erro:", response.text)

# def main():
#     testar_token()

# if __name__ == "__main__":
#     main()


# def buscar_gastos():
#     url = "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos"
#     headers = {
#         "chave-api-dados": TOKEN,
#         "Accept": "application/json"
#     }

#     params = {
#         "ano": 2024,
#         "mes": 1,
#         "codigoFuncao": "12",
#         "pagina": 1
#     }

#     response = requests.get(url, headers=headers, params=params)

#     print("Status code:", response.status_code)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Erro:", response.text)
#         return None


# def main():
#     dados = buscar_gastos()

#     if dados:
#         print("Dados recebidos:")
#         print(dados[:2])  # mostra 2 registros
#     else:
#         print("Nenhum dado retornado")


# if __name__ == "__main__":
#     main()