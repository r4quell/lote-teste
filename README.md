# Projeto POM com Selenium

## Objetivo
Este projeto demonstra uma refatoração para o padrão Page Object Model (POM) em automação web com Selenium, separando a interação com a interface das regras de fluxo do script principal.

## Tecnologias utilizadas
- Python
- Selenium
- pytest
- webdriver-manager

## Padrão Page Object Model
A lógica de interação com os elementos da página foi encapsulada em classes específicas:
- LoginPage: responsável pelo acesso e login
- FormPage: responsável pelo preenchimento e validação do formulário

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

## Benefícios da refatoração
- Código mais limpo e legível
- Reutilização de locators e ações em páginas específicas
- Facilidade de manutenção e escalabilidade
- Separação clara entre orquestração e automação de interface
