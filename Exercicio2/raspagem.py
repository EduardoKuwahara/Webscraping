import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

produtos = []
for div in soup.find_all("div", class_="produto"):
    produtos.append({
        "nome": div.find("h2", class_="nome").get_text(strip=True),
        "fabricante": div.find("p", class_="fabricante").get_text(strip=True),
        "categoria": div.find("p", class_="categoria").get_text(strip=True),
        "preco": div.find("p", class_="preco").get_text(strip=True),
        "estoque": div.find("p", class_="estoque").get_text(strip=True),
    })

print("=== TODOS OS PRODUTOS ===\n")
for p in produtos:
    print(f"Produto:    {p['nome']}")
    print(f"Fabricante: {p['fabricante']}")
    print(f"Categoria:  {p['categoria']}")
    print(f"Preço:      {p['preco']}")
    print(f"Estoque:    {p['estoque']}")
    print("-" * 40)

print("\n=== APENAS PRODUTOS DISPONÍVEIS ===\n")
for p in produtos:
    if p["estoque"] == "Disponível":
        print(f"{p['nome']} ({p['fabricante']}) - {p['preco']}")