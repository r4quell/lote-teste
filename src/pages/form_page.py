from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.numero_lote_input = (By.ID, "numero_lote")
        self.produto_select = (By.ID, "produto")
        self.status_select = (By.ID, "status")
        self.enviar_button = (By.ID, "btn_enviar")
        self.mensagem_sucesso = (By.ID, "mensagem_sucesso")

    def preencher_formulario(self, dados_lote):
        lote_field = self.wait.until(EC.visibility_of_element_located(self.numero_lote_input))
        lote_field.clear()
        lote_field.send_keys(dados_lote["numero_lote"])

        produto_select = Select(self.driver.find_element(*self.produto_select))
        produto_select.select_by_visible_text(dados_lote["produto"])

        status_select = Select(self.driver.find_element(*self.status_select))
        status_select.select_by_visible_text(dados_lote["status"])

        self.driver.find_element(*self.enviar_button).click()

    def is_sucesso(self):
        elemento = self.wait.until(EC.visibility_of_element_located(self.mensagem_sucesso))
        return elemento.is_displayed()
