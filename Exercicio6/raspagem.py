import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

for evento in soup.find_all("div", class_="evento"):
    nome = evento.find("h2", class_="nome").get_text(strip=True)
    data = evento.find("p", class_="data").get_text(strip=True)
    horario = evento.find("p", class_="horario").get_text(strip=True)
    local = evento.find("p", class_="local").get_text(strip=True)

    palestrantes = [p.get_text(strip=True)
                    for p in evento.find_all("span", class_="palestrante")]

    link = evento.find("a", class_="inscricao")
    texto_link = link.get_text(strip=True)
    href_link = link["href"]

    print(f"Evento:       {nome}")
    print(f"Data:         {data}")
    print(f"Horário:      {horario}")
    print(f"Local:        {local}")
    print(f"Palestrantes: {', '.join(palestrantes)}")
    if len(palestrantes) > 1:
        print(f"  >> Este evento possui {len(palestrantes)} palestrantes!")
    print(f"Inscrição:    {texto_link} -> {href_link}")
    print("-" * 50)