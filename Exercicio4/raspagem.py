import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

livros = []
for div in soup.find_all("div", class_="livro"):
    palavras = [li.get_text(strip=True)
                for li in div.find("ul", class_="palavras-chave").find_all("li")]
    livros.append({
        "titulo": div.find("h2", class_="titulo").get_text(strip=True),
        "autor": div.find("p", class_="autor").get_text(strip=True),
        "ano": div.find("p", class_="ano").get_text(strip=True),
        "genero": div.find("p", class_="genero").get_text(strip=True),
        "situacao": div.find("p", class_="situacao").get_text(strip=True),
        "palavras": palavras,
    })

print("=== TODOS OS LIVROS ===\n")
for l in livros:
    print(f"Título:   {l['titulo']}")
    print(f"Autor:    {l['autor']}")
    print(f"Ano:      {l['ano']}")
    print(f"Gênero:   {l['genero']}")
    print(f"Situação: {l['situacao']}")
    print("Palavras-chave:")
    for p in l["palavras"]:
        print(f"  - {p}")
    print("-" * 40)

print("\n=== LIVROS DISPONÍVEIS ===\n")
for l in livros:
    if l["situacao"] == "Disponível":
        print(f"{l['titulo']} - {l['autor']} ({l['ano']})")