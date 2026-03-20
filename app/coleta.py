import requests

def buscar_dados():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/01/2023"

    try:
        response = requests.get(url)

        print("Status code:", response.status_code)  # 👈 debug

        if response.status_code == 200:
            return response.json()
        else:
            print("Erro:", response.text)
            return None

    except Exception as e:
        print("Erro na requisição:", e)
        return None

def main():
    dados = buscar_dados()

    if dados:
        print("Dados recebidos:")
        print(dados[:5])
    else:
        print("Nenhum dado retornado")

if __name__ == "__main__":
    main()