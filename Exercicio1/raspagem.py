import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

cursos = soup.find_all("div", class_="curso")
print(f"Total de cursos encontrados: {len(cursos)}\n")

for i, curso in enumerate(cursos, start=1):
    nome = curso.find("h2", class_="nome").get_text(strip=True)
    area = curso.find("p", class_="area").get_text(strip=True)
    carga = curso.find("p", class_="carga").get_text(strip=True)

    print(f"Curso {i}: {nome}")
    print(f"  {area}")
    print(f"  {carga}")
    print("  Assuntos estudados:")
    for assunto in curso.find("ul", class_="assuntos").find_all("li"):
        print(f"    - {assunto.get_text(strip=True)}")
    print("-" * 40)