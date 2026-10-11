import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

# 1º: localiza cada seção do cardápio
for secao in soup.find_all("section", class_="secao"):
    categoria = secao.find("h2", class_="categoria").get_text(strip=True)
    print("=" * 45)
    print(categoria.upper())
    print("=" * 45)

    # 2º: percorre apenas os itens DESTA seção
    for item in secao.find_all("div", class_="item"):
        nome = item.find("h3", class_="nome").get_text(strip=True)
        descricao = item.find("p", class_="descricao").get_text(strip=True)
        preco = item.find("span", class_="preco").get_text(strip=True)

        print(f"  {nome} - {preco}")
        print(f"    {descricao}")
    print()