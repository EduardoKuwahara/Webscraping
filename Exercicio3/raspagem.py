import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"
CATEGORIA_ESCOLHIDA = "Tecnologia"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

noticias = []
for art in soup.find_all("article", class_="noticia"):
    noticias.append({
        "categoria": art.find("span", class_="categoria").get_text(strip=True),
        "titulo": art.find("h2", class_="titulo").get_text(strip=True),
        "data": art.find("time", class_="data").get_text(strip=True),
        "resumo": art.find("p", class_="resumo").get_text(strip=True),
        "autor": art.find("p", class_="autor").get_text(strip=True),
    })

for n in noticias:
    print("=" * 50)
    print(f"Categoria: {n['categoria']}")
    print(f"Título:    {n['titulo']}")
    print(f"Data:      {n['data']}")
    print(f"Resumo:    {n['resumo']}")
    print(f"Autor:     {n['autor']}")
print("=" * 50)

print(f"\nTítulos da categoria '{CATEGORIA_ESCOLHIDA}':")
for n in noticias:
    if n["categoria"] == CATEGORIA_ESCOLHIDA:
        print(f"  - {n['titulo']}")