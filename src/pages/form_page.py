"""Page Object do formulário de lotes."""

from typing import Any, Mapping

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class FormPage:
    """Encapsula locators, esperas e ações do cadastro de lotes."""

    NUMERO_LOTE = "#lote"
    PRODUTO = "#produto"
    STATUS = "input[name='status'][value='{status}']"
    BOTAO_ENVIAR = "#formulario button[type='submit']"
    MENSAGEM_FINAL = "#mensagem"
    TIMEOUT = 10

    def __init__(self, browser: Any) -> None:
        self._browser = browser
        self._is_playwright = callable(getattr(browser, "locator", None))

    def abrir(self, url: str) -> None:
        """Abre a aplicação e aguarda o formulário ficar disponível."""
        if self._is_playwright:
            self._browser.goto(url, wait_until="domcontentloaded")
            self._browser.locator(self.NUMERO_LOTE).wait_for(
                state="visible", timeout=self.TIMEOUT * 1_000
            )
            return
        self._browser.get(url)
        WebDriverWait(self._browser, self.TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.NUMERO_LOTE))
        )

    def preencher_lote(self, dados_lote: Mapping[str, str]) -> None:
        """Preenche e envia um lote."""
        numero = dados_lote["numero_lote"]
        produto = dados_lote["produto"]
        status = dados_lote["status"]
        status_locator = self.STATUS.format(status=status)

        if self._is_playwright:
            lote_input = self._browser.locator(self.NUMERO_LOTE)
            lote_input.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            lote_input.fill(numero)
            produto_select = self._browser.locator(self.PRODUTO)
            produto_select.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            produto_select.select_option(label=produto)
            status_radio = self._browser.locator(status_locator)
            status_radio.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            status_radio.check()
            botao = self._browser.locator(self.BOTAO_ENVIAR)
            botao.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            botao.click()
            return

        wait = WebDriverWait(self._browser, self.TIMEOUT)
        lote_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.NUMERO_LOTE))
        )
        lote_input.clear()
        lote_input.send_keys(numero)
        Select(wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.PRODUTO))
        )).select_by_visible_text(produto)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, status_locator))).click()
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.BOTAO_ENVIAR))
        ).click()

    def is_sucesso(self) -> bool:
        """Retorna se a mensagem de sucesso ficou visível."""
        if self._is_playwright:
            mensagem = self._browser.locator(self.MENSAGEM_FINAL)
            mensagem.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            return mensagem.is_visible()
        return WebDriverWait(self._browser, self.TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.MENSAGEM_FINAL))
        ).is_displayed()
