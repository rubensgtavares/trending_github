import requests
from requests.exceptions import HTTPError, RequestException
from bs4 import BeautifulSoup
import csv

def crawl_website(url: str, headers: dict) -> str | None:
    try:
        resposta = requests.get(url=url, headers=headers)
        resposta.raise_for_status()
        return resposta.text  # Retorna o conteúdo da resposta
    except HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
    except RequestException as req_err:
        print(f"Erro na requisição: {req_err}")
    return None  # Retorna None se houver erro

URL = 'https://github.com/trending'
conteudo1 = crawl_website(url=URL,headers=headers)
with open(file='10_trending_repo.html',mode='w', encoding='utf8') as fp:
    fp.write(conteudo1)

# Carregar o HTML salvo
with open("10_trending_repo.html", "r", encoding="utf8") as fp:
    pagina = BeautifulSoup(fp, "html.parser")

# Encontrar os repositórios
repositorios = pagina.find_all("article", class_="Box-row")

dados = []
for idx, repo in enumerate(repositorios[:10], 1):  # Pegamos os 10 primeiros
    # Nome do repositório
    nome_repo = repo.find("h2", class_="h3").find("a").text.strip().replace("\n", "").replace(" ", "")
    
    # Linguagem principal
    linguagem = repo.find("span",attrs={"itemprop": "programmingLanguage"})
    linguagem = linguagem.text.strip() if linguagem else "Desconhecida"

    # Estrelas totais
    estrelas = repo.find("a", class_="Link--muted d-inline-block mr-3")
    estrelas = estrelas.text.strip().replace(",", "") if estrelas else "0"

    # Tentar encontrar todas as tags <a> dentro do repositório
    estrelas = "0"
    tags = repo.find_all("a", class_="Link Link--muted d-inline-block mr-3")
    # Normalmente, a primeira <a> contém as estrelas
    if tags:
        estrelas = tags[0].text.strip().replace(",", "")


    # Estrelas hoje (geralmente com ícone de estrela)
    estrelas_hoje = repo.find("span", class_="d-inline-block float-sm-right")
    estrelas_hoje = estrelas_hoje.text.strip().split()[0].replace(",", "") if estrelas_hoje else "0"

    # Forks
    forks = repo.find_all("a", class_="Link--muted d-inline-block mr-3")
    forks = forks[1].text.strip().replace(",", "") if len(forks) > 1 else "0"
    
    # Tentar encontrar todas as tags <a> dentro do repositório
    forks = "0"
    tags = repo.find_all("a", class_="Link Link--muted d-inline-block mr-3")
    # Verificando no site, a segunda <a> contém os forks
    if tags:
        forks = tags[1].text.strip().replace(",", "")

    # Adicionar ao array de dados
    dados.append([idx, nome_repo, linguagem, estrelas, estrelas_hoje, forks])

# Criar o CSV
with open("github.csv", "w", newline="", encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["ranking", "project", "language", "stars", "stars_today", "forks"])  # Cabeçalhos
    writer.writerows(dados)

print("Arquivo 'github.csv' criado com sucesso!")
