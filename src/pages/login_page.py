"""Page Object da tela de login."""

from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Encapsula locators, esperas e ações de uma tela de login."""

    USUARIO = "#usuario"
    SENHA = "#senha"
    BOTAO_LOGIN = "#entrar"
    TIMEOUT = 10

    def __init__(self, browser: Any) -> None:
        self._browser = browser
        self._is_playwright = callable(getattr(browser, "locator", None))

    def fazer_login(self, usuario: str, senha: str) -> None:
        """Preenche as credenciais fictícias e envia o formulário."""
        if self._is_playwright:
            usuario_input = self._browser.locator(self.USUARIO)
            usuario_input.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            usuario_input.fill(usuario)
            senha_input = self._browser.locator(self.SENHA)
            senha_input.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            senha_input.fill(senha)
            botao = self._browser.locator(self.BOTAO_LOGIN)
            botao.wait_for(state="visible", timeout=self.TIMEOUT * 1_000)
            botao.click()
            return

        wait = WebDriverWait(self._browser, self.TIMEOUT)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.USUARIO))).send_keys(usuario)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SENHA))).send_keys(senha)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.BOTAO_LOGIN))).click()
