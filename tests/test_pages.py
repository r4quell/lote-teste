"""Testes unitários dos Page Objects sem acessar sistemas reais."""

from unittest.mock import MagicMock

from src.pages.form_page import FormPage
from src.pages.login_page import LoginPage


def test_form_page_playwright_preenche_e_valida_sucesso() -> None:
    page = MagicMock()
    page.locator = MagicMock()
    locators: dict[str, MagicMock] = {}

    def locator(selector: str) -> MagicMock:
        return locators.setdefault(selector, MagicMock())

    page.locator.side_effect = locator
    form = FormPage(page)
    dados = {"numero_lote": "L-1", "produto": "Mouse", "status": "Pendente"}

    form.preencher_lote(dados)
    mensagem = locator(FormPage.MENSAGEM_FINAL)
    mensagem.is_visible.return_value = True

    assert form.is_sucesso() is True
    locators[FormPage.NUMERO_LOTE].fill.assert_called_once_with("L-1")
    locators[FormPage.PRODUTO].select_option.assert_called_once_with(label="Mouse")
    locators[FormPage.STATUS.format(status="Pendente")].check.assert_called_once()
    locators[FormPage.BOTAO_ENVIAR].click.assert_called_once()


def test_login_page_playwright() -> None:
    page = MagicMock()
    page.locator = MagicMock()
    locators: dict[str, MagicMock] = {}
    page.locator.side_effect = lambda selector: locators.setdefault(selector, MagicMock())

    LoginPage(page).fazer_login("usuario-demo", "senha-demo")

    locators[LoginPage.USUARIO].fill.assert_called_once_with("usuario-demo")
    locators[LoginPage.SENHA].fill.assert_called_once_with("senha-demo")
    locators[LoginPage.BOTAO_LOGIN].click.assert_called_once()
