import requests
from bs4 import BeautifulSoup
import argparse

def extract_titles(url):
    # Enviar uma solicitação HTTP para o site
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parsear o conteúdo da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos os títulos (supondo que estão em tags <h2>)
        titles = soup.find_all('h2')

        # Extrair e imprimir os textos dos títulos
        for title in titles:
            print(title.get_text())
    else:
        print(f"Erro ao acessar o site: {response.status_code}")

def main():
    # Configurando o parser de argumentos
    parser = argparse.ArgumentParser(description='Extrair títulos de um site.')
    parser.add_argument('url', type=str, help='URL do site a ser analisado')
    
    args = parser.parse_args()
    
    # Chamar a função de extração
    extract_titles(args.url)

if __name__ == "__main__":
    main()
