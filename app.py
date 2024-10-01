import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Garante que o pedido foi bem-sucedido
        soup = BeautifulSoup(response.content, 'html.parser')

        # Exemplo: capturando o título da página
        title = soup.title.string if soup.title else "Sem título"
        return title
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar o site: {e}"

def on_submit():
    url = url_entry.get()
    title = scrape_website(url)
    messagebox.showinfo("Título da Página", title)

# Criação da interface gráfica
root = tk.Tk()
root.title("Web Scraper")

# Configuração do layout
tk.Label(root, text="Insira a URL do site:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)
tk.Button(root, text="Submeter", command=on_submit).pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
