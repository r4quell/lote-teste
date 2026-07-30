"""Teste integrado do cadastro local com Selenium."""

from pathlib import Path

import pytest
from selenium import webdriver

from src.pages import FormPage


ROOT = Path(__file__).resolve().parents[1]
URL_BASE = (ROOT / "lote-teste.html").as_uri()


@pytest.fixture
def browser() -> webdriver.Chrome:
    """Cria e encerra um navegador isolado para o teste."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()


def test_cadastro_lote(browser: webdriver.Chrome) -> None:
    """Cadastra um lote fictício pela interface local."""
    form_page = FormPage(browser)
    form_page.abrir(URL_BASE)
    form_page.preencher_lote(
        {
            "numero_lote": "LOTE-2025-0001",
            "produto": "Notebook",
            "status": "Pendente",
        }
    )

    assert form_page.is_sucesso() is True
