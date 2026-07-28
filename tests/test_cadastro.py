from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
for path in [str(ROOT), str(SRC)]:
    if path not in sys.path:
        sys.path.insert(0, path)

from main import URL_BASE, criar_driver, start_http_server, stop_http_server
from pages.login_page import LoginPage
from pages.form_page import FormPage


@pytest.fixture
def browser():
    server = start_http_server()
    driver = criar_driver()
    try:
        driver.get(URL_BASE)
        yield driver
    finally:
        driver.quit()
        stop_http_server(server)


def test_cadastro_lote(browser):
    login_page = LoginPage(browser)
    login_page.fazer_login("standard_user", "secret_sauce")

    assert "inventory.html" in browser.current_url

    form_page = FormPage(browser)
    dados_lote = {
        "numero_lote": "LOTE-2025-0001",
        "produto": "Notebook",
        "status": "Concluído",
    }
    form_page.preencher_formulario(dados_lote)

    assert form_page.is_sucesso() is True
