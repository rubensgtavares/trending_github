
# 📊 Trending GitHub Repositories Scraper  

Este repositório contém um script Python para extrair os **10 repositórios mais populares** do [GitHub Trending](https://github.com/trending) e salvar os dados em um arquivo CSV para análise.

## 🚀 Funcionalidades  
- Obtém os **10 primeiros repositórios trending** do GitHub.  
- Extrai informações como:  
  - Nome do repositório (`usuário/repo`)  
  - Linguagem principal  
  - Número de estrelas ⭐  
  - Número de forks 🍴  
- Salva os dados extraídos no arquivo `github.csv`.  

---

## 📦 Requisitos  
Antes de executar o script, certifique-se de ter instalado:  

- Python 3.7+  
- Bibliotecas necessárias (`BeautifulSoup4` e `requests`)  

Para instalar as dependências, execute:  
```bash
pip install -r requirements.txt
```

## ▶️ Como Usar  
### **Clone este repositório:**
```bash
git clone https://github.com/seu-usuario/trending_github.git
cd trending_github
```

```bash
python github_scraper.py
```

O arquivo github.csv será gerado no mesmo diretório com os 10 repositórios mais populares.

📝 Exemplo de Saída (CSV)
Após rodar o script, o arquivo github.csv conterá os dados no seguinte formato:

```bash 
ranking;project;language;stars;forks
1;hacksider/Deep-Live-Cam;Python;47826;3821
2;NVIDIA/TensorRT-LLM;C++;29540;1520
3;agerle/ruoyi-ai;Java;18375;842
4;alibaba/spring-ai-alibaba;Java;17542;803
...
``` 

##🔧 Como Funciona?
O script realiza as seguintes etapas:

Faz uma requisição HTTP para obter a página do GitHub Trending.

Usa BeautifulSoup para extrair os dados dos repositórios.

Formata os dados e os organiza corretamente.

Salva tudo em um arquivo CSV para análise posterior.


##🛠️ Tecnologias Utilizadas
Python 🐍

BeautifulSoup4 (para parsing do HTML)

Requests (para requisições HTTP)

CSV (para salvar os dados)

##📜 Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

💡 Dúvidas ou sugestões? Abra uma issue ou contribua com o projeto! 🚀
