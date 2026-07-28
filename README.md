# Automação e Raspagem: Cadastro de Lotes de Produção

## Objetivo

O Principal objetivo deste projeto é compreender e aplicar o processo de raspagem
de dados (Web Scraping) e automação de interface utilizando padrões de projeto,
com destaque para o **Page Object Model (POM)**.

A ideia é criar classes raspagem modulares, que separa os mapeamentos dos elementos web da lógica
de execução. Promovendo:

- **Reaproveitamento de código**
- **Código Limpo**
- **Conciso e de fácil de Manutenção**

## Cenário

O projeto automatiza as interações com um sistema corporativo (ambiente de teste)
focado no **Cadastro de Lotes de Produção**. O Formulário é composto pelo seguintes elementos:
- **Número do Lote:** Campo de entrada de texto (ex: `LOTE-2025-0001`).
- **Produto:** Menu de seleção (*dropdown*) contendo opções como Notebook, Mouse, Teclado e Monitor.
- **Status:** Botões de rádio (*radio buttons*) para os estados "Pendente", "Em Processamento" e "Concluído".
- **Ação:** Botão "Processar Lote", que aciona a simulação de cadastro e exibe a mensagem de sucesso no sistema.


## Tecnologias Utilizadas

- **Linguagem de Programação:** Python 3.12
- **Bibliotecas de Automação e Raspagem:**
  - Selenium
  - Webdriver-manager
  - Playwright


## Estrutura do projeto
```text
projeto-pom/
├── src/
│   └── pages/
│       ├── __init__.py
│       ├── login_page.py
│       └── form_page.py
├── tests/
│   └── test_cadastro.py
├── main.py
├── index.html
├── inventory.html
├── requirements.txt
└── README.md
```

## Instalação
```bash
pip install -r requirements.txt
```

## Execução
```bash
python main.py
```

## Execução dos testes
```bash
pytest
```

## Padrões de Projetos aplicados

- **Page Object Model (POM):** Utilizado para mapear as páginas da aplicação em classes distintas. Em vez de espalhar seletores e interações (como *clicks* e *inputs*) pelos scripts principais, tudo é encapsulado em métodos dentro da classe da página (ex: `PaginaCadastroLote`).
- **Orientação a Objetos (POO):** Encapsulamento, abstração e reutilização de componentes.

## Membros da Equipe
- Carlos Souza
- Gustavo Nunes
- Raquel
