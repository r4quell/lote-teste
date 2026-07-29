# Automação e Cadastro de Lotes com Page Object Model

## Objetivo

Este projeto demonstra automação de interface em um ambiente fictício de
cadastro de lotes de produção. A implementação aplica Page Object Model (POM)
para separar o mapeamento e as interações com elementos web da lógica de
execução, facilitando reutilização, manutenção e testes.

O formulário contém número do lote, produto, status e a ação de processamento.
Nenhuma credencial ou sistema real é utilizado.

## Tecnologias

- Python 3.12 ou superior
- Selenium
- Playwright
- pytest
- webdriver-manager

## Arquitetura

```text
src/
├── pages/
│   ├── login_page.py
│   └── form_page.py
├── automation/
│   ├── common.py
│   ├── web_automation.py
│   └── selenium_automation.py
├── config/
├── utils/
└── main.py
tests/
└── test_pages.py
```

Os Page Objects concentram locators, esperas explícitas e ações de UI. Os
orquestradores concentram fluxo, iteração, logs, screenshots, exceções e
DataPool. `LoginPage` está preparado para uma futura tela de autenticação; o
HTML local atual contém somente o formulário e usa diretamente `FormPage`.

## Fluxo da automação

1. A CLI seleciona Selenium ou Playwright.
2. O Page Object abre `lote-teste.html`.
3. O orquestrador entrega um dicionário de lote a `preencher_lote`.
4. `is_sucesso` valida a confirmação.
5. São salvos screenshot, JSON, log e o caminho no DataPool local.

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Execução

```bash
python bot.py --engine selenium
python bot.py --engine playwright
```

Use `--headed` para exibir o navegador. Evidências são gravadas em
`evidencias/` e o DataPool simulado em `datapool.json`.

## Testes

```bash
python -m pytest
```

Os testes usam doubles e não acessam navegador ou sistema real.

## DataPool e Maestro

`DataPool` é um protocolo injetável. `JsonDataPool` oferece execução local; um
gateway BotCity Maestro pode implementar o mesmo método `registrar` usando
credenciais fornecidas pelo ambiente, sem contaminar os Page Objects.

## GitFlow

O trabalho é desenvolvido na branch `feature/page-object` com commit semântico:

```text
feat(page-object): implement Page Object Model for web automation
```

Consulte [PDD.md](PDD.md) para responsabilidades, fluxograma e rastreabilidade.

## Equipe

- Carlos Souza
- Gustavo Nunes
- Raquel
